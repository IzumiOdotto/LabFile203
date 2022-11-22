# -*- coding = uft-8 -*-
# @File     : S05b_test_sensor_with_mat.py
# @Time     : 2022/11/21 10:39  
# @Author   : Samuel HONG
# @Description : 
# @Version  :


from pyfirmata import Arduino, util
import time
import numpy as np
import tkinter as tk

board = Arduino("COM8")

it = util.Iterator(board)
it.start()

board.digital[13].write(1)
board.analog[1].enable_reporting()

sensor_li = []
last_10_data_li = []

flowpast = False
while not flowpast:
    sensor_li.append(board.analog[1].read())
    print(board.analog[1].read())
    signal_standard_arr = np.array(sensor_li[-10:])
    if len(sensor_li) > 20:
        var_sensor_li = np.var(sensor_li[-10:])
        if var_sensor_li > 1e-4:
            print("FLOW PAST B!")
            flowpast = True
    time.sleep(0.025)
