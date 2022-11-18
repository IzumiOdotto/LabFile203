# -*- coding = uft-8 -*-
# @File     : PT01_00_send_command.py
# @Time     : 2022/11/18 15:21  
# @Author   : Samuel HONG
# @Description :  Just write a command and send it, see that of will happen.
# @Version  :

from CHEMYX_multistep.core import connect

baud = 38400
conn = connect.Connection(port='COM7', baudrate=baud, x=0, mode=0)

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
