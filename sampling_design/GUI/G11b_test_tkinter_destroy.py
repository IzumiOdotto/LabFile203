# -*- coding = uft-8 -*-
# @File     : G11b_test_tkinter_destroy.py
# @Time     : 2023/2/24 13:25  
# @Author   : Samuel HONG
# @Description : 
# @Version  :

import time
import tkinter as tk
from pump.F00_01_pump_heritage_pot_0830 import Pump


def reset_pump(pump):
    reset_pump_id = 18.04
    reset_pump_rate = 0.5
    reset_pump_volume = 10
    pump.initiate(volume=reset_pump_volume, id=reset_pump_id, rate=reset_pump_rate)
    pump.start()
    pump.stop()
    time.sleep(0.1)


class Delayer(object):
    def __init__(self, chemyx_A):
        self.root = tk.Tk()
        self.root.geometry('300x120')
        self.frame = tk.Frame(master=self.root)
        self.frame.pack()
        sd_btn = tk.Button(self.frame, text="Sample Slow Down", fg='blue',
                           command=lambda: self.set_rate_destroy(chemyx_A, 0.5))
        sd_btn.place(x=100, y=20)
        sd_btn.pack(side='right', padx=15, pady=20)
        self.root.mainloop()

    def set_rate_destroy(self, pump, rate):
        pump.set_rate(rate)
        self.root.destroy()


chemyx_A = Pump(3, 38400)
reset_pump(chemyx_A)
delayer = Delayer(chemyx_A)
print("See how it done.")
