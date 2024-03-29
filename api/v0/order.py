#!/usr/bin/python 
# -*- coding: utf-8 -*-

import sys
import time

import system_common_pb2
import system_order_pb2
from .protocol import route
from helper import helper
from model.order.order import Order
from model.washer.washer import Washer

from bson.objectid import ObjectId

def handle(socket, protocol, platform, data):
    handler = route.get(protocol)
    if handler is None:
        print("protocol:{} handler is not found".format(protocol) )
        return
    fun = getattr(sys.modules[__name__], handler)
    fun(socket, platform, data)

#用户下单，分配订单
def allocate_order(socket, platform, data):
    request = system_order_pb2.Allocate_Order_Request()
    request.ParseFromString(data)

    order_id           = request.order_id
    washer_type        = request.washer_type
    quantity           = request.quantity
    customer_id        = request.customer.id
    customer_phone     = request.customer.phone
    customer_nick      = request.customer.nick
    customer_level     = request.customer.level
    customer_avatar    = request.customer.avatar
    customer_city_code = request.customer.city_code
    customer_longitude = request.customer.longitude
    customer_latitude  = request.customer.latitude
    
    print("customer_city_code:{}, customer_longitude:{}, customer_latitude:{}, washer_type:{}, quantity:{}".format(customer_city_code, customer_longitude, customer_latitude, washer_type, quantity))
    washer = Washer.allocate_washer(customer_city_code, customer_longitude, customer_latitude, washer_type)

    response = system_order_pb2.Allocate_Order_Response()
    if washer is None:
        response.error_code = system_common_pb2.ERROR_WASHER_NOT_FOUND
        helper.system_response(socket, system_common_pb2.ALLOCATE_ORDER, response)
        return

    filter = {"_id": ObjectId(order_id) }
    update = {
        "$set":{
            "washer_id": washer['id'],
            "washer_phone": washer['phone'], 
            "washer_nick": washer['nick'],
            "washer_avatar": washer['avatar'],
            "status": system_common_pb2.DISTRIBUTED,
            "allocate_time": int(time.time())
            }
    }
    result = Order.update_one(filter, update)
     
    if not result.modified_count:
        response.error_code = system_common_pb2.ERROR_ALLOCATE_WASHER_FAILURE
        helper.system_response(socket, system_common_pb2.ALLOCATE_ORDER, response)
        return
    
    response.id = washer['id']
    response.phone = washer['phone']
    response.nick  = washer['nick']
    response.avatar = washer['avatar']
    response.level  = washer['level']
    response.longitude = washer['longitude']
    response.latitude  = washer['latitude']
    response.error_code = system_common_pb2.SUCCESS
    
    helper.system_response(socket, system_common_pb2.ALLOCATE_ORDER, response)

    #通知商家有人下单
    response = system_order_pb2.Allocate_Order_Push()
    response.customer.id = customer_id
    response.customer.phone = customer_phone
    response.customer.nick  = customer_nick
    response.customer.avatar = customer_avatar
    response.customer.level = customer_level
    response.customer.longitude = customer_longitude
    response.customer.latitude = customer_latitude
    response.order_id = order_id
    response.quantity = quantity
    print("response.quantity:{}".format(quantity))
    response.error_code = system_common_pb2.SUCCESS
    helper.client_send(washer['socket'], system_common_pb2.WASHER_ALLOCATE_ORDER, response)

#用户取消订单
def cancel_order(socket, platform, data):
    pass
    request = system_order_pb2.Cancel_Order_Request()
    request.ParseFromString(data)
