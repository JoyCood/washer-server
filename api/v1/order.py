#!/usr/bin/python 
# -*- coding: utf-8 -*-

import sys
import time

import common_1_pb2 as common_pb2
import order_1_pb2 as order_pb2
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
        print("protocol:{} handler is not found".format(protocol))
        return
    fun = getattr(sys.modules[__name__], handler)
    fun(socket, platform, data)

def order_check(socket, platform, data):
    washer = Washer.get_online_washer(socket)
    if washer is None:
        return

    filter = {
        "washer_phone": washer['phone'],
        "status": common_pb2.DISTRIBUTED
    }
    sort   = [("allocate_time", 1)] 
    cursor = Order.find(filter).sort(sort)

#已送回,更新完成状态
def finish_order(socket, platform, data):
    request = order_pb2.Finish_Order_Request()
    request.ParseFromString(data)
    order_id = request.order_id.strip()

    response = order_pb2.Finish_Order_Response()
    washer = Washer.get_online_washer(socket)
    if washer is None:
        print("error-> v1.order.finish_order: not logined washer")
        response.error_code = common_pb2.ERROR_NOT_LOGIN
        helper.client_send(socket, common_pb2.FINISH_ORDER, response)
        return
    filter = {
        "_id": ObjectId(order_id), 
        "status": common_pb2.DISTRIBUTED, 
        "washer_phone": washer['phone']
    }
    order = Order.find_one(filter)
    now = int(time.time())
    update = {
        "$set": {
            "status": common_pb2.FINISH,
            "finish_time": now
        }
    }
    result = Order.update_one(filter, update)
    if not result.modified_count:
        print("error-> v1.order.finish_order: modified_count not greate than zero")
        response.error_code = common_pb2.ERROR_ORDER_FINISH_FAILURE
        helper.client_send(socket, platform, common_pb2.FINISH_ORDER, response)
        return

    response.error_code = common_pb2.SUCCESS
    helper.client_send(socket, common_pb2.FINISH_ORDER, response)
    print("success-> v1.order.finish_order success")

    system_request = system_order_pb2.Finish_Order_Request()
    system_request.customer_phone = order['customer_phone']
    helper.system_send(system_common_pb2.FINISH_ORDER, system_request)

#历史订单
def history_order(socket, platform, data):
    response = order_pb2.History_Order_Response()
    
    washer = Washer.get_online_washer(socket)
    if washer is None:
        response.error_code = order_pb2.ERROR_NOT_LOGIN
        helper.client_send(socket, common_pb2.HISTORY_ORDER, response)
        return

    request = order_pb2.History_Order_Request()
    request.ParseFromString(data)
    filter = {
        "washer_phone": washer['phone']         
    }
    if request.offset:
        filter.udpate({"order_time": {"$lt": request.offset}})
    sort = [("order_time", -1)]
    limit = request.limit or 10
    cursor = Order.find(filter, sort=sort, limit=limit)
    for item in cursor:
        order = response.order.add()
        order.id = str(item['_id'])
        order.status = item['status']
        order.quantity = item['quantity']
        order.order_time = item['order_time']
        order.washer_nick = item['washer_nick']
        order.washer_avatar = item['washer_avatar']
    helper.client_send(socket, common_pb2.HISTORY_ORDER, response)

#取消订单
def cancel_order(socket, platform, data):
    response = order_pb2.Cancel_Order_Response()
    washer = Washer.get_online_washer(socket)
    if washer is None:
        response.error_code = common_pb2.ERROR_NOT_LOGIN
        helper.client_send(socket, common_pb2.CANCEL_ORDER, response)
        return

    request = order_pb2.Cancel_Order_Request()
    request.ParseFromString(data)
    order_id = request.order_id.strip()
    now = int(time.time())

    filter = {
        "_id": ObjectId(order_id),
        "washer_phone": washer['phone'],
        "status": common_pb2.DISTRIBUTED
    }
    update = {
        "$set": {
            "status": common_pb2.CANCELED, 
            "cancel_time": now,
            "cancel_by": 2
        }
    }
    result = Order.update_one(filter, update)
    if not result.modified_count:
        response.error_code = common_pb2.ERROR_CANCEL_ORDER_FAILURE
        helper.client_send(socket, common_pb2.CANCEL_ORDER, response)
        return
    response.error_code = common_pb2.SUCCESS
    helper.client_send(socket, common_pb2.CANCEL_ORDER, response)

    system_request = system_order_pb2.Cancel_Order_Request()
    system_request.customer_phone = order['customer_phone']
    system_request.order_id = order_id
    helper.system_send(system_common_pb2.CANCEL_ORDER, system_request)

def order_feedback(socket, platform, data):
    pass



