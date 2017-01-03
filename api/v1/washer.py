#!/usr/bin/python 
# -*- coding: utf-8 -*-

import sys
import time
import hashlib

import common
from helper import helper
from .protocol import route
import common_1_pb2 as common_pb2
import washer_1_pb2 as washer_pb2
import order_1_pb2  as order_pb2
from model.washer.washer import Washer
from model.washer.washer import Mix as Washer_Mix
from model.order.order import Order
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
        response.error_code = common_pb2.ERROR_PHONE_INVALID
        helper.client_send(socket, platform, common_pb2.LOGIN, response)
        return
    
    if password:
        _login(socket, phone, password, uuid)
        return
    
    if signature:
        _reconnect(socket, phone, uuid, signature)
        return

    print('bad request.')
    response.error_code = common_pb2.ERROR_BADREQEUST
    helper.client_send(socket, common_pb2.LOGIN, response)

#密码登录
def _login(socket, phone, password, uuid):
    response = washer_pb2.Login_Response()

    md5 = hashlib.md5()
    md5.update(password.encode())
    password = md5.hexdigest()
    
    filter = {
        "phone": phone        
    }
    washer = Washer.find_one(filter)

    if washer is None:
        response.error_code = common_pb2.ERROR_WASHER_NOT_FOUND
        helper.client_send(socket, common_pb2.LOGIN, response)
        print('washer:{} not found.'.format(phone))
        return
    elif washer['password'] != password:
        response.error_code = common_pb2.ERROR_PASSWORD_INVALID
        helper.client_send(socket, common_pb2.LOGIN, response)
        print('password invalid.')
        return
    print('{}, login success'.format(phone))
    filter = {"washer_phone": phone, "statu": common_pb2.DISTRIBUTED}
    orders = Order.find(filter).count()
    _washer = {
        "id": str(washer['_id']),
        "phone": phone, 
        "nick": washer['nick'],
        "level": washer['level'],
        "avatar": washer['avatar'],
        "type": washer['type'], 
        "orders": orders,
        "open": washer['open'],
        "socket": socket
    }
    Washer.add_online_washer(socket, _washer)
    response.washer.id          = str(washer['_id'])
    response.washer.phone       = washer['phone']
    response.washer.nick        = washer['nick']
    response.washer.avatar      = washer['avatar']
    response.washer.level       = washer['level']
    response.washer.reg_time    = washer['reg_time']
    response.washer.status      = washer['status']
    response.washer.open        = washer['open']
    response.washer.type        = washer['type']
    response.washer.secret      = _make_secret(phone, uuid)
    response.error_code         = common_pb2.SUCCESS
    helper.client_send(socket, common_pb2.LOGIN, response)
    filter = {"phone":phone}
    update = {"$set": {"last_login":int(time.time())}}
    Washer.update_one(filter, update)

