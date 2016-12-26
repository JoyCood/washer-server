#!/usr/bin/python 
# -*- coding: utf-8 -*-

import sys
import time
import common
import hashlib

from helper import helper
from .protocol import route
from protocol.v1 import washer_pb2
from model.washer.washer import Washer
from model.washer.washer import Mix as Washer_Mix
from pymongo.errors import DuplicateKeyError

def handle(socket, protocol, platform, data):
    handler = route.get(protocol)
    if handler is None:
        print("protocol:{} handler is not found".format(protocol))
        return
    fun = getattr(sys.modules[__name__], handler)
    fun(socket, platform, data)

#登录
def login(socket, platform, data):
    request = washer_pb2.Login_Request()
    request.ParseFromString(data)

    phone     = request.phone.strip()
    password  = request.password.strip()
    uuid      = request.uuid.strip()
    signature = request.signature.strip()

    response = washer_pb2.Login_Response()

    if not helper.verify_phone(phone):
        print('phone invalid.')
        response.error_code = washer_pb2.ERROR_PHONE_INVALID
        helper.client_send(socket, platform, washer_pb2.LOGIN, response)
        return
    
    if password:
        _login(socket, phone, password)
        return
    
    if signature:
        _reconnect(socket, phone, uuid, signature)
        return

    print('bad request.')
    response.error_code = washer_pb2.ERROR_BADREQEUST
    helper.client_send(socket, washer_pb2.LOGIN, response)

#密码登录
def _login(socket, phone, password):
    response = washer_pb2.Login_Response()

    md5 = hashlib.md5()
    md5.update(password.encode())
    password = md5.hexdigest()
    
    filter = {
        "phone": phone        
    }
    washer = Washer.find_one(filter)

    if washer is None:
        response.error_code = washer_pb2.ERROR_WASHER_NOT_FOUND
        helper.client_send(socket, washer_pb2.LOGIN, response)
        print('washer:{} not found.'.format(phone))
        return
    elif washer['password'] != password:
        response.error_code = washer_pb2.ERROR_PASSWORD_INVALID
        helper.client_send(socket, washer_pb2.LOGIN, response)
        print('password invalid.')
        return
    print('login success')
    response.washer.id       = str(washer['_id'])
    response.washer.phone    = washer['phone']
    response.washer.nick     = washer['nick']
    response.washer.avatar   = washer['avatar']
    response.washer.level    = washer['level']
    response.washer.reg_time = washer['reg_time']
    response.washer.status   = washer['status']
    response.error_code      = washer_pb2.SUCCESS
    helper.client_send(socket, washer_pb2.LOGIN, response)

#断线重连
def _reconnect(socket, phone, uuid, signature):
    response = washer_pb2.Login_Response()

    result = verify_signature(phone, uuid, signature)

    if not result:
        response.error_code = washer_pb2.ERROR_BADREQUEST
        helper.client_send(socket, washer_pb2.LOGIN, response)
        return

    filter = {"phone":phone}
    washer = Washer.find_one(filter)
    if washer is None: #r找不到商家
        print('washer not found.')
        response.error_code = washer_pb2.ERROR_WASHER_NOT_FOUND
        helper.client_send(socket, washer_pb2.LOGIN, response)
        return
    
    _washer['socket'] = socket
    _washer['phone']  = washer['phone']
    add_online_washer(_washer)

    response.id     = str(washer['_id'])
    response.nick   = washer['nick']
    response.phone  = washer['phone']
    response.avatar = washer['avatar']
    response.level  = washer['level']
    response.status = washer['status']
    response.secret = result['secret']
    helper.client_send(socket, washer_pb2.LOGIN, response)

#注册
def register(socket, platform, data):
    request = washer_pb2.Register_Request()
    request.ParseFromString(data)

    nick      = request.nick.strip()
    phone     = request.phone.strip()
    authcode  = request.authcode
    password  = request.password.strip()
    password2 = request.password2.strip()
    avatar    = request.avatar.strip()
    signature = request.signature.strip()

    response = washer_pb2.Register_Response()

    if password != password2:
        response.error_code = washer_pb2.ERROR_PASSWORD_NOT_EQUAL
        helper.client_send(socket, washer_pb2.REGISTER, response)
        print('password not equal')
        return
    elif not helper.verify_phone(phone):
        response.error_code = washer_pb2.ERROR_PHONE_INVALID
        helper.client_send(socket, washer_pb2.REGISTER, response)
        print('phone invalid')
        return

    now = int(time.time())

    filter = {"phone": phone}
    washer = Washer.find_one(filter)
    washer_mix = Washer_Mix.find_one(filter)

    if washer is not None:
        print('washer:{} exist.'.format(phone))
        response.error_code = washer_pb2.ERROR_WASHER_EXIST
        helper.client_send(socket, washer_pb2.REGISTER, response)
        return
    elif washer_mix is None or washer_mix['authcode'] != authcode:
        print('authcode:{} invalid'.format(authcode))
        response.error_code = washer_pb2.ERROR_AUTHCODE_INVALID
        helper.client_send(socket, washer_pb2.REGISTER, response)
        return
    elif washer_mix['expired'] < now:
        print('autchode expired.')
        response.error_code = washer_pb2.ERROR_AUTHCODE_EXPIRED
        helper.client_send(socket, washer_pb2.REGISTER, response)
        return

    md5 = hashlib.md5()
    md5.update(password.encode())
    password = md5.hexdigest()

    doc = {
        "nick": nick,
        "phone": phone,
        "password": password,
        "avatar": avatar,
        "status": 0,
        "reg_time": now,
        "last_login": now,
        "level": common.WASHER_INIT_LEVEL
    }

    try:
        result = Washer.insert_one(doc)
        response.washer.id     = str(result.inserted_id)
        response.washer.phone  = phone
        response.washer.nick   = nick
        response.washer.level  = common.WASHER_INIT_LEVEL
        response.washer.status = 0
        response.washer.avatar = avatar
        response.error_code = washer_pb2.SUCCESS
        helper.client_send(socket, washer_pb2.REGISTER, response)
        print('register success')
    except DuplicateKeyError:
        response.error_code = washer_pb2.ERROR_WASHER_EXIST
        helper.client_send(socket, washer_pb2.REGISTER, response)
        print('duplicate key error, washer exist')

