# -*- coding = uft-8 -*-
# @File     : S04_try_modebus.py
# @Time     : 2022/11/16 15:30  
# @Author   : Samuel HONG
# @Description : Try 485 sensor modbus
# @Version  :

import time

from pymodbus.client import ModbusSerialClient as ModbusClient

port = 'COM9'
client = ModbusClient(port=port, baudrate=9600, method='RTU', stopbits=1, bytesize=8, timeout=1, parity='N')
client.connect()

while True:
    val = client.read_holding_registers(address=1, count=2, slave=1)
    print(val.encode())