#断线重连
def _reconnect(socket, phone, uuid, signature, city_code, longitude, latitude):
    response = washer_pb2.Login_Response()

    result = verify_signature(phone, uuid, signature)

    if not result:
        response.error_code = common_pb2.ERROR_BADREQUEST
        helper.client_send(socket, common_pb2.LOGIN, response)
        return

    filter = {"phone":phone}
    washer = Washer.find_one(filter)
    if washer is None: #找不到商家
        print('washer not found.')
        response.error_code = common_pb2.ERROR_WASHER_NOT_FOUND
        helper.client_send(socket, common_pb2.LOGIN, response)
        return
    
    _washer['socket'] = socket
    _washer['phone']  = washer['phone']
    Washer.add_online_washer(socket, _washer)

    response.id     = str(washer['_id'])
    response.nick   = washer['nick']
    response.phone  = washer['phone']
    response.avatar = washer['avatar']
    response.level  = washer['level']
    response.status = washer['status']
    response.secret = result['secret']
    helper.client_send(socket, common_pb2.LOGIN, response)

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
        response.error_code = common_pb2.ERROR_PASSWORD_NOT_EQUAL
        helper.client_send(socket, common_pb2.REGISTER, response)
        print('password not equal')
        return
    elif not helper.verify_phone(phone):
        response.error_code = common_pb2.ERROR_PHONE_INVALID
        helper.client_send(socket, common_pb2.REGISTER, response)
        print('phone invalid')
        return

    now = int(time.time())

    filter = {"phone": phone}
    washer = Washer.find_one(filter)
    washer_mix = Washer_Mix.find_one(filter)

    if washer is not None:
        print('washer:{} exist.'.format(phone))
        response.error_code = common_pb2.ERROR_WASHER_EXIST
        helper.client_send(socket, common_pb2.REGISTER, response)
        return
    elif washer_mix is None or washer_mix['authcode'] != authcode:
        print('authcode:{} invalid'.format(authcode))
        response.error_code = common_pb2.ERROR_AUTHCODE_INVALID
        helper.client_send(socket, common_pb2.REGISTER, response)
        return
    elif washer_mix['expired'] < now:
        print('autchode expired.')
        response.error_code = common_pb2.ERROR_AUTHCODE_EXPIRED
        helper.client_send(socket, common_pb2.REGISTER, response)
        return

    md5 = hashlib.md5()
    md5.update(password.encode())
    password = md5.hexdigest()

    doc = {
        "phone": phone,
        "nick": nick,
        "password": password,
        "avatar": avatar,
        "status": 0,
        "reg_time": now,
        "last_login": 0,
        "level": common.WASHER_INIT_LEVEL,
        "address": "",
        "longitude": 0.0,
        "latitude": 0.0,
        "type": common_pb2.PERSONAL, #用户类型
        "open": 0 #是否营业
    }

    try:
        result = Washer.insert_one(doc)
        response.washer.id     = str(result.inserted_id)
        response.washer.phone  = phone
        response.washer.nick   = nick
        response.washer.level  = common.WASHER_INIT_LEVEL
        response.washer.status = 0
        response.washer.avatar = avatar
        response.washer.type   = common_pb2.PERSONAL
        response.error_code = common_pb2.SUCCESS
        helper.client_send(socket, common_pb2.REGISTER, response)
        print('register success')
    except DuplicateKeyError:
        response.error_code = common_pb2.ERROR_WASHER_EXIST
        helper.client_send(socket, common_pb2.REGISTER, response)
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
        response.error_code = common_pb2.ERROR_PHONE_INVALID
        helper.client_send(socket, common_pb2.REQUEST_AUTHCODE, response)
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
    
    print('request authcode success,authcode:{}'.format(authcode))
    authcode = authcode or washer_mix['authcode']
    response.authcode = authcode
    response.error_code = common_pb2.SUCCESS
    helper.client_send(socket, common_pb2.REQUEST_AUTHCODE, response)

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
        response.error_code = common_pb2.ERROR_PHONE_INVALID
        helper.client_send(socket, common_pb2.VERIFY_AUTHCODE, response)
        return

    filter = {"phone": phone}
    washer_mix = Washer_Mix.find_one(filter)

    if washer_mix is None or washer_mix['authcode'] != authcode:
        print('authcode invalid')
        response.error_code = common_pb2.ERROR_AUTHCODE_INVALID
        helper.client_send(socket, common_pb2.VERIFY_AUTHCODE, response)
        return
    elif washer_mix['expired'] < int(time.time()):
        print('authcode expired')
        response.error_code = common_pb2.ERROR_AUTHCODE_EXPIRED
        helper.client_send(socket, common_pb2.VERIFY_AUTHCODE, response)
        return

    print('verify authcode success') 
    response.error_code = common_pb2.SUCCESS
    helper.client_send(socket, common_pb2.VERIFY_AUTHCODE, response)

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
    response = washer_pb2.Start_Work_Response() 
    washer   = Washer.get_online_washer(socket)
    if washer is None: #未登录
        print("login first please")
        response.error_code = common_pb2.ERROR_NOT_LOGIN
        helper.client_send(socket, common_pb2.START_WORK, response)
        return
    """
    if washer['open'] == 1: #已经处于开工状态
        response.error_code = common_pb2.ERROR_ALREAD_START
        helper.client_send(socket, common_pb2.START_WORK, response)
        return
    """
    filter = {"phone": washer['phone']}
    update = {"$set":{"open":1}}
    result = Washer.update_one(filter, update)
    """
    if not result.modified_count: #mongo version 2.6开始才有此值
        response.error_code = common_pb2.ERROR_START_WORK_FAILURE
        helper.client_send(socket, common_pb2.START_WORK, response)
        return
    """
    request = washer_pb2.Start_Work_Request()
    request.ParseFromString(data)
    city_code = request.city_code
    longitude = request.longitude
    latitude  = request.latitude
    result = Washer.in_workgroup(city_code, longitude, latitude, washer['phone'], washer['type'])
    if not result: #写入redis失败
        print("(), add to workgroup failure".format(washer['phone']))
        response.error_code = common_pb2.ERROR_START_WORK_FAILURE
        helper.client_send(socket, common_pb2.START_WORK, response)
        return
    washer['open'] = 1
    washer['city_code'] = city_code
    Washer.add_online_washer(socket, washer)
    response.error_code = common_pb2.SUCCESS
    helper.client_send(socket, common_pb2.START_WORK, response)
    print("{}, start work success".format(washer['phone']))

#收工
def stop_work(socket, platform, data):
    response = washer_pb2.Stop_Work_Response()
    washer   = Washer.get_online_washer(socket)
    if washer is None: #未登录
        response.error_code = common_pb2.ERROR_NOT_LOGIN
        helper.client_send(socket, common_pb2.STOP_WORK, response)
        return
    filter = {"phone": washer['phone']}
    update = {"$set": {"open": 0}}
    result = Washer.update_one(filter, update)
    if not result.modified_count:
        response.error_code = common_pb2.ERROR_STOP_WORK_FAILURE
        helper.client_send(socket, common_pb2.STOP_WORK, response)
        return
    result = Washer.out_workgroup(washer['city_code'], washer['phone'], washer['type'])
    if not result:
        response.error_code = common_pb2.ERROR_STOP_WORK_FAILURE
        helper.client_send(socket, common_pb2.STOP_WORK, response)
        return
    response.error_code = common_pb2.SUCCESS
    helper.client_send(socket, common_pb2.STOP_WORK, response)

#更新地理位置
def fresh_location(socket, platform, data):
    response = washer_pb2.Fresh_Location_Response()
    washer = Washer.get_online_washer(socket)
    if washer is None: #未登录
        response.error_code = common_pb2.ERROR_NOT_LOGIN
        helper.client_send(socket, common_pb2.FRESH_LOCATION, response)
        return
    
    request = washer_pb2.Fresh_Location_Request()
    request.ParseFromString(data)
    
    if not washer['open']: #没开工的不允许更新工作组中的地理位置
        response.error_code = common_pb2.ERROR_NOT_START_WORK
        helper.client_send(socket, common_pb2.FRESH_LOCATION, response)
    else:
        washer['city_code'] = request.city_code
        Washer.add_online_washer(socket, washer)
        return

    if washer['orders'] >= common.MAX_ORDERS: #超过所允许接单数
        response.error_code = common_pb2.ERROR_OUT_MAX_ORDERS
        helper.client_send(socket, common_pb2.FRESH_LOCATION, response)
        return

    city_code = request.city_code
    longitude = request.longitude
    latitude  = request.latitude
    result = Washer.in_workgroup(city_code, longitude, latitude, washer['phone'], washer['type'])
    if not result:
        response.error_code = common_pb2.ERROR_FRESH_LOCATION_FAILURE
        helper.client_send(socket, common_pb2.FRESH_LOCATION, response)
        return
    response.error_code = common_pb2.SUCCESS
    helper.client_send(socket, common_pb2.FRESH_LOCATION, response)

#登出
def logout(socket, platform, data):
    response = washer_pb2.Logout_Response()
    washer = Washer.get_online_washer(socket)
    if washer['open']:
        filter = {"phone": washer['phone']}
        update = {"$set":{"open": 0}}
        Washer.update_one(filter, update)
        Washer.out_workgroup(washer['city_code'], washer['phone'], washer['type'])
        Washer.remove_online_washer(socket)
    response.error_code = common_pb2.SUCCESS
    helper.client_send(socket, common_pb2.LOGOUT, response)
    socket.close() 

#生成令牌
def _make_secret(phone, uuid):
    now = time.time()

    elements = [str(now)]
    elements.append(common.APP_KEY)
    elements.append(uuid)
    elements.append(helper.make_rand(6))
    elements.append(phone)
    
    secret = ''.join(elements)
    
    md5 = hashlib.md5()
    md5.update(secret.encode())
    secret = md5.hexdigest()
    filter = {"phone": phone}
    update = {"$set":{"secret":secret}}
    Washer.update_one(filter, update)
    return secret
