#!/usr/bin/python 
# -*- coding: utf-8 -*-

import sys
import time
import common

from protocol.v0 import system_order_pb2
from .protocol import route
from helper import helper
from model.order.order import Order

from bson.objectid import ObjectId

def handle(socket, protocol, platform, data):
    handler = route.get(protocol)
    if handler is None:
        print("protocol:{} handler is not found".format(protocol) )
        return
    fun = getattr(sys.modules[__name__], handler)
    fun(socket, platform, data)

#分配订单
def allocate_order(socket, platform, data):
    request = system_order_pb2.Allocate_Order_Request()
    request.ParseFromString(data)

    order_id           = request.order_id
    order_type         = request.order_type
    quantity           = request.quantity
    customer_id        = request.customer.id
    customer_phone     = request.customer.phone
    customer_nick      = request.customer.nick
    customer_level     = request.customer.level
    customer_avatar    = request.customer.avatar
    customer_city_code = request.customer.city_code
    customer_longitude = request.customer.longitude
    customer_latitude  = request.customer.latitude

    washer = {
        "id": '1234567890',
        "phone": '+8613533332421',
        "nick": 'iwasher',
        "avatar": 'http://www.image.com/1.jpg',
        "level": 5.0,
        "longitude": 120.025806,
        "latitude" : 30.246185
    }

    filter = {"_id":ObjectId(order_id)}
    update = {"$set":{"washer_phone":washer['phone'], "washer_nick":washer['nick']}}
    Order.update_one(filter, update)
    
    response = system_order_pb2.Allocate_Order_Response()
    
    response.id = washer['id']
    response.phone = washer['phone']
    response.nick  = washer['nick']
    response.avatar = washer['avatar']
    response.level  = washer['level']
    response.longitude = washer['longitude']
    response.latitude  = washer['latitude']
    response.error_code = system_order_pb2.SUCCESS
    
    helper.system_response(socket, system_order_pb2.ALLOCATE_ORDER, response)

#取消订单
def cancel_order(socket, socket, data)
    pass
