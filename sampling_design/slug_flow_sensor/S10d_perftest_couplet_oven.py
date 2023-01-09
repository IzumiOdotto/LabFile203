# -*- coding = uft-8 -*-
# @File     : S10d_perftest_couplet_oven.py
# @Time     : 2023/1/8 22:59  
# @Author   : Samuel HONG
# @Description : After detecting a slug flow is coming,
# @Version  :


from pyfirmata import Arduino, util
import time
import numpy as np
import win32gui
import win32con
import pyautogui
import winsound


def get_hwnd_analyzer(hwnd_li):
    word = '分析'
    for i in hwnd_li:
        title = win32gui.GetWindowText(i)
        if word in title:
            return i


hwnd_li = []
win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), hwnd_li)
hwnd_pycharm = win32gui.GetForegroundWindow()
hwnd_analyzer = get_hwnd_analyzer(hwnd_li)

board = Arduino("COM8")
it = util.Iterator(board)
it.start()

# board.digital[13].write(1)
board.analog[0].enable_reporting()

sensor_li = []
last_10_data_li = []
var_shreshold = 2.5e-4

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

win32gui.ShowWindow(hwnd_analyzer, win32con.SW_SHOWMAXIMIZED)

pyautogui.moveTo(1780, 510)
pyautogui.doubleClick()
pyautogui.press('0')
pyautogui.press('enter')

win32gui.ShowWindow(hwnd_pycharm, win32con.SW_SHOWMAXIMIZED)
