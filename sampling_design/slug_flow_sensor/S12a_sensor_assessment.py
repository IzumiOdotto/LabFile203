# -*- coding = uft-8 -*-
# @File     : S12a_sensor_assessment.py
# @Time     : 2023/2/22 16:28  
# @Author   : Samuel HONG
# @Description : 
# @Version  :


from pyfirmata import Arduino, util

board = Arduino("COM8")
it = util.Iterator(board)
it.start()

board.analog[1].enable_reporting()
board.analog[2].enable_reporting()
sensor_li_1 = []
sensor_li_2 = [2]
last_10_data_li = []
var_shreshold = 0.6e-5

while True:
    sensor_li_1.append(board.analog[1].read())
    sensor_li_2.append(board.analog[2].read())
    print(board.analog[1].read(), '\t', board.analog[2].read())
