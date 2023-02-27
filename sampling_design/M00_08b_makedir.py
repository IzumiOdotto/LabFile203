# -*- coding = uft-8 -*-
# @File     : M00_08b_makedir.py
# @Time     : 2023/2/22 17:22  
# @Author   : Samuel HONG
# @Description : 
# @Version  :
import os.path

address=r'D:\DATA\BlankSample_1.lcd'
print(os.path.dirname(address)+r'\test')
os.makedirs(os.path.dirname(address)+r'\test')