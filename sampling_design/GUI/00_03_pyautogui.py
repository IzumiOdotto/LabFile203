# -*- coding = uft-8 -*-
# @File     : 00_03_pyautogui.py
# @Time     : 2022/12/2 17:17
# @Author   : Samuel HONG
# @Description : Move to Analysis and switch valve.
# @Version  :

import time
import pyautogui

# time.sleep(1)
# pyautogui.click(510, 1060)
# pyautogui.click(1800, 510)
# pyautogui.doubleClick(1800, 510)
# time.sleep(1)

# time.sleep(5)
# print(pyautogui.position())

pyautogui.moveTo(510, 1060)

pyautogui.click()
pyautogui.moveTo(1800, 510)
pyautogui.doubleClick()

pyautogui.press('0')
pyautogui.press('enter')
