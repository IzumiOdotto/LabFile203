# -*- coding = uft-8 -*-
# @File     : quote_pump_func.py
# @Time     : 2022/11/6 15:46  
# @Author   : Samuel HONG
# @Description : Sort of assimilate some functions of the pump.
# @Version  :

import time
from pump_heritage_pot_0830 import Pump

# port_num of pump_B is 7
chemyx_A = Pump(6, 38400)
chemyx_A.initiate(volume=-10, id=18.04, rate=5)
chemyx_A.start()
time.sleep(30)

chemyx_A.initiate(volume=-5, id=18.04, rate=0.5)