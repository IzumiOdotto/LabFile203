# -*- coding = uft-8 -*-
# @File     : S02_read_multiple_analogue.py
# @Time     : 2022/11/12 18:49  
# @Author   : Samuel HONG
# @Description : Let's see if there is a way to read multiple analogue.
# @Version  :

from pyfirmata import Arduino, util
import time
import numpy as np
import tkinter as tk


board = Arduino("COM8")

it = util.Iterator(board)
it.start()

board.digital[13].write(1)
board.analog[0].enable_reporting()
board.analog[1].enable_reporting()
board.analog[2].enable_reporting()

sensor_li = [[], [], []]

while True:
    # for i in range(0, 2):
    i = 2
    sensor_li[i].append(board.analog[i].read())
    print(sensor_li[i])
    time.sleep(0.002)
