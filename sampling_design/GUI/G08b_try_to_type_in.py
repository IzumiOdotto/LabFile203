# -*- coding = uft-8 -*-
# @File     : G08a_bring_to_front.py
# @Time     : 2023/2/12 11:09  
# @Author   : Samuel HONG
# @Description : 
# @Version  :


import time
import pyautogui
import win32gui
import win32con


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


hwnd_analyzer, hwnd_pycharm = get_hwnd_analyzer_and_pycharm()
single_analysis(sample_name='blanksample03')
confirm()

switch_valve_state(state=0)
time.sleep(15)
switch_valve_state(state=1)
