import os
import sys
import socket
import struct

WASHER_BIND_HOST = '127.0.0.1'
WASHER_BIND_PORT = 8888

def fun_filter(fun):
    (name, value) = fun
    return name # return fun[0]

def send(sock, protocol, data):
    packet = data.SerializeToString()
    body_len = data.ByteSize()
    header = struct.pack('>5I', body_len, 2, protocol, 0, 1)
    packet = header + packet
    return sock.send(packet)

def get(sock):
    try:
        header = sock.recv(12)
        if header:
            (body_len, protocol, num) = struct.unpack('>3I', header)
            if body_len:
                body = sock.recv(body_len)
                return body
        return False
    except socket.error:
        return False
