# -*- coding = uft-8 -*-
# @File     : G11a_try_tkinkter_destroy.py
# @Time     : 2023/2/24 12:59  
# @Author   : Samuel HONG
# @Description : 
# @Version  :

import tkinter as tk


# def delayer():
#     root = tk.Tk()
#     root.geometry('300x120')
#     frame = tk.Frame(master=root)
#     frame.pack()
#     sampling_btn = tk.Button(frame, text="Sample Slow Down", fg='blue',
#                              command=lambda: quit(root))
#     sampling_btn.place(x=100, y=20)
#     sampling_btn.pack(side='right', padx=15, pady=20)
#     root.mainloop()
#     return root
#
#
# def quit(root):
#     print('set rate')
#     root.destroy()

class Delayer(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x120')
        self.frame = tk.Frame(master=self.root)
        self.frame.pack()

        self.button = tk.Button(self.root, text="Sample Slow Down", fg='blue',
                                command=self.quit)
        self.button.place(x=150, y=20)
        self.button.pack(side='right', padx=100, pady=20)
        self.root.mainloop()

    def quit(self):
        print("set rate")
        self.root.destroy()


delayer = Delayer()
print('Me popping out means success.')
