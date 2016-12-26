#!/usr/bin/python 
# -*- coding: utf-8 -*-

from itertools import chain
import os
import socket
import sys
import threading
from .exceptions import (ConnectionError, TimeoutError)
from queue import LifoQueue
import struct

class IWasher(object):
    def __init__(self, host, port, socket_timeout=20, retry_on_timeout=False, socket_connect_timeout=None, socket_keepalive=False, socket_keepalive_options=None, max_connections=None):

        kwargs = {
            'host': host,
            'port': port,
            'max_connections': max_connections,
            'socket_keepalive': socket_keepalive,
            'socket_keepalive_options': socket_keepalive_options,
            'socket_timeout': socket_timeout,
            'retry_on_timeout': retry_on_timeout
        }
        self.connection_pool = ConnectionPool(**kwargs)

    def request(self, data):
        connection = self.connection_pool.get_connection()
        try:
            connection.send(data)
            return connection.response()
        except (ConnectionError, TimeoutError) as e:
            connection.disconnect()
            if not connection.retry_on_timeout and isinstance(e, TimeoutError):
                raise
            connection.send(data)
            return connection.response()
        finally:
            self.connection_pool.release(connection)

    def send(self, data):
        connection = self.connection_pool.get_connection()
        try:
            connection.send(data)
        except (ConnectionError, TimeoutError) as e:
            if not connection.retry_on_timeout and isinstance(e, TimeoutError):
                raise
            connection.send(data)
        finally:
            self.connection_pool.release(connection)

class Connection(object):
    def __init__(self, host, port, socket_timeout=None, socket_connect_timeout=None, socket_keepalive=False, socket_keepalive_options=None, retry_on_timeout=False):

        self.pid = os.getpid()
        self.host = host
        self.port = port
        self.socket_timeout = socket_timeout
        self.retry_on_timeout = retry_on_timeout
        self.socket_connect_timeout = socket_connect_timeout or socket_timeout
        self.socket_keepalive = socket_keepalive
        self.socket_keepalive_options = socket_keepalive_options or {}
        self._sock = None
        self.header_len = 8

    def connect(self):
        if self._sock:
            return
        try:
            sock = self._connect()
        except socket.error:
            e = sys.exc_info()[1]
            raise ConnectionError(self._error_message(e))
        self._sock = sock

    def _connect(self):
        err = None
        for res in socket.getaddrinfo(self.host, self.port, 0, socket.SOCK_STREAM):
            family, socktype, proto, canonname, socket_address = res
            sock = None
            try:
                sock = socket.socket(family, socktype, proto)
                sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                if self.socket_keepalive:
                    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
                    for k, v in iteritems(self.socket_keepalive_options):
                        sock.setsockopt(socket.SOL_TCP, k, v)
                sock.settimeout(self.socket_connect_timeout)
                sock.connect(socket_address)
                sock.settimeout(self.socket_timeout)
                return sock
            except socket.error as e:
                err = e
                if sock is not None:
                    sock.close()
            if err is not None:
                raise err
            raise socket.err("socket.getaddrinfo returned an empty list")

    def disconnect(self):
        if self._sock is None:
            return
        try:
            self._sock.shutdown(socket.SHUT_RDWR)
            self._sock.close()
        except socket.error:
            pass
        self._sock = None

    def send(self, data):
        if not self._sock:
            self.connect()
        try:
            self._sock.sendall(data)
        except socket.timeout:
            self.disconnect()
            raise TimeoutError("Timeout writing to socket")
        except socket.error:
            e = sys.exc_info()[1]
            self.disconnect()
            if len(e.args) == 1:
                errno, errmsg = 'UNKNOW', e.args[0]
            else:
                errno  = e.args[0]
                errmsg = e.args[1]
            raise ConnectionError("Error {} while writing to socket. {}".format(errno, errmsg))
        except:
            self.disconnect()
            raise

    def response(self):
        try:
            header = self._sock.recv(self.header_len)
            (body_len, protocol) = struct.unpack('>2I', header)
            return self._sock.recv(body_len)
        except socket.timeout:
            self.disconnect()
            raise TimeoutError("Timeout reading from socket")
        except socket.error:
            self.disconnect()
            e = sys.exc_info()[1]
            raise ConnectionError("Error while reading from socket:{}".format(e.args,))

    def _error_message(self, exception):
        if len(exception.args) == 1:
            return "Error connecting to {}:{} {}.".format(self.host, self.port, exception.args[0]) 
        else:
            return "Error {} connecting to {}:{} {}".format(exception.args[0], self.host, self.port, exception.args[1])


class ConnectionPool(object):
    def __init__(self, connection_class=Connection, max_connections=None, **connection_kwargs):
        max_connections = max_connections or 2 ** 10
        if not isinstance(max_connections, int) or max_connections < 0:
            raise ValueError('"max_connections" must be a positive integer')
        self.connection_class  = connection_class
        self.connection_kwargs = connection_kwargs
        self.max_connections   = max_connections
        self.reset()

    def reset(self):
        self.pid = os.getpid()
        self._created_connections = 0
        self._available_connections = []
        self._in_use_connections = set()
        self._check_lock = threading.Lock()

    def _checkpid(self):
        if self.pid != os.getpid():
            with self._check_lock:
                if self.pid == os.getpid():
                    return
                self.disconnect()
                self.reset()

    def get_connection(self):
        self._checkpid()
        try:
            connection = self._available_connections.pop()
        except IndexError:
            connection = self.make_connection()
        self._in_use_connections.add(connection)
        return connection

    def make_connection(self):
        """ create a new connection """
        if self._created_connections >= self.max_connections:
            raise ConnectionError("Too many connections")
        self._created_connections += 1
        return self.connection_class(**self.connection_kwargs)

    def release(self, connection):
        """ release the connection back to the pool """
        self._checkpid()
        if connection.pid != self.pid:
            return
        self._in_use_connections.remove(connection)
        self._available_connections.append(connection)

    def disconnect(self):
        """ disconnects all connection in the pool """
        all_conns = chain(self._available_connections, self._in_use_connections)
        for connection in all_conns:
            connection.disconnect()

