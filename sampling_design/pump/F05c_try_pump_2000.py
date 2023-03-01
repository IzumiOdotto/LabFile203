# -*- coding = uft-8 -*-
# @File     : F05c_try_pump_2000.py
# @Time     : 2023/3/1 10:17  
# @Author   : Samuel HONG
# @Description : 
# @Version  :


import time

from CIDARLab import pump_code_pack as pck

sc_com5 = pck.SerialConnection("COM5")
pC5 = pck.Pump2000(sc_com5, address=0, name="PHDUltra")

i_d = 18.14
pC5.set_dia(diameter=i_d)

rate = 100
rate_unit = "ul/min"
pC5.set_infuse_rate(rate, rate_unit)

pC5.set_irun()
time.sleep(3)
pC5.set_stop()
