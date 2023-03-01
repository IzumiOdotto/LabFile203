# -*- coding = uft-8 -*-
# @File     : R00a_reaction_sketch.py
# @Time     : 2023/2/25 16:38  
# @Author   : Samuel HONG
# @Description : 
# @Version  :

import datetime
import os.path

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
import threading

global syringe_id_A, syringe_id_B, syringe_id_C
syringe_id_A = 19.17
syringe_id_B = 18.04
syringe_id_C = 22.03


def reset_pump(pump):
    reset_pump_id = 18.04
    reset_pump_rate = 0.5
    reset_pump_volume = 10
    pump.initiate(volume=reset_pump_volume, id=reset_pump_id, rate=reset_pump_rate)
    pump.start()
    pump.stop()
    time.sleep(0.1)


# class SamplingSignal(object):
# def __init__(self, pump1, pump2, valve):
#     self.root = tk.Tk()
#     self.root.geometry('300x120')
#     self.frame = tk.Frame(self.root)
#     self.frame.pack()
#
#     self.sampling_btn = tk.Button(self.frame, text="Sample Now", fg='blue',
#                                   command=lambda: self.sampling_and_stop_chemyxB(pump1, pump2, valve))
#     self.sampling_btn.place(x=100, y=20)
#     self.sampling_btn.pack(side='right', padx=15, pady=20)
#     self.root.mainloop()

def sampling_and_stop_chemyxB(pump1, pump2, valve):
    # loop connects to flow stream, pump_B stops
    pump1.stop()
    pump2.stop()
    valve.switch_loop_to_sample()
    time.sleep(1)


def get_slug_flow(rate_eq=0.1, rate_solv=9):
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

    # Charge a Sampling Signal Right Now.

    # sampling_signal = SamplingSignal(chemyx_B, chemyx_C, valveA)
    time.sleep(120)
    sampling_and_stop_chemyxB(chemyx_B, chemyx_C, valveA)

    chemyx_A.initiate(volume=20, id=syringe_id_A, rate=1.75)
    chemyx_A.start()
    return chemyx_A, chemyx_B, chemyx_C, valveA


def get_hwnd_analyzer(hwnd_li):
    word = '分析'
    for i in hwnd_li:
        title = win32gui.GetWindowText(i)
        if word in title:
            return i


def switch_valve_state(state):
    pyautogui.moveTo(1800, 510)
    pyautogui.doubleClick()
    pyautogui.press('%d' % state)
    pyautogui.press('enter')
    win32gui.SetForegroundWindow(hwnd_pycharm)


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


def oscillation(reaction_time, oscillate_rate=1):
    start_time = datetime.datetime.now()
    while (datetime.datetime.now() - start_time).seconds < reaction_time:

        sensor_li_B = [0]
        sensor_li_C = [0]

        chemyx_A.initiate(volume=-2.5, id=syringe_id_A, rate=oscillate_rate)
        time.sleep(0.025)
        chemyx_A.start()
        time.sleep(0.002)

        past_B = False
        while not past_B:
            sensor_li_B.append(board.analog[4].read())
            if len(sensor_li_B) > 20:
                var_sensorB_li = np.var(sensor_li_B[-10:])
                if var_sensorB_li > 2e-5:
                    past_B = True
            time.sleep(0.002)
            continue
        print("Slug flow has arrived at sensor B.")

        chemyx_A.stop()
        time.sleep(0.025)
        chemyx_A.initiate(volume=2.5, id=syringe_id_A, rate=oscillate_rate)
        time.sleep(0.025)
        chemyx_A.start()

        past_C = False
        while not past_C:
            sensor_li_C.append(board.analog[5].read())
            if len(sensor_li_C) > 20:
                var_sensorC_li = np.var(sensor_li_C[-10:])
                if var_sensorC_li > 2e-5:
                    past_C = True
            time.sleep(0.002)
            continue
        print("Slug flow has arrived at sensor C.")

        chemyx_A.stop()
        time.sleep(0.025)
        continue


