# -*- coding = uft-8 -*-
# @File     : 00_03_test_while_loop.py
# @Time     : 2022/11/13 15:51  
# @Author   : Samuel HONG
# @Description : Try to care and test the while loop.
# @Version  :

import time
import numpy as np
import statistics
from pyfirmata import Arduino, util

board = Arduino("COM8")

it = util.Iterator(board)
it.start()

board.digital[13].write(1)
board.analog[0].enable_reporting()
board.analog[1].enable_reporting()
board.analog[2].enable_reporting()

sensorA_li = []

slug_flow_past_A = False
while slug_flow_past_A == False:
    sensorA_li.append(board.analog[2].read())
    if len(sensorA_li) > 20:
        var_sensorA_li = np.var(sensorA_li[-10:])
        if var_sensorA_li > 1e-4:
            slug_flow_past_A = True
        # print(var_sensorA_li)
    time.sleep(0.002)
    print(sensorA_li[-10:])
    continue
print("FLOW PAST THE LOOP ALREADY!!")
