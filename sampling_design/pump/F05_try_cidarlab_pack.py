# -*- coding = uft-8 -*-
# @File     : F05_try_cidarlab_pack.py
# @Time     : 2023/2/22 14:31  
# @Author   : Samuel HONG
# @Description : 
# @Version  :

from CIDARLab import pump_code_pack

sc_com5 = pump_code_pack.SerialConnection("COM5")

address = 0
p_ultra = pump_code_pack.PumpUltra(sc_com5, address, name="PHDUltra")

i_d = 18.14
p_ultra.set_dia(diameter=i_d)

rate = 10
rate_unit = "ul/min"
p_ultra.set_infuse_rate(rate, rate_unit)

p_ultra.set_irun()
