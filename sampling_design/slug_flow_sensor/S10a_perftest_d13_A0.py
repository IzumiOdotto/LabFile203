# -*- coding = uft-8 -*-
# @File     : S10a_perftest_d13_A0.py
# @Time     : 2023/1/7 22:46  
# @Author   : Samuel HONG
# @Description : This script is for testing whether IO data fluctuates with the blinking LED output of digitalPin13
# @Version  :


from pyfirmata import Arduino, util
import threading
import time
import numpy as np
import tkinter as tk


# We'll use threading for the blinking

def blink():
    while True:
        board.digital[13].write(1)
        time.sleep(1)
        board.digital[13].write(0)
        time.sleep(1)


# why should the deritive class come into realization?
class myThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        blink()


board = Arduino("COM8")
it = util.Iterator(board)
it.start()

board.digital[13].write(1)
board.analog[0].enable_reporting()

thread_blink = myThread()
thread_blink.start()

sensor_li = []
last_10_data_li = []

while True:
    sensor_li.append(board.analog[0].read())
    print(board.analog[0].read())

    # signal_standard_arr = np.array(sensor_li[-10:])
    # if len(sensor_li) > 20:
    #     var_sensor_li = np.var(sensor_li[-10:])
    # time.sleep(0.002)
    #
    # # if var_sensor_li > 1e-4, send a window and quit.
    # # if var_sensor_li exists.
    # if 'var_sensor_li' in locals():
    #     if var_sensor_li > 0.0001:
    #         break
