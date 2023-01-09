# -*- coding = uft-8 -*-
# @File     : G02_block_example.py
# @Time     : 2022/11/6 23:46  
# @Author   : Samuel HONG
# @Description : 
# @Version  :

import tkinter as tk


class SamplingSignal(object):
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.sampling_btn = tk.Button(self.frame, text="Sample Now", fg='blue')
        self.sampling_btn.place(x=100, y=20)
        self.sampling_btn.pack(side='right', padx=15, pady=20)


class OscillateSignal(object):
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.sampling_btn = tk.Button(self.frame, text="Oscillate Now", fg='blue')
        self.sampling_btn.place(x=100, y=20)
        self.sampling_btn.pack(side='right', padx=15, pady=20)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('300x120')
    sampling_signal = SamplingSignal(root)
    root.mainloop()

    root = tk.Tk()
    root.geometry('300x120')
    oscillate_signal = OscillateSignal(root)
    root.mainloop()
