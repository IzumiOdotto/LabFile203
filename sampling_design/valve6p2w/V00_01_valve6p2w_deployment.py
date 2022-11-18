# -*- coding = uft-8 -*-
# @File     : V00_01_valve6p2w_deployment.py
# @Time     : 2022/11/6 18:09  
# @Author   : Samuel HONG
# @Description : Sampling mode & Oscilating mode
# @Version  :

import logging
from pymodbus.client import ModbusSerialClient as ModbusClient


class ValveA(object):
    # normally it is COM4
    def __init__(self, port_num):
        self.port_num = port_num
        self.port_name = 'COM' + '%s' % self.port_num
        # print(self.port_name)
        self.client = ModbusClient(port=self.port_name, baudrate=9600, method='RTU', stopbits=1, bytesize=8,
                                   timeout=0.01)
        self.client.connect()

    # mode1, 1-2, oscillating
    # mode2, 1-6, sampling

    def switch_loop_to_sample(self):
        self.client.write_coil(1, True, slave=17)

    def switch_loop_to_flowstream(self):
        self.client.write_coil(2, True, slave=17)

    def reset_valveA(self):
        self.client.write_coil(0, True, slave=17)


if __name__ == "__main__":
    my_valve = ValveA('4')
    # my_valve.switch_loop_to_mainpath()
    my_valve.switch_loop_to_sample()