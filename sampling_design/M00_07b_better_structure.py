# -*- coding = uft-8 -*-
# @File     : M00_07b_better_structure.py
# @Time     : 2022/11/24 10:46  
# @Author   : Samuel HONG
# @Description : Better get pump reconstructed.
# @Version  :

import time
import tkinter as tk
from pyfirmata import Arduino, util
from valve6p2w.V00_01_valve6p2w_deployment import ValveA
from pump.F00_01_pump_heritage_pot_0830 import Pump
from slug_flow_sensor.S06_duplicate_ssensor import FlowPastSensor


def detect_flow(pos):
    flow_sensor = FlowPastSensor(board, pos)
    flow_past = False
    while not flow_past:
        flow_sensor.collect()
        if flow_sensor.variance(10, 1e-4):
            flow_past = flow_sensor.variance(10, 1e-4)
    flow_sensor.reset()


def reset_pump(pump):
    reset_pump_id = 18.04
    reset_pump_rate = 0.5
    reset_pump_volume = 1
    pump.initiate(volume=reset_pump_volume, id=reset_pump_id, rate=reset_pump_rate)
    pump.start()
    pump.stop()
    time.sleep(0.1)


class SamplingSignal(object):
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.sampling_btn = tk.Button(self.frame, text="Sample Now", fg='blue',
                                      command=lambda: self.sampling_and_stop_chemyxB(chemyx_B, valveA))
        self.sampling_btn.place(x=100, y=20)
        self.sampling_btn.pack(side='right', padx=15, pady=20)

    def sampling_and_stop_chemyxB(self, pump, valve):
        # loop connects to flow stream, pump_B stops
        pump.stop()
        valve.switch_loop_to_flowstream()


if __name__ == "__main__":
    Arduino_port = 'COM8'
    board = Arduino(Arduino_port)
    it = util.Iterator(board)
    it.start()
    board.digital[13].write(1)

    analog_A, analog_B, analog_C = 0, 1, 2
    syringe_id_A = 19.17

    chemyx_A = Pump(6, 38400)
    chemyx_B = Pump(7, 38400)
    reset_pump(chemyx_A)
    reset_pump(chemyx_B)

    valveA = ValveA('4')
    valveA.switch_loop_to_sample()

    chemyx_B.initiate(volume=10, id=18.04, rate=1)
    chemyx_B.start()

    # Charge a Sampling Signal Right Now!
    root = tk.Tk()
    root.geometry('300x120')
    sampling_signal = SamplingSignal(root)
    root.mainloop()

    chemyx_A.initiate(volume=20, id=syringe_id_A, rate=1)
    chemyx_A.start()

    detect_flow(analog_C)
    print("Slug flow has arrived at sensor C.")

    chemyx_A.stop()
    time.sleep(0.1)
    chemyx_A_oscillating = True

    while chemyx_A_oscillating:
        chemyx_A.initiate(volume=-5, id=syringe_id_A, rate=5)
        chemyx_A.start()

        detect_flow(analog_B)
        print("Slug flow has arrived at sensor B.")

        chemyx_A.stop()
        time.sleep(0.1)
        chemyx_A.initiate(volume=5, id=18.04, rate=5)
        chemyx_A.start()

        detect_flow(analog_C)
        print("Slug flow has arrived at sensor C.")

        chemyx_A.stop()
        time.sleep(0.1)
        continue