#发送验证码
def request_authcode(socket, platform, data):
    request = washer_pb2.Request_Authcode_Request()
    request.ParseFromString(data)
    
    phone = request.phone.strip()
    signature = request.signature.strip()

    response = washer_pb2.Request_Authcode_Response()

    if not helper.verify_phone(phone):
        print("phone:{} invalid".format(phone))
        response.error_code = washer_pb2.ERROR_PHONE_INVALID
        helper.client_send(socket, washer_pb2.REQUEST_AUTHCODE, response)
        return

    filter = {"phone": phone}
    washer_mix = Washer_Mix.find_one(filter)

    now = int(time.time())
    authcode = None

    filter = {"phone": phone}
    washer_mix = Washer_Mix.find_one(filter)

    if washer_mix is None: #验证码不存在则重新生成
        authcode = helper.make_authcode()
        expired  = now + common.AUTHCODE_EXPIRED_TIME
        doc = {
            "phone": phone,
            "authcode": authcode,
            "expired": expired,
            "create_time": now
        }
        result = Washer_Mix.insert_one(doc)
    elif washer_mix['expired'] < now: #验证码已过期则重新生成
        authcode = helper.make_authcode()
        expired  = now + common.AUTHCODE_EXPIRED_TIME
        doc = {
            "$set": {
                "authcode": authcode,
                "expired":  expired,
                "create_time": now
            }        
        }
        result = Washer_Mix.update_one(filter, doc)
    
    print('request authcode success')
    authcode = authcode or washer_mix['authcode']
    response.authcode = authcode
    response.error_code = washer_pb2.SUCCESS
    helper.client_send(socket, washer_pb2.REQUEST_AUTHCODE, response)

#校验验证码
def verify_authcode(socket, platform, data):
    request = washer_pb2.Verify_Authcode_Request()
    request.ParseFromString(data)

    phone = request.phone.strip()
    authcode = request.authcode
    signature = request.signature.strip()

    response = washer_pb2.Verify_Authcode_Response()

    if not helper.verify_phone(phone):
        print('phone:{} invalid'.format(phone))
        response.error_code = washer_pb2.ERROR_PHONE_INVALID
        helper.client_send(socket, washer_pb2.VERIFY_AUTHCODE, response)
        return

    filter = {"phone": phone}
    washer_mix = Washer_Mix.find_one(filter)

    if washer_mix is None or washer_mix['authcode'] != authcode:
        print('authcode invalid')
        response.error_code = washer_pb2.ERROR_AUTHCODE_INVALID
        helper.client_send(socket, washer_pb2.VERIFY_AUTHCODE, response)
        return
    elif washer_mix['expired'] < int(time.time()):
        print('authcode expired')
        response.error_code = washer_pb2.ERROR_AUTHCODE_EXPIRED
        helper.client_send(socket, washer_pb2.VERIFY_AUTHCODE, response)
        return

    print('verify authcode success') 
    response.error_code = washer_pb2.SUCCESS
    helper.client_send(socket, washer_pb2.VERIFY_AUTHCODE, response)

#校验签名
def verify_signature(phone, uuid, signature):
    filter = {"phone": phone}
    washer_mix = Washer_Mix.find_one(filter)
    if washer_mix is None:
        return False
    signature2 = [washer_mix['secret']]
    signature2.append(common.WASHER_KEY)
    signature2.append(uuid)
    signature2.append(phone)

    signature2 = ''.join(signature2)
    signature2 = helper.md5(signature2)

    return signature2 == signature

#开工
def start_work(socket, platform, data):
    washer = get_washer_by_socket(socket)
    if washer is None:
        response.error_code = washer_pb2.ERROR_NOT_LOGIN
        helper.client_send(socket, washer_pb2.START_WORK, response)
        return
    if washer['status'] == 1:
        response.error_code = washer_pb2.ERROR_ALREAD_START
        helper.client_send(socket, washer_pb2.START_WORK, response)
        return
    washer['status'] = 1
    add_washer(washer)
    response.error_code = washer_pb2.SUCCESS
    helper.client_send(socket, washer_pb2.START_WORK, response)

#收工
def stop_work(socket, platform, data):
    pass

#分配商家
def allocate_washer(socket, platform, data):
    pass

def fresh_location(socket, platform, data):
    pass
