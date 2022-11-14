# -*- coding = uft-8 -*-
# @File     : S03_SlugSensor.py
# @Time     : 2022/11/13 11:54  
# @Author   : Samuel HONG
# @Description : Try to compose a Class file of slug flow sensor
# @Version  :

from pyfirmata import Arduino, util
import time


class ArduinoSensorBoard(object):
    def __init__(self, port_num, light_on=True):
        # By doing this, we can get over with the initialization of Arduino.
        self.port_num = port_num
        # self.board = Arduino("COM" + "%d", self.port_num)
        self.board = Arduino("COM8")

        self.it = util.Iterator(self.board)
        self.it.start()

        if light_on == True:
            self.board.digital[13].write(1)


class SlugSensor(ArduinoSensorBoard):
    def __init__(self, analog_num, port_num):
        super().__init__(port_num)
        self.analog_num = analog_num
        self.board.analog[analog_num].enable_reporting()

    def data_collect(self):
        # while self.data_collect.continue
        self.sensor_li = []
        self.sensor_li.append(self.board.analog[self.analog_num].read())
        print(self.sensor_li[self.analog_num])
        time.sleep(0.002)


if __name__ == '__main__':
    # myArduino = ArduinoSensorBoard(port_num=8, light_on=True)

    # myArduino = ArduinoSensorBoard(port_num=8,light_on=True)
    sensorA = SlugSensor(0,'COM8')
    sensorA.data_collect()