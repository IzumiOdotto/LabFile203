# -*- coding = uft-8 -*-
# @File     : S11a_perftest_under_a_new_logic.py
# @Time     : 2023/2/15 16:36  
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


def reset_pump(pump):
    reset_pump_id = 18.04
    reset_pump_rate = 0.5
    reset_pump_volume = 10
    pump.initiate(volume=reset_pump_volume, id=reset_pump_id, rate=reset_pump_rate)
    pump.start()
    pump.stop()
    time.sleep(0.1)


class SamplingSignal(object):
    def __init__(self, master, chemyx_B, chemyx_C, valveA):
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.sampling_btn = tk.Button(self.frame, text="Sample Now", fg='blue',
                                      command=lambda: self.sampling_and_stop_chemyxB(chemyx_B, chemyx_C, valveA))
        self.sampling_btn.place(x=100, y=20)
        self.sampling_btn.pack(side='right', padx=15, pady=20)

    def sampling_and_stop_chemyxB(self, pump1, pump2, valve):
        # loop connects to flow stream, pump_B stops
        pump1.stop()
        pump2.stop()
        valve.switch_loop_to_sample()


def get_slug_flow(rate_eq=0.1, rate_solv=9):
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

    # Charge a Sampling Signal Right Now.
    root = tk.Tk()
    root.geometry('300x120')
    sampling_signal = SamplingSignal(root, chemyx_B, chemyx_C, valveA)
    root.mainloop()
    root.quit()

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


def delayer():
    root = tk.Tk()
    root.geometry('300x120')
    frame = tk.Frame(master=root)
    frame.pack()
    sampling_btn = tk.Button(frame, text="Sample Slow Down", fg='blue',
                             command=lambda: chemyx_A.set_rate(0.5))
    sampling_btn.place(x=100, y=20)
    sampling_btn.pack(side='right', padx=15, pady=20)
    root.mainloop()
    root.quit()


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


chemyx_A, chemyx_B, chemyx_C, valveA = get_slug_flow(rate_eq=0.05, rate_solv=0.95)

board = Arduino("COM8")
it = util.Iterator(board)
it.start()

# board.digital[13].write(1)
board.analog[0].enable_reporting()
sensor_li = []
last_10_data_li = []
var_shreshold = 0.8e-5

hwnd_analyzer, hwnd_pycharm = get_hwnd_analyzer_and_pycharm()
switch_valve_state(state=0)

delayer()

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
single_analysis(sample_name='blanksample0.05_0.95', address=r'D:\DATA\230224\BlankSample_1.lcd')
confirm()
time.sleep(5)
