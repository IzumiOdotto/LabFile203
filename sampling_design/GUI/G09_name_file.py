# -*- coding = uft-8 -*-
# @File     : G09_name_file.py
# @Time     : 2023/2/12 11:24  
# @Author   : Samuel HONG
# @Description : 
# @Version  :

import pyautogui
import win32gui


def single_analysis(sample_name='test'):
    sample_name = 'somefilename'
    pyautogui.click(300, 35)
    pyautogui.click(350, 60)
    pyautogui.doubleClick(990, 315)
    pyautogui.write(sample_name)
    pyautogui.write('\n')


# 300,35 for data collecting
# 350,60 for single analysis

single_analysis()


# def get_hwnd_datacollect_starter(hwnd_li):
#     word = '开始数据采集'
#     for i in hwnd_li:
#         title = win32gui.GetWindowText(i)
#         if word in title:
#             return i


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


confirm()
