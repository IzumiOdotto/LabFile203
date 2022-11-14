# -*- coding = uft-8 -*-
# @File     : 00_02_merge_with_slug_sensor.py
# @Time     : 2022/11/13 14:10  
# @Author   : Samuel HONG
# @Description : Go with this, whatever the result comes out.
# @Version  :

import time
import tkinter as tk
import numpy as np
from pyfirmata import Arduino, util
from valve6p2w.V00_01_valve6p2w_deployment import ValveA
from pump.pump_heritage_pot_0830 import Pump
from GUI.G00_button import SamplingSignal, OscillateSignal

if __name__ == '__main__':

    board = Arduino("COM8")

    it = util.Iterator(board)
    it.start()

    board.digital[13].write(1)
    board.analog[0].enable_reporting()
    board.analog[1].enable_reporting()
    board.analog[2].enable_reporting()

    # port_num of pump_A is 6, that of pump_B is 7
    chemyx_A = Pump(6, 38400)
    chemyx_B = Pump(7, 38400)
    chemyx_A.initiate(volume=1, id=18.04, rate=0.5)
    chemyx_B.initiate(volume=1, id=18.04, rate=0.5)
    chemyx_A.start()
    chemyx_B.start()
    time.sleep(0.025)
    chemyx_A.stop()
    chemyx_B.stop()

    # valve at sampling_mode
    valveA = ValveA('4')
    valveA.switch_loop_to_sample()

    chemyx_B.initiate(volume=1, id=18.04, rate=0.5)
    chemyx_B.start()

    # Charge a Sampling Signal Right Now!
    root = tk.Tk()
    root.geometry('300x120')
    sampling_signal = SamplingSignal(root)
    root.mainloop()

    # Initiate sensorA data collect process, A0.
    # sensorA_li = []
    # slug_flow_past_A = False
    # while not slug_flow_past_A:
    #     sensorA_li.append(board.analog[0].read())
    #     if len(sensorA_li) > 20:
    #         var_sensorA_li = np.var(sensorA_li[-10:])
    #         if var_sensorA_li > 1e-4:
    #             slug_flow_past_A = True
    #     time.sleep(0.002)
    #     continue
    # print("Surface has arrived at sensor A.")

    chemyx_B.stop()
    valveA.switch_loop_to_flowstream()
    sensorA_li = []

    chemyx_A.initiate(volume=20, id=18.04, rate=0.5)
    chemyx_A.start()

    sensorB_li = []
    sensorC_li = []

    # When the slug flow arrives at the position C
    slug_flow_past_C = False
    while not slug_flow_past_C:
        sensorC_li.append(board.analog[2].read())
        if len(sensorC_li) > 20:
            var_sensorC_li = np.var(sensorC_li[-10:])
            if var_sensorC_li > 1e-4:
                slug_flow_past_C = True
        time.sleep(0.002)
        continue
    print("Slug flow has arrived at sensor C.")

    chemyx_A.stop()
    chemyx_A_oscillating = True

    while chemyx_A_oscillating:

        sensorB_li = []
        sensorC_li = []

        chemyx_A.initiate(volume=-1, id=18.04, rate=0.5)
        chemyx_A.start()

        timeout = 20
        mustend_B = time.time() + timeout

        slug_flow_past_B = False
        while time.time() <= mustend_B and not slug_flow_past_B:
            sensorB_li.append(board.analog[1].read())
            if len(sensorB_li) > 20:
                var_sensorB_li = np.var(sensorB_li[-10:])
                if var_sensorB_li > 1e-4:
                    slug_flow_past_B = True
            time.sleep(0.002)
            continue
        print("Slug flow has arrived at sensor B.")

        chemyx_A.stop()
        chemyx_A.initiate(volume=1, id=18.04, rate=0.5)
        chemyx_A.start()

        timeout = 20
        mustend_C = time.time() + timeout

        slug_flow_past_C = False
        while time.time() <= mustend_C and not slug_flow_past_C:
            sensorC_li.append(board.analog[2].read())
            if len(sensorC_li) > 20:
                var_sensorC_li = np.var(sensorC_li[-10:])
                if var_sensorC_li > 1e-4:
                    slug_flow_past_C = True
            time.sleep(0.002)
            continue
        print("Slug flow has arrived at sensor B.")

        chemyx_A.stop()
        continue

# # Charge a Oscillatory Signal right Now!
# root = tk.Tk()
# root.geometry('300x120')
# oscillate_signal = OscillateSignal(root)
# root.mainloop()