class Stopper(object):
    def __init__(self, stop_oscillating):
        self.root = tk.Tk()
        self.root.geometry('300x120')
        self.frame = tk.Frame(master=self.root)
        self.frame.pack()
        sd_btn = tk.Button(self.frame, text="Stop Oscillation", fg='blue',
                           command=lambda: self.stop_oscillation(stop_oscillating))
        sd_btn.place(x=100, y=20)
        sd_btn.pack(side='right', padx=15, pady=20)
        self.root.mainloop()

    def stop_oscillation(self, stop_bool):
        stop_bool = False
        self.root.destroy()


def single_analysis(sample_name='test', address=r'D:\DATA\BlankSample_1.lcd'):
    if not os.path.exists(os.path.dirname(address)):
        os.makedirs(os.path.dirname(address))

    pyautogui.click(300, 35)
    pyautogui.click(350, 60)
    pyautogui.moveTo(990, 315)
    pyautogui.doubleClick()
    pyautogui.write(sample_name)

    pyautogui.click(1000, 440)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write(address)
    pyautogui.write('\n')
    # pyautogui.click(970,765)


def confirm():
    exists_frame = False
    while not exists_frame:
        hwnd_li = []
        win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), hwnd_li)
        word = '开始数据采集'
        for i in hwnd_li:
            title = win32gui.GetWindowText(i)
            if word in title:
                # return i
                pyautogui.write('\n')
                exists_frame = True


def get_hwnd_analyzer_and_pycharm():
    hwnd_li = []
    win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), hwnd_li)
    hwnd_pycharm = win32gui.GetForegroundWindow()
    hwnd_analyzer = get_hwnd_analyzer(hwnd_li)

    win32gui.ShowWindow(hwnd_analyzer, win32con.SW_SHOWMAXIMIZED)
    current_window = win32gui.GetForegroundWindow()
    if current_window == hwnd_pycharm:
        win32gui.SetForegroundWindow(hwnd_analyzer)
    return hwnd_analyzer, hwnd_pycharm


# Requirement:
# as soon as the valve switch, slug flow oscillates.

chemyx_A, chemyx_B, chemyx_C, valveA = get_slug_flow(rate_eq=0.1, rate_solv=0.9)

board = Arduino("COM8")

it = util.Iterator(board)
it.start()

board.analog[0].enable_reporting()
board.analog[4].enable_reporting()
board.analog[5].enable_reporting()

sensor_li = []
last_10_data_li = []
var_shreshold = 0.8e-5

hwnd_analyzer, hwnd_pycharm = get_hwnd_analyzer_and_pycharm()
switch_valve_state(state=0)

sensor_li_B = []
sensor_li_C = []

past_C = False
while not past_C:
    sensor_li_C.append(board.analog[5].read())
    signal_standard_arr_C = np.array(sensor_li_C[-10:])
    if len(sensor_li_C) > 20:
        var_sensor_li_C = np.var(sensor_li_C[-10:])
        if var_sensor_li_C > 2e-5:
            past_C = True
    time.sleep(0.002)
    continue
print("Slug flow has arrived at sensor C.")

chemyx_A.stop()
oscillation(reaction_time=240, oscillate_rate=2)
chemyx_A.stop()
chemyx_A.initiate(volume=20, id=syringe_id_A, rate=1.5)
chemyx_A.start()

# global chemyx_A_oscillating
# chemyx_A_oscillating = True

# thread_1 = threading.Thread(target=oscillation())
# thread_1.start()
# stopper = Stopper()

delayer = Delayer(chemyx_A)

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
            break

switch_valve_state(state=1)
chemyx_A.stop()
single_analysis(sample_name='reaction_t240_0.1_0.9', address=r'D:\DATA\230228\Reaction_10Cit_0.1Ru_1.lcd')
confirm()
time.sleep(5)
