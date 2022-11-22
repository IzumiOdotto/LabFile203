# -*- coding = uft-8 -*-
# @File     : S03_SlugSensor.py
# @Time     : 2022/11/13 11:54  
# @Author   : Samuel HONG
# @Description : Try to compose a Class file of slug flow sensor
# @Version  :

from pyfirmata import Arduino, util
import time
import numpy as np


class ArduinoSensorBoard(object):
    def __init__(self, port_num, light_on=True):
        # By doing this, we can get over with the initialization of Arduino.
        self.port_num = port_num
        # self.board = Arduino("COM" + "%d", self.port_num)
        self.board = Arduino("COM8")

        self.it = util.Iterator(self.board)
        self.it.start()

        if light_on:
            self.board.digital[13].write(1)


class SlugSensor(object):
    def __init__(self, analog_num, port_num):
        # super().__init__(port_num, light_on=True)
        self.port_num = port_num
        self.board = Arduino("COM8")

        self.it = util.Iterator(self.board)
        self.it.start()

        self.board.digital[13].write(1)
        self.sensor_li = []
        self.analog_num = analog_num
        self.board.analog[analog_num].enable_reporting()

    def reset(self):
        self.sensor_li = []

    def data_collect(self):
        # while self.data_collect.continue
        self.sensor_li.append(self.board.analog[self.analog_num].read())
        # print(self.sensor_li[-1:])
        time.sleep(0.002)
        return self.sensor_li

    def print_data(self):
        print(self.sensor_li[-1:])

    def examine_variance(self):
        if len(self.sensor_li) > 20:
            if np.var(self.sensor_li[-10:]) > 1e-4:
                return True
            else:
                pass
        else:
            pass


if __name__ == '__main__':
    # myArduino = ArduinoSensorBoard(port_num=8, light_on=True)

    # myArduino = ArduinoSensorBoard(port_num=8,light_on=True)
    sensorA = SlugSensor(0, 'COM8')
    sensorA.data_collect()
