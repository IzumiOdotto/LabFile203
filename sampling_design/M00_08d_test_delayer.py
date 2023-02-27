# -*- coding = uft-8 -*-
# @File     : M00_08d_test_delayer.py
# @Time     : 2023/2/24 10:54  
# @Author   : Samuel HONG
# @Description : 
# @Version  :

import time
import tkinter as tk
from pyfirmata import Arduino, util
from pump.F00_01_pump_heritage_pot_0830 import Pump


# from M00_08c_time_split import reset_pump

def reset_pump(pump):
    reset_pump_id = 18.04
    reset_pump_rate = 0.5
    reset_pump_volume = 10
    pump.initiate(volume=reset_pump_volume, id=reset_pump_id, rate=reset_pump_rate)
    pump.start()
    pump.stop()
    time.sleep(0.1)


class SlowingDownSignal(object):
    def __init__(self,master, chemyx_A):
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.sampling_btn = tk.Button(self.frame, text="Sample Now", fg='blue',
                                      command=lambda: self.slowingdown_chemyx_A(chemyx_A))
        self.sampling_btn.place(x=100, y=20)
        self.sampling_btn.pack(side='right', padx=15, pady=20)

    def slowingdown_chemyx_A(self, pump):
        pump.stop()


def delayer():
    root = tk.Tk()
    root.geometry('300x120')
    frame = tk.Frame(master=root)
    frame.pack()
    sampling_btn = tk.Button(frame, text="Sample Slow Down", fg='blue',
                             command=lambda: chemyx_A.set_rate(0.5))
    sampling_btn.place(x=100, y=20)
    sampling_btn.pack(side='right', padx=15, pady=20)
    root.mainloop()
    root.quit()


# chemyx_A.set_rate(0.5)
chemyx_A = Pump(3, 38400)
reset_pump(chemyx_A)
delayer()
print("Has it done yet")

board = Arduino("COM8")
it = util.Iterator(board)
it.start()

# board.digital[13].write(1)
board.analog[0].enable_reporting()
sensor_li = []
last_10_data_li = []
var_shreshold = 0.8e-5

while True:
    sensor_li.append(board.analog[0].read())
    print(board.analog[0].read())
