#!/usr/bin/python 
# -*- coding:utf-8 -*-
import os
import sys
filepath = os.path.dirname(os.path.realpath(__file__))[0:-6] + "protocol/v2/"
sys.path.append(filepath)
print(sys.path)
