# -*- coding = uft-8 -*-
# @File     : G04b_pywin32.py
# @Time     : 2022/12/10 13:31  
# @Author   : Samuel HONG
# @Description : How to acquire hwnd using python
# @Version  :

import sys
import win32gui
import win32con


# get hwnd of all the windows.
def get_all_windows():
    hWnd_list = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWnd_list)
    print(hWnd_list)
    return hWnd_list


# get hwnd of a sub window.
def get_son_windows(parent):
    hWnd_child_list = []
    win32gui.EnumChildWindows(parent, lambda hWnd, param: param.append(hWnd), hWnd_child_list)
    print(hWnd_child_list)
    return hWnd_child_list


# get hwnd title.
def get_title(hwnd):
    title = win32gui.GetWindowText(hwnd)
    print('窗口标题:%s' % (title))
    return title


# get hwnd classname.
def get_classname(hwnd):
    classname = win32gui.GetClassName(hwnd)
    print('窗口类名:%s' % (classname))
    return classname


if __name__ == '__main__':
    hwnd_li = get_all_windows()
    for i in hwnd_li:
        print(i)
        get_title(i)
        print('\r')

    hwnd = 197524
    title = win32gui.GetWindowText(hwnd)
    print(title)
