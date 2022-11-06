# -*- coding = uft-8 -*-
# @File     : try_timeout.py
# @Time     : 2022/11/6 17:06  
# @Author   : Samuel HONG
# @Description : try some timeout out of work.
# @Version  :

import logging
from pymodbus.client import ModbusSerialClient as ModbusClient

# mode1, 1-2, oscilating
# mode2, 1-6, sampling

port = 'COM4'
client = ModbusClient(port=port, baudrate=9600, method='RTU', stopbits=1, bytesize=8, timeout=0.01)
client.connect()
client.write_coil(1, True, slave=17)
