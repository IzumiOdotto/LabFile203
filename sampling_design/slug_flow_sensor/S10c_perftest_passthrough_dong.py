# -*- coding = uft-8 -*-
# @File     : S10c_perftest_passthrough_dong.py
# @Time     : 2023/1/8 22:10  
# @Author   : Samuel HONG
# @Description : 
# @Version  :


import winsound

from pyfirmata import Arduino, util
import time
import numpy as np
import tkinter as tk

# We'll use threading for the blinking


board = Arduino("COM8")
it = util.Iterator(board)
it.start()

board.digital[13].write(1)
board.analog[0].enable_reporting()

sensor_li = []
last_10_data_li = []

freq = 2500
dur = 50

# Beep only once and break.
while True:
    sensor_li.append(board.analog[0].read())
    print(board.analog[0].read())

    signal_standard_arr = np.array(sensor_li[-10:])
    if len(sensor_li) > 20:
        var_sensor_li = np.var(sensor_li[-10:])
    time.sleep(0.002)

    # if var_sensor_li > 1e-4, send a window and quit.
    # if var_sensor_li exists.
    if 'var_sensor_li' in locals():
        if var_sensor_li > 0.0001:
            break

# make 'gong' sound.(Beep)
winsound.Beep(freq, dur)
time.sleep(1)