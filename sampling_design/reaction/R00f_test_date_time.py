# -*- coding = uft-8 -*-
# @File     : R00f_test_date_time.py
# @Time     : 2023/2/28 10:16  
# @Author   : Samuel HONG
# @Description : 
# @Version  :

import datetime


def o(reaction_time):
    start_time = datetime.datetime.now()

    while (datetime.datetime.now() - start_time).seconds < reaction_time:
        print("Finished")


o(5)
