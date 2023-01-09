# -*- coding = uft-8 -*-
# @File     : G00_button.py
# @Time     : 2022/11/6 18:56  
# @Author   : Samuel HONG
# @Description : Try to charge a Sampling Signal and a Oscillate Signal
# @Version  :

import time
import tkinter as tk
from valve6p2w.V00_01_valve6p2w_deployment import ValveA
from pump.F00_01_pump_heritage_pot_0830 import Pump


class SamplingSignal(object):
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.sampling_btn = tk.Button(self.frame, text="Sample Now", fg='blue', command=self.sampling_and_stop_chemyxB)
        self.sampling_btn.place(x=100, y=20)
        self.sampling_btn.pack(side='right', padx=15, pady=20)

    def sampling_and_stop_chemyxB(self):
        # loop connects to flow stream, pump_B stops
        chemyx_B.stop()

        valveA = ValveA('4')
        valveA.switch_loop_to_flowstream()

class OscillateSignal(object):
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.sampling_btn = tk.Button(self.frame, text="Oscillate Now", fg='blue', command=self.oscillate_pumpA)
        self.sampling_btn.place(x=100, y=20)
        self.sampling_btn.pack(side='right', padx=15, pady=20)

    def oscillate_pumpA(self):
        chemyx_A.stop()
        while True:
            chemyx_A.initiate(volume=-0.25, id=18.04, rate=2.5)
            chemyx_A.start()
            time.sleep(10)
            chemyx_A.stop()

            chemyx_A.initiate(volume=0.25, id=18.04, rate=2.5)
            chemyx_A.start()
            time.sleep(10)
            chemyx_A.stop()


if __name__ == '__main__':
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

    # port_num of pump_A is 6
    chemyx_A = Pump(6, 38400)
    chemyx_A.initiate(volume=20, id=18.04, rate=0.5)
    chemyx_A.start()

    # Charge a Oscillatory Signal right Now!
    root = tk.Tk()
    root.geometry('300x120')
    oscillate_signal = OscillateSignal(root)
    root.mainloop()
