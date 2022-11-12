# -*- coding = uft-8 -*-
# @File     : S00_try_to_read_flow_sensor_with_pyfirmata.py
# @Time     : 2022/11/12 14:52  
# @Author   : Samuel HONG
# @Description : Try to read flow sensor with pyFirmata
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

sensor_li = []
last_10_data_li = []

while True:
    sensor_li.append(board.analog[0].read())
    # print(board.analog[0].read())
    signal_standard_arr = np.array(sensor_li[-10:])
    if len(sensor_li) > 20:
        var_sensor_li = np.var(sensor_li[-10:])
    time.sleep(0.002)

    # if var_sensor_li > 1e-4, send a window and quit.
    if var_sensor_li > 0.0001:
        break