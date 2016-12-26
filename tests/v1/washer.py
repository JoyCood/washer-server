#!/usr/bin/python 
# -*- coding: utf-8 -*-

import os
import sys
import socket
import inspect
import common

WASHER_PHONE = '+8618565389757'

def fresh_location(socket):
    pb = washer_pb2.Fresh_Location_Request()
    pb.longitude = 120.21937542
    pb.latitude  = 30.25924446
    pb.city_code = 179

    common.send(socket, washer_pb2.FRESH_LOCATION, pb)
    body = common.get(socket)
    if body:
        resp = washer_pb2.Fresh_Location_Response()
        resp.ParseFromString(body)
        print('fresh_location result:')
        print(resp.error_code)

def get_near_washer(socket):
    pb = washer_pb2.Near_Washer_Request()
    pb.city_code = 179
    pb.longitude = 120.21937542
    pb.latitude  = 30.25924446
    common.send(socket, washer_pb2.NEAR_WASHER, pb)
    body = common.get(socket)
    if body:
        resp = washer_pb2.Near_Washer_Response()
        resp.ParseFromString(body)
        print(resp)
        #for washer in resp.washer:
        #    print "------------"
        #    print washer.phone

#请求验证码
def request_authcode(socket):
    requestAuthcode = washer_pb2.Request_Authcode_Request()
    requestAuthcode.phone = WASHER_PHONE
    requestAuthcode.signature = 'signature'
    common.send(socket, washer_pb2.REQUEST_AUTHCODE, requestAuthcode)
    body = common.get(socket)
    if body:
        raResponse = washer_pb2.Request_Authcode_Response()
        raResponse.ParseFromString(body)
        print('request_authcode response:{!r}'.format(raResponse))
        return raResponse.authcode
    return False

#校验验证码
def verify_authcode(socket):
    authcode = request_authcode(socket)
    if not authcode:
        print('get request authcode failure..')
        return
    verifyAuthcode = washer_pb2.Verify_Authcode_Request()
    verifyAuthcode.phone = WASHER_PHONE
    verifyAuthcode.authcode = authcode
    verifyAuthcode.signature = 'signature'
    common.send(socket, washer_pb2.VERIFY_AUTHCODE, verifyAuthcode)
    body = common.get(socket)
    if body:
        va = washer_pb2.Verify_Authcode_Response()
        va.ParseFromString(body);
        if va.error_code == washer_pb2.SUCCESS:
            print("verify authcode success:%s" % va.error_code)
            return authcode
    print('verify authcode failure')
    return False

#注册
def register(socket):
    authcode = verify_authcode(socket)
    if not authcode:
        return
    pb = washer_pb2.Register_Request()
    pb.phone = WASHER_PHONE
    pb.authcode = authcode
    pb.password = 'iwasher'
    pb.password2 = 'iwasher'
    pb.nick = 'iwasher'
    pb.signature = 'signature'
    common.send(socket, washer_pb2.REGISTER, pb)
    body = common.get(socket)
    if body:
        res = washer_pb2.Register_Response()
        res.ParseFromString(body)
        print(res)
        print('finish register')

def login(socket):
    washer = washer_pb2.Login_Request()
    washer.phone = WASHER_PHONE
    washer.password = 'iwasher'
    washer.signature = 'signature'
    common.send(socket, washer_pb2.LOGIN, washer)
    body = common.get(socket)
    if body:
        washerResponse = washer_pb2.Login_Response()
        washerResponse.ParseFromString(body)
        print(washerResponse)
        return
    print('login failure')
    

if __name__ == '__main__':
    filepath = os.path.realpath(__file__)
    sys.path.append(os.path.dirname(os.path.realpath(__file__))[:-8])
    from protocol.v1 import washer_pb2
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((common.WASHER_BIND_HOST, common.WASHER_BIND_PORT))
    sys.stdout.write("%")

    while True:
        fun = sys.stdin.readline()
        if fun == '\n':
            client.close()
            break
        fun = fun.strip('\n')
        fun_list = inspect.getmembers(sys.modules[__name__], inspect.isfunction)
        fun_list = map(common.fun_filter, fun_list)
        if fun in fun_list:
            f = getattr(sys.modules[__name__], fun)
            f(client)
