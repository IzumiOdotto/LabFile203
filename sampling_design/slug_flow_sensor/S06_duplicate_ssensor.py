# -*- coding = uft-8 -*-
# @File     : S06_duplicate_ssensor.py
# @Time     : 2022/11/22 22:03  
# @Author   : Samuel HONG
# @Description : Try to establish a class script of Sensor Board. Sketch would also be okay.
# @Version  :

# Requis:
# Establish a port\board initiate scheme.

from pyfirmata import Arduino, util
import time
import numpy as np
from threading import Thread


# Very coarse.
# Please consider what would happen if there appears the demand of two sensors.
# It seems that board should be a variable to be input to this class?
class FlowPastSensor(object):
    def __init__(self, arduino_board, analog_num):
        self.analog_num = analog_num
        self.board = arduino_board

        self.it = util.Iterator(self.board)
        self.it.start()

        self.li = []
        self.board.anlog[self.analog_num].enable_reporting()

        # Would the coming sentence still be working now...
        # self.board.digital[13].write(1)

    def reset(self):
        self.li = []

    def collect(self):
        self.li.append(self.board.anlog[self.analog_num].read())
        time.sleep(0.002)
        return self.li

    def print_data(self):
        print(self.li[-1:])

    def variance(self, num_range, threshold):
        if len(self.li) > 10:
            try:
                if np.var(self.li[-num_range:]) > threshold:
                    return True
            except TypeError:
                pass


if __name__ == "__main__":
    Arduino_port = 'COM8'

    board = Arduino(Arduino_port)
    it = util.Iterator(board)
    it.start()
    board.digital[13].write(1)

    analog_A = 0
    analog_B = 1
    analog_C = 2
    flow_past_sensor_B = FlowPastSensor(board, analog_B)
    flow_past_sensor_B.collect()
    flow_past_sensor_B.variance(10, 1e-4)

    # How to turn an endless while loop into a better Threading? :)
