# -*- coding = uft-8 -*-
# @File     : PT02_try_to_call_pump_continuously.py
# @Time     : 2022/11/18 16:06  
# @Author   : Samuel HONG
# @Description : Try to call the pump continuously
# @Version  :
import time

from CHEMYX_multistep.core import connect

baud = 38400
conn = connect.Connection(port='COM7', baudrate=baud, x=0, mode=0)

conn.openConnection()

units = 'mL/min'  # OPTIONS: 'mL/min','mL/hr','μL/min','μL/hr'
diameter = 19.17
volume = -10
rate = 2
delay = 0

conn.setUnits(units)
conn.setDiameter(diameter)
conn.setVolume(volume)
conn.setRate(rate)
conn.setDelay(delay)

conn.startPump()

volume = 10
rate = -3
conn.setVolume(volume)
conn.setRate(rate)

time.sleep(2)

conn.startPump()

volume = 20
rate = 3
conn.setVolume(volume)
conn.setRate(rate)

time.sleep(5)

conn.startPump()