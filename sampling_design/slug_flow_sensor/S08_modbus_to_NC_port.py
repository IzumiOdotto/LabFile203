# -*- coding = uft-8 -*-
# @File     : S08_modbus_to_NC_port.py
# @Time     : 2022/11/24 9:14  
# @Author   : Samuel HONG
# @Description : Try to connect sensor conductivity with board.
# @Version  :

from pyfirmata import Arduino, util
import time

port = 'COM8'
board = Arduino(port)
it = util.Iterator(board)
it.start()

board.analog[0].enable_reporting()

li = []

while True:
    li.append(board.analog[0].read())
    print(li[-1:])
