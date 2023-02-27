# -*- coding = uft-8 -*-
# @File     : S11c_test_filename.py
# @Time     : 2023/2/20 10:04  
# @Author   : Samuel HONG
# @Description : 
# @Version  :

import datetime
import time

import pyautogui
import pyperclip

sample_name = 'test'
print(datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
# pyperclip.copy(sample_name)
pyautogui.moveTo(990, 315)
pyautogui.doubleClick()
time.sleep(1)
# pyperclip.paste()
pyautogui.write(sample_name)

address = r'D:\DATA\221105\BlankSample_H3PO4MeCN_MeCN\BlankSample_H3PO4MeCN_MeCN23.lcd'
pyautogui.click(1000, 440)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(address)
