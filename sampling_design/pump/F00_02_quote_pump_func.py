# -*- coding = uft-8 -*-
# @File     : F00_02_quote_pump_func.py
# @Time     : 2022/11/6 15:46  
# @Author   : Samuel HONG
# @Description : Sort of assimilate some functions of the pump.
# @Version  :

import time
from F00_01_pump_heritage_pot_0830 import Pump



def oscillate_pumpA():
    chemyx_A.initiate(volume=-0.5,id=18.04,rate=0.5)
    chemyx_A.start()
    time.sleep(10)
    chemyx_A.stop()

    chemyx_A.initiate(volume=0.5, id=18.04, rate=0.5)
    chemyx_A.start()
    time.sleep(10)
    chemyx_A.stop()

if __name__=="__main__":
    # port_num of pump_B is 7
    chemyx_A = Pump(6, 38400)
    chemyx_A.initiate(volume=-10, id=18.04, rate=5)
    chemyx_A.start()
    time.sleep(30)

    chemyx_A.initiate(volume=-5, id=18.04, rate=0.5)