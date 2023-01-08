# -*- coding = uft-8 -*-
# @File     : 00_04a_pywin32.py
# @Time     : 2022/12/10 12:30  
# @Author   : Samuel HONG
# @Description : Meet pywin32.
# @Version  :


import time

import win32gui
import win32con

hwnd_analyzer = 197524
hwnd_pycharm = 3019364
# win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
# time.sleep(5)
# win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
win32gui.SetForegroundWindow(hwnd_analyzer)
time.sleep(5)
win32gui.SetForegroundWindow(hwnd_pycharm)
