# -*- coding = uft-8 -*-
# @File     : F04_try_chemios.py
# @Time     : 2023/2/22 9:53  
# @Author   : Samuel HONG
# @Description : 
# @Version  :

import time
from chemios.pumps import HarvardApparatus
import serial

# This Harvard Phd Ultra stands for COM port 5.
ser = serial.Serial(port='COM5', baudrate=38400)
harvard_pump = HarvardApparatus(model='Phd-Ultra', ser=ser)
harvard_pump.set_syringe(manufacturer='hamilton', volume=10, inner_diameter=14)

rate = {'value': 100, 'units': 'uL/min'}
harvard_pump.set_rate(rate=rate, direction='INF')

harvard_pump.run()
time.sleep(20)
harvard_pump.stop()
