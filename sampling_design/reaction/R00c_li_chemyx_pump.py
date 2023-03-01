# -*- coding = uft-8 -*-
# @File     : R00c_li_chemyx_pump.py
# @Time     : 2023/2/27 14:11  
# @Author   : Samuel HONG
# @Description : 
# @Version  :

from exlusive_test_on_pump.CHEMYX_multistep.core import connect

baud = 38400
conn = connect.Connection(port='COM3', baudrate=baud, x=0, mode=0)

conn.openConnection()

units = 'mL/min'  # OPTIONS: 'mL/min','mL/hr','μL/min','μL/hr'
diameter = 19.17
volume = [5, -5]
rate = [10, -10]
delay = [0, 0]

conn.setUnits(units)
conn.setDiameter(diameter)
conn.setVolume(volume)
conn.setRate(rate)
conn.setDelay(delay)

# conn.sendCommand('start')
conn.startPump()