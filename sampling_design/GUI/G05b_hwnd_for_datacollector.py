# -*- coding = uft-8 -*-
# @File     : G05a_search_for_hwnd.py
# @Time     : 2022/12/16 15:22
# @Author   : Samuel HONG
# @Description : Search hwnd and call it out.
# @Version  :


import os
import time
import win32gui
import win32con
import pyautogui


def get_hwnd_analyzer(hwnd_li):
    word = '分析'
    for i in hwnd_li:
        title = win32gui.GetWindowText(i)
        if word in title:
            return i


def get_hwnd_datacollect_starter(hwnd_li):
    word = '开始数据采集'
    for i in hwnd_li:
        title = win32gui.GetWindowText(i)
        if word in title:
            return i


hwnd_li = []
win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), hwnd_li)
# print(hwnd_li)

print(get_hwnd_datacollect_starter(hwnd_li))
# hwnd_pycharm = win32gui.GetForegroundWindow()
# # print(hwnd_pycharm)
# hwnd_analyzer = get_hwnd_analyzer(hwnd_li)
# # print(hwnd_analyzer)
#
# # win32gui.SetForegroundWindow(hwnd_analyzer)
# # # time.sleep(3)
# # win32gui.SetForegroundWindow(hwnd_pycharm)
#
# # with win32gui.SetForegroundWindow(hwnd_analyzer):
# win32gui.ShowWindow(hwnd_analyzer, win32con.SW_SHOWMAXIMIZED)
# # while not win32gui.GetForegroundWindow() == hwnd_analyzer:
# #     pass
# # else:
# #     win32gui.SetForegroundWindow(hwnd_analyzer)
# #     time.sleep(3)
# # #
# # pyautogui.moveTo(1800, 510)
# # pyautogui.doubleClick()
# # pyautogui.press('0')
# # pyautogui.press('enter')
# # win32gui.SetForegroundWindow(hwnd_pycharm)
