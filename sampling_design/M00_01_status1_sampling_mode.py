# -*- coding = uft-8 -*-
# @File     : M00_01_status1_sampling_mode.py
# @Time     : 2022/11/6 18:05  
# @Author   : Samuel HONG
# @Description : Sampling
# @Version  :

from valve6p2w.V00_01_valve6p2w_deployment import ValveA
from pump.F00_01_pump_heritage_pot_0830 import Pump
from GUI.G00_button import SamplingSignal
import tkinter as tk

# valve at sampling_mode
valveA = ValveA('4')
valveA.switch_loop_to_sample()

# port_num of pump_B is 7
chemyx_B = Pump(7, 38400)
chemyx_B.initiate(volume=1, id=18.04, rate=0.5)
chemyx_B.start()

# Charge a Sampling Signal Right Now!
root = tk.Tk()
root.geometry('300x120')
sampling_signal = SamplingSignal(root)
root.mainloop()

chemyx_A=Pump(6,38400)
chemyx_A.initiate(volume=20,id=18.04,rate=1)
chemyx_A.start()

