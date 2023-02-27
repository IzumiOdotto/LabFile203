# -*- coding = uft-8 -*-
# @File     : S10f_perftest_MeOHtest_function_get_flow.py
# @Time     : 2023/2/11 9:53  
# @Author   : Samuel HONG
# @Description : 
# @Version  :


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


def get_slug_flow():
    syringe_id_A = 19.17
    chemyx_A = Pump(6, 38400)
    chemyx_B = Pump(7, 38400)
    reset_pump(chemyx_A)
    reset_pump(chemyx_B)

    valveA = ValveA('4')
    valveA.switch_loop_to_flowstream()

    chemyx_B.initiate(volume=10, id=18.04, rate=1)
    chemyx_B.start()

    # Charge a Sampling Signal Right Now!
    root = tk.Tk()
    root.geometry('300x120')
    sampling_signal = SamplingSignal(root,chemyx_B, valveA)
    root.mainloop()
    root.quit()

    chemyx_A.initiate(volume=20, id=syringe_id_A, rate=1)
    chemyx_A.start()


get_slug_flow()

board = Arduino("COM8")
it = util.Iterator(board)
it.start()

# board.digital[13].write(1)
board.analog[0].enable_reporting()
sensor_li = []
last_10_data_li = []
var_shreshold = 1e-4

while True:
    sensor_li.append(board.analog[0].read())
    print(board.analog[0].read())

    signal_standard_arr = np.array(sensor_li[-10:])
    if len(sensor_li) > 20:
        var_sensor_li = np.var(sensor_li[-10:])
    time.sleep(0.002)

    # if var_sensor_li > 1e-4, send a window and quit.
    # if var_sensor_li exists.
    if 'var_sensor_li' in locals():
        if var_sensor_li > var_shreshold:
            winsound.Beep(2000, 50)

