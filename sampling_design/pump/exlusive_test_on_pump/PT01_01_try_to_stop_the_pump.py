# -*- coding = uft-8 -*-
# @File     : PT01_01_try_to_stop_the_pump.py
# @Time     : 2022/11/18 16:08  
# @Author   : Samuel HONG
# @Description : try to stop the pump with code.
# @Version  :

from CHEMYX_multistep.core import connect

baud = 38400
conn = connect.Connection(port='COM7', baudrate=baud, x=0, mode=0)

conn.openConnection()
conn.stopPump()