# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:50:21 2022
@author: cukelarter

Script for initiating multi-step run on Chemyx Syringe Pump. Tested on Chemyx 100-X.
Capable of variable units between steps, and linear ramping within a step.

After importing serial connection driver we connect to the pump. Connection will remain open
until user calls "conn.closeConnection()". If user does not call this before exiting
the connection will remain locked until the connection is physically broken (unplugged).
The run will continue to completion after connection is closed.

To initiate multi-step routine the user must enter "Multi-step" mode on the pump before running code.
Multi-step routine will repeat an infinite number of times.
"""
#%% Import CHEMYX serial connection module/driver
from core import connect

# get open port info
portinfo = connect.getOpenPorts() 

# MUST set baudrate in pump "System Settings", and MUST match this rate:
baudrate=9600
# initiate Connection object with first open port
conn = connect.Connection(port=str(portinfo[0]),baudrate=baudrate, x=0, mode=0)

#%% Connect and Run Pump - Multi-Step Setup
if __name__=='__main__':
    
    # Open Connection to pump
    conn.openConnection()
    
    # Setup parameters for multi-step run
    units='mL/min' 			# OPTIONS: 'mL/min','mL/hr','μL/min','μL/hr'
    diameter=28.6           # 28.6mm diameter
    volume=[0.25,5,2]       # Volume = [Step1: 0.25mL, Step2: 5mL, Step3: 2mL]
    delay=[0.1,0.2,0.3]     # Delay  = [Step1: 6s,     Step2: 12s, Step3: 18s]
    
    # Variable flow rates in each step, linear ramping generated by pump
    rate1=[20,5,40]         # between rate1 and rate2 for each step
    rate2=[21,6,41]         # use one rate list for linear flow per step
    varrates=[str(rate1[ii])+'/'+str(rate2[ii]) for ii in range(len(rate1))]
    # Rate = [Step1: 20mL/min->21mL/min, Step2: 5mL/min->6mL/min, Step3: 40mL/min->41mL/min]
            
    # communicate parameters to pump
    conn.setUnits(units)
    conn.setDiameter(diameter)  
    conn.setVolume(volume)      
    conn.setRate(varrates)          
    conn.setDelay(delay)  
    
    # start pump
    conn.startPump()