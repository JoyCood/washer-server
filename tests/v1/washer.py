#!/usr/bin/python 
# -*- coding: utf-8 -*-

import os
import sys
import socket
import inspect
import common

WASHER_PHONE = '+8613533332424'

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
    common.send(socket, common_pb2.REQUEST_AUTHCODE, requestAuthcode)
    (protocol, body) = common.get(socket)
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
    common.send(socket, common_pb2.VERIFY_AUTHCODE, verifyAuthcode)
    (protocol,body) = common.get(socket)
    if body:
        va = washer_pb2.Verify_Authcode_Response()
        va.ParseFromString(body);
        if va.error_code == common_pb2.SUCCESS:
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
    pb.type = common_pb2.PERSONAL
    common.send(socket, common_pb2.REGISTER, pb)
    (protocol, body) = common.get(socket)
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
    #washer.city_code = 179
    #washer.longitude = 120.025806
    #washer.latitude  = 30.246185
    common.send(socket, common_pb2.LOGIN, washer)
    (protocol, body) = common.get(socket)
    if body:
        washerResponse = washer_pb2.Login_Response()
        washerResponse.ParseFromString(body)
        print(washerResponse)
        return True
    print('login failure')

def wechat_pay(socket):
    login(socket)
    request = order_pb2.Wechat_Pay_Request()
    request.order_id = '123456677756443'
    common.send(socket, common_pb2.WECHAT_PAY, request)
    (protocol, body) = common.get(socket)
    if body:
        response = order_pb2.Wechat_Pay_Response()
        response.ParseFromString(body)
        print(response)

    
def start_work(socket):
    result = login(socket)
    if result is None:
        print('login first')
        return
    request = washer_pb2.Start_Work_Request()
    request.city_code = 179
    request.longitude = 120.025806
    request.latitude  = 30.246185
    common.send(socket, common_pb2.START_WORK, request)
    print("start work, protocol:{}".format(common_pb2.START_WORK))
    while True:
        body = common.get(socket)
        if not body:
            break
        else:
            (protocol, data) = body
            if protocol == common_pb2.START_WORK:
                print("protocol: start_work")
                response = washer_pb2.Start_Work_Response()
                response.ParseFromString(data)
                print(response)

            elif protocol == common_pb2.ALLOCATE_ORDER:
                print("protocol: allocate_order")
                response = order_pb2.Allocate_Order_Push()
                response.ParseFromString(data)
                print(response)

                request = order_pb2.cancel_order_
                
                print("protocol: processing_order")
                request = order_pb2.Processing_Order_Request()
                request.order_id = response.order_id
                common.send(socket, common_pb2.PROCESSING_ORDER, request)

                print("protocol: finish_order")
                request = order_pb2.Finish_Order_Request()
                request.order_id = response.order_id
                common.send(socket, common_pb2.FINISH_ORDER, request)

                print("protocol: order_feedback")
                request = order_pb2.Order_Feedback_Request()
                request.order_id = response.order_id
                request.score = 5
                common.send(socket, common_pb2.ORDER_FEEDBACK, request)
                
            elif protocol == common_pb2.FINISH_ORDER:
                print("protocol: finish_order" )
                response = order_pb2.Finish_Order_Response()
                response.ParseFromString(data)
                print(response)

def stop_work(socket):
    request = washer_pb2.Stop_Work_Request()    
    common.send(socket, common_pb2.STOP_WORK, request)
    body = common.get(socket)
    if body:
        (protocol, data) = body
        response = washer_pb2.Stop_Work_Response()
        response.ParseFromString(data)
        print(response)

if __name__ == '__main__':
    filepath = os.path.dirname(os.path.realpath(__file__))[:-8] + "protocol/v1"
    sys.path.append(filepath)
    import washer_1_pb2 as washer_pb2
    import common_1_pb2 as common_pb2
    import order_1_pb2  as order_pb2
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
