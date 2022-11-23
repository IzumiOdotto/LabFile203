# -*- coding = uft-8 -*-
# @File     : 00_07_better_structure.py
# @Time     : 2022/11/23 10:15  
# @Author   : Samuel HONG
# @Description :  Better structure, and testiment.
# @Version  :


import time
import tkinter as tk
import numpy as np
from pyfirmata import Arduino, util
from valve6p2w.V00_01_valve6p2w_deployment import ValveA
from pump.pump_heritage_pot_0830 import Pump
from slug_flow_sensor.S06_duplicate_ssensor import FlowPastSensor


def detect_flow(pos):
    flow_sensor = FlowPastSensor(board, pos)
    flow_past = False
    while not flow_past:
        flow_sensor.collect()
        if flow_sensor.variance(10, 1e-4):
            flow_past = flow_sensor.variance(10, 1e-4)
    flow_sensor.reset()


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


if __name__ == "__main__":
    Arduino_port = 'COM8'
    board = Arduino(Arduino_port)
    it = util.Iterator(board)
    it.start()
    board.digital[13].write(1)

    analog_A = 0
    analog_B = 1
    analog_C = 2

    chemyx_A = Pump(6, 38400)
    chemyx_B = Pump(7, 38400)
    chemyx_A.initiate(volume=1, id=18.04, rate=0.5)
    chemyx_B.initiate(volume=1, id=18.04, rate=0.5)
    chemyx_A.start()
    chemyx_B.start()
    chemyx_A.stop()
    chemyx_B.stop()

    valveA = ValveA('4')
    valveA.switch_loop_to_sample()

    chemyx_B.initiate(volume=1, id=18.04, rate=0.5)
    chemyx_B.start()

    # Charge a Sampling Signal Right Now!
    root = tk.Tk()
    root.geometry('300x120')
    sampling_signal = SamplingSignal(root)
    root.mainloop()

    chemyx_A.initiate(volume=20, id=18.04, rate=0.5)
    chemyx_A.start()

    detect_flow(analog_C)
    print("Slug flow has arrived at sensor C.")

    chemyx_A.stop()
    chemyx_A_oscillating = True

    while chemyx_A_oscillating:
        chemyx_A.initiate(volume=-2.5, id=18.04, rate=0.8)
        chemyx_A.start()

        detect_flow(analog_B)
        print("Slug flow has arrived at sensor B.")

        chemyx_A.stop()
        chemyx_A.initiate(volume=2.5, id=18.04, rate=0.8)
        chemyx_A.start()

        detect_flow(analog_C)
        print("Slug flow has arrived at sensor C.")

        chemyx_A.stop()
        continue
