# -*- coding = uft-8 -*-
# @File     : R00b_li_val_pump.py
# @Time     : 2023/2/27 13:55  
# @Author   : Samuel HONG
# @Description : 
# @Version  :

from F00_01_pump_heritage_pot_0830 import Pump
import time


def reset_pump(pump):
    reset_pump_id = 18.04
    reset_pump_rate = 0.5
    reset_pump_volume = 10
    pump.initiate(volume=reset_pump_volume, id=reset_pump_id, rate=reset_pump_rate)
    pump.start()
    pump.stop()
    time.sleep(0.1)


volume_li = [1, -1]
rate_li = [1, -1]
syringe_id_A = 19.17

chemyx_A = Pump(3, 38400)
reset_pump(chemyx_A)
# chemyx_A.initiate(volume=volume_li, rate_li=rate_li, id=syringe_id_A)
chemyx_A.set_volume(volume_li)
chemyx_A.set_rate(rate_li)
chemyx_A.set_id(syringe_id_A)
time.sleep(0.1)
chemyx_A.start()
