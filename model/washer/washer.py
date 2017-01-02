#!/usr/bin/python 
# -*8 coding: utf-8 -*-

from common import (mongo, redis, MAX_ORDERS)
import random

class Washer(object):
    _online_washer = dict()
    _washer_map   = dict()

    @staticmethod
    def aggregate(pipline, **kwargs):
        return mongo.washer.aggregate(pipline, **args)

    @staticmethod
    def insert_one(doc, bypass_document_validation=False):
        return mongo.washer.insert_one(doc, bypass_document_validation)

    @staticmethod
    def find_one(filter, *args, **kwargs):
        return mongo.washer.find_one(filter, *args, **kwargs)

    @staticmethod
    def update_one(filter, update, upsert=False, bypass_document_validation=False):
        return mongo.washer.update_one(filter, update, upsert, bypass_document_validation)

    @classmethod
    def add_online_washer(cls, socket, data):
        cls._online_washer[socket] = data 
        cls._washer_map[data['phone']] = socket

    @classmethod
    def get_online_washer(cls, socket):
        return cls._online_washer.get(socket)

    @classmethod
    def remove_online_washer(cls, socket):
        try:
            washer = cls.online_washer[socket]
            del _washer_map[washer['phone']]
            del _online_washer[socket]
        except (TypeError, KeyError):
            pass
        return True

    @classmethod
    def in_workgroup(cls, city_code, longitude, latitude, phone, washer_type):
        key = str(city_code) + '-' + str(washer_type)
        print("in_workgroup key:{}".format(key))
        exploder = ' '
        cmd = ['GEOADD']
        cmd.append(key)
        cmd.append(str(longitude))
        cmd.append(str(latitude))
        cmd.append(phone)
        cmd = exploder.join(cmd)
        
        try:
            redis.execute_command(cmd)
            return True
        except ResponseError as e:
            return False
    
    @classmethod
    def out_workgroup(cls, city_code, phone, washer_type):
        key = str(city_code) + '-' + str(washer_type)
        try:
            redis.zrem(key, phone)
            return True
        except ResponseError as e:
            return False

    @classmethod
    def allocate_washer(cls, city_code, longitude, latitude, washer_type):
        key = str(city_code) + '-' + str(washer_type);
        exploder = ' '
        cmd = ['GEORADIUS']
        cmd.append(key)
        cmd.append(str(longitude))
        cmd.append(str(latitude))
        cmd.append('3 km WITHDIST WITHCOORD')
        cmd = exploder.join(cmd)

        washers = redis.execute_command(cmd)

        if washers is None:
            print("can not find any avalid washer in redis")
            return 

        size = len(washers)
        if not size:
            print("the washers length is zero")
            return

        index     = random.randint(0, size-1)
        _washer   = washers[index]
        phone     = _washer[0].decode('utf-8')
        distance  = _washer[1]
        longitude = float(_washer[2][0])
        latitude  = float(_washer[2][1])
        _socket   = cls._washer_map[phone]
        washer = cls.get_online_washer(_socket)
        if washer is None:
            print("get one not login washer\n")
            return
        _washer = {
            "id": washer['id'],
            "phone": washer['phone'],
            "nick" : washer['nick'],
            "avatar": washer['avatar'],
            "level": washer['level'],
            "longitude": longitude,
            "latitude": latitude,
            "distance": distance,
            "socket": washer['socket']
        }
        #是否达到允许接单数，达到则从服务组中剃除，不再给此商家分配订单
        if (washer['orders'] + 1) >= MAX_ORDERS:
            cls.out_workgroup(city_code, phone, washer['type'])
        washer['orders'] += 1
        cls.add_online_washer(washer['socket'], washer)

        return _washer

    @classmethod
    def cleanup_state(cls, socket):
        pass
    
class Mix(object):
    @staticmethod
    def insert_one(doc, bypass_document_validation=False):
        return mongo.washer_mix.insert_one(doc, bypass_document_validation)
    
    @staticmethod
    def find_one(filter, *args, **kwargs):
        return mongo.washer_mix.find_one(filter, *args, **kwargs)

    @staticmethod
    def update_one(filter, update, upsert=False, bypass_document_validation=False):
        return mongo.washer_mix.update_one(filter, update, upsert, bypass_document_validation)

