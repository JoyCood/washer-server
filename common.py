from pymongo import MongoClient

WASHER_BIND_HOST = ''
WASHER_BIND_PORT = 8888
WASHER_HEADER_LENGTH = 20

APP_SERVER_HOST = '127.0.0.1'
APP_SERVER_PORT = 7777

SYSTEM  = 0
IOS     = 1
ANDROID = 2

AUTHCODE_MIN = 1000
AUTHCODE_MAX = 9999
AUTHCODE_EXPIRED_TIME = 600

MOD = {
    '11': 'member',
    '12': 'order',
    '13': 'washer',
    '14': 'payment'
}

mongo = MongoClient().hotelwasher
