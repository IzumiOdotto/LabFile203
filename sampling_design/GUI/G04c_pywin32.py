# -*- coding = uft-8 -*-
# @File     : G04c_pywin32.py
# @Time     : 2022/12/17 20:42  
# @Author   : Samuel HONG
# @Description : Desciptas.
# @Version  :


import win32gui

hwnd_li = []
win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), hwnd_li)
word = '分析'
for i in hwnd_li:
    title = win32gui.GetWindowText(i)
    if word in title:
        print(i)
