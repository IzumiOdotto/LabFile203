# -*- coding = uft-8 -*-
# @File     : S09_try_black_shell.py
# @Time     : 2022/12/16 15:18  
# @Author   : Samuel HONG
# @Description : Let's try some blackshell.
# @Version  :

from pyfirmata import Arduino, util
import time
import numpy as np

board = Arduino("COM8")

it=util.Iterator(board)
it.start()

board.digital[12].write(1)
board.analog[0].enable_reporting()

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
