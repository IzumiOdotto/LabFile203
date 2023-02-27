# -*- coding = uft-8 -*-
# @File     : PG00_try_modbus.py
# @Time     : 2022/11/24 11:38  
# @Author   : Samuel HONG
# @Description : 
# @Version  :


# pressure gauge
import time

from pymodbus.client import ModbusSerialClient as ModbusClient

port = 'COM4'
client = ModbusClient(port=port, baudrate=9600, method='RTU', stopbits=1, bytesize=8, timeout=1, parity='N')
client.connect()

while True:
    val = client.read_holding_registers(address=0, count=1, slave=1)
    print(val.registers)
