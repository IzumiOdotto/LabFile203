# -*- coding = uft-8 -*-
# @File     : S03_SlugSensor.py
# @Time     : 2022/11/13 11:54  
# @Author   : Samuel HONG
# @Description : Try to compose a Class file of slug flow sensor
# @Version  :

from pyfirmata import Arduino, util
import time


class SlugSensor(object):
    def __init__(self, port_num):
        self.port_num = port_num

