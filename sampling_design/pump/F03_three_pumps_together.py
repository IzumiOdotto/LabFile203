# -*- coding = uft-8 -*-
# @File     : F03_three_pumps_together.py
# @Time     : 2023/2/21 13:41  
# @Author   : Samuel HONG
# @Description : 
# @Version  :

import datetime

from pyfirmata import Arduino, util
from pump.F00_01_pump_heritage_pot_0830 import Pump
from valve6p2w.V00_01_valve6p2w_deployment import ValveA
import time
import numpy as np
import win32gui
import win32con
import pyautogui
import tkinter as tk
import winsound


def reset_pump(pump):
    reset_pump_id = 18.04
    reset_pump_rate = 0.5
    reset_pump_volume = 1
    pump.initiate(volume=reset_pump_volume, id=reset_pump_id, rate=reset_pump_rate)
    pump.start()
    pump.stop()
    time.sleep(0.1)


class SamplingSignal(object):
    def __init__(self, master, chemyx_B, valveA):
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.sampling_btn = tk.Button(self.frame, text="Sample Now", fg='blue',
                                      command=lambda: self.sampling_and_stop_chemyxB(chemyx_B, valveA))
        self.sampling_btn.place(x=100, y=20)
        self.sampling_btn.pack(side='right', padx=15, pady=20)

    def sampling_and_stop_chemyxB(self, pump, valve):
        # loop connects to flow stream, pump_B stops
        pump.stop()
        valve.switch_loop_to_sample()


def get_slug_flow(rate_eq=0.1, rate_solv=1):
    syringe_id_A = 19.17
    syringe_id_B = 18.04
    syringe_id_C = 22.03
    chemyx_A = Pump(3, 38400)
    chemyx_B = Pump(7, 38400)
    chemyx_C = Pump(6, 38400)
    reset_pump(chemyx_A)
    reset_pump(chemyx_B)
    reset_pump(chemyx_C)

    valveA = ValveA('4')
    valveA.switch_loop_to_flowstream()

    chemyx_B.initiate(volume=10, id=syringe_id_B, rate=rate_eq)
    chemyx_C.initiate(volume=30, id=syringe_id_C, rate=rate_solv)
    chemyx_B.start()
    chemyx_C.start()

    # Charge a Sampling Signal Right Now!
    root = tk.Tk()
    root.geometry('300x120')
    sampling_signal = SamplingSignal(root, chemyx_B, valveA)
    root.mainloop()
    root.quit()

    chemyx_A.initiate(volume=20, id=syringe_id_A, rate=1.5)
    chemyx_A.start()
    return chemyx_A, chemyx_B, chemyx_C, valveA


chemyx_A, chemyx_B, chemyx_C, valveA = get_slug_flow()
