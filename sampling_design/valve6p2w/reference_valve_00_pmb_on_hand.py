# -*- coding = uft-8 -*-
# @File     : 00_pmb_on_hand.py
# @Time     : 2022/7/9 16:31  
# @Author   : Samuel HONG
# @Description : Just set my thought to things
# @Version  :

import logging
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

port = 'COM4'
client = ModbusClient(port=port, baudrate=9600, method='RTU', stopbits=1, bytesize=8, timeout=5)
# client = ModbusClient(port=port, baudrate=115200, method='RTU', stopbits=1, bytesize=8)
client.connect()

# para1: output register address
# para2: output value
# para unit: slave address
# client.write_coil(1, True, unit=17)
client.write_coil(2, True, unit=17)
