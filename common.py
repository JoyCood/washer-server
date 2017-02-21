import os
import sys
from pymongo import MongoClient
from lib.washer import Washer
import redis

WASHER_BIND_HOST = ''
WASHER_BIND_PORT = 8888
WASHER_HEADER_LENGTH = 20

APP_SERVER_HOST = '127.0.0.1'
APP_SERVER_PORT = 7777

SYSTEM  = 0
IOS     = 1
ANDROID = 2

APP_KEY = 'abc'

AUTHCODE_MIN = 1000
AUTHCODE_MAX = 9999
AUTHCODE_EXPIRED_TIME = 600

WASHER_INIT_LEVEL = 1
MAX_ORDERS = 1

WECHAT_PAY = {
        "appkey": "f9c62cccbdc99de463304d89358788f9",
        "appid": 'wxd32d25b2a43c0f93',
        "mchid": '1312998901',
        'notify_url': 'https://developer.7swim.com'
}

ALIPAY = {
        
}

MOD = {
    '11': 'member',
    '12': 'order',
    '13': 'washer',
    '14': 'payment',

    '80': 'washer', #80开始为内部系统协议
    '81': 'order',
}

redis = redis.StrictRedis()
mongo = MongoClient().hotelwasher
AppServer = Washer.IWasher(APP_SERVER_HOST, APP_SERVER_PORT)
SERVER_PATH = os.path.dirname(__file__)
sys.path.append(SERVER_PATH + "/protocol/v0")
