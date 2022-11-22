# -*- coding = uft-8 -*-
# @File     : S05a_test_sensor_with_mat.py
# @Time     : 2022/11/21 10:04  
# @Author   : Samuel HONG
# @Description : Test sensor with material
# @Version  :

from S03_SlugSensor import SlugSensor

sensorB = SlugSensor(1, 'COM8')
sensorB.data_collect()

# while not slug_flow_past_B:
#     sensorB_li.append(board.analog[1].read())
#     if len(sensorB_li) > 20:
#         var_sensorB_li = np.var(sensorB_li[-10:])
#         if var_sensorB_li > 1e-4:
#             slug_flow_past_B = True
#     time.sleep(0.002)
#     continue

while True:
    sensorB.print_data()
    if sensorB.examine_variance():
        print("FLOW PAST B!")
