# -*- coding = uft-8 -*-
# @File     : S11b_in_case_sensor_to_analysis_go_wrong.py
# @Time     : 2023/2/17 15:46  
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


def single_analysis(sample_name='test'):
    pyautogui.click(300, 35)
    pyautogui.click(350, 60)
    pyautogui.moveTo(990, 315)
    pyautogui.doubleClick()
    pyautogui.write(sample_name)
    pyautogui.write('\n')


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

chemyx_A = Pump(3, 38400)

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
# chemyx_A.stop()
single_analysis(sample_name='blanksample04')
time.sleep(5)
confirm()
time.sleep(5)