#!/usr/bin/python 
# -*- coding: utf-8 -*-

class ServerError(Exception):
    pass

class ConnectionError(ServerError):
    pass

class TimeoutError(ServerError):
    pass
