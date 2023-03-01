# -*- coding = uft-8 -*-
# @File     : F05a_try_cidarlab_pack.py
# @Time     : 2023/2/22 14:31  
# @Author   : Samuel HONG
# @Description : 
# @Version  :

from CIDARLab import pump_code_pack as pcp

sc_com5 = pcp.SerialConnection("COM5")
sc_com10 = pcp.SerialConnection("COM10")

p_ultra_C_solv = pcp.PumpUltra(sc_com5, address=0, name="PHDUltra")
p_ultra_B_eq = pcp.PumpUltra(sc_com10, address=0, name="PHDUltra")

i_d_C = 22.03
i_d_B = 14.75
p_ultra_C_solv.set_dia(diameter=i_d_C)
p_ultra_B_eq.set_dia(diameter=i_d_B)
# p_ultra.set_pump_mode()

rate = 100
rate_unit = "ul/min"
p_ultra_C_solv.set_infuse_rate(rate, rate_unit)
p_ultra_B_eq.set_infuse_rate(rate,rate_unit)

p_ultra_C_solv.set_irun()
p_ultra_B_eq.set_irun()

p_ultra_C_solv.set_stop()
p_ultra_B_eq.set_stop()