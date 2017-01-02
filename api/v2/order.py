#!/usr/bin/python 
# -*- coding: utf-8 -*-

import sys
import time

from protocol.v1 import order_pb2
from .protocol import route
from helper import helper
from model.order.order import Order
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
        "status": order_pb2.DISTRIBUTED
    }
    cursor = Order.find(filter).sort([{"allocate_time":1}])
    

#已送回,更新完成状态
def order_finish(socket, platform, data):
    request = order_pb2.Order_Finish_Request()
    request.ParseFromString(data)
    order_id = request.order_id.strip()
    washer = Washer.get_online_washer(socket)
    filter = {
        "_id": ObjectId(order_id), 
        "status": order_pb2.DISTRIBUTED, 
        "washer_phone": washer['phone']
    }
    order = Order.find_one(filter)
    now = int(time.time())
    update = {
        "$set": {
            "status": order_pb2.FINISH,
            "finish_time": now
        }
    }
    result = Order.update_one(filter, update)
    if not result.modified_count:
        response.error_code = order_pb2.ERROR_ORDER_FINISH_FAILURE
        helper.client_send(socket, platform, order_pb2.ORDER_FINISH, response)
        return

    system_request = system_order_pb2.Order_Finish_Request()
    system_request.customer_phone = order['customer_phone']
    helper.system_send(protocol, system_request)

def history_order(socket, platform, data):
    pass

def cancel_order(socket, platform, data):
    pass

def order_feedback(socket, platform, data):
    pass



