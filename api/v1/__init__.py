#!/usr/bin/python 
# -*- coding:utf-8 -*-
import os
import sys
import common
start = len(common.SERVER_PATH) + 5 
v = os.path.dirname(os.path.realpath(__file__))[start:]
protocol = common.SERVER_PATH + "/protocol/" + v
sys.path.append(protocol)
