# -*- coding = uft-8 -*-
# @File     : 00_01meet_kinter.py
# @Time     : 2022/11/6 14:57  
# @Author   : Samuel HONG
# @Description : Let's meet Tkinter.
# @Version  :

import tkinter as tk

app = tk.Tk()
app.title("FishC Demo")

# The following is given by the example.
# app.geometry('300×240')
# This comes by the reference from web.
app.geometry("500x300+750+200")

theLabel = tk.Label(app, text="My GUI task")
theLabel.pack()

app.mainloop()


# Here comes one with buttons.
class APP:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        self.hi_there = tk.Button(frame, text='Say HI', fg='blue', command=self.say_hi)
        self.hi_there.pack()

    def say_hi(self):
        print('Hi! Here to deliver my joy!')

root =tk.Tk()
root.geometry('300x120')
app=APP(root)
root.mainloop()