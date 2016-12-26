#!/usr/bin/python 
# -*- coding: utf-8 -*-

import sys
import time
import common

from protocol.v0 import system_washer_pb2
from .protocol import route
from helper import helper

def handle(socket, protocol, platform, data):
    handler = route.get(protocol)
    if handler is None:
        print("protocol:{} handler is not found".format(protocol))
        return
    fun = getattr(sys.modules[__name__], handler)
    fun(socket, platform, data)

def allocate_washer(socket, platform, data):
    request = system_washer_pb2.Allocate_Washer_Request()    
    request.ParseFromString(data)

    order_type = request.order_type
    city_code  = request.city_code
    longitude  = request.longitude
    latitude   = request.latitude

    response = system_washer_pb2.Allocate_Washer_Response()

    response.washer.id    = '123456'
    response.washer.phone = '+8613533332421'
    response.washer.nick  = 'iwasher'
    response.error_code   = system_washer_pb2.SUCCESS

    helper.system_response(socket, system_washer_pb2.ALLOCATE_WASHER, response)
