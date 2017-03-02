import common
import random
import string
import struct
import socket
import hashlib
import phonenumbers
from common import AppServer

def client_send(sock, protocol, data):
    (body_len, packet) = pack(protocol, data)
    header = struct.pack('>3I', body_len, protocol, 0)
    packet = header + packet
    try:
        sock.sendall(packet)
    except socket.error:
        print('socket except happend.')
        sock.close()

def socket_close(sock):
    try:
        sock.shutdown(socket.SHUT_WR)
    except socket.error:
        pass
    sock.close()

def system_send(protocol, data):
    (body_len, packet) = pack(protocol, data)
    api = 0
    num = 0
    sys = 0
    header = struct.pack('>5I', body_len, api, protocol, num, sys)
    packet = header + packet
    return AppServer.send(packet)

def system_request(protocol, data):
    (body_len, packet) = pack(protocol, data)
    api = 0
    num = 0
    sys = 0
    header = struct.pack('>5I', body_len, api, protocol, num, sys)
    packet = header + packet
    return AppServer.request(packet)

def system_response(sock, protocol, data):
    (body_len, packet) = pack(protocol, data)
    header = struct.pack('>2I', body_len, protocol)
    packet = header + packet
    try:
        sock.sendall(packet)
    except socket.error:
        print('socket except happend')
        sock.close()

def pack(protocol, data):
    if isinstance(protocol, int):
        if not isinstance(data, bytes):
            body_len = data.ByteSize()
            packet   = data.SerializeToString()
        else:
            body_len = len(data)
            packet   = data
    else:
        raise RuntimeError("protocol must an integer.")
    return (body_len, packet)

def md5(x):
    m = hashlib.md5()
    m.update(x.encode())
    return m.hexdigest()

def make_rand(size):
    chars = string.ascii_letters + string.digits
    return ''.join((random.choice(chars) for _ in range(size)))

def verify_phone(phone, country='CN'):
    try:
        phone_number = phonenumbers.parse(phone, country)
    except phonenumbers.NumberParseException:
        return False
    return phonenumbers.is_valid_number(phone_number)

def make_authcode():
    return random.randint(common.AUTHCODE_MIN, common.AUTHCODE_MAX)
