# -*- coding = uft-8 -*-
# @File     : P00_pump_rewrite_attempt.py
# @Time     : 2022/11/23 14:30  
# @Author   : Samuel HONG
# @Description : Just naturally have the attempt to rewrite the Pump to give it a better class.
# @Version  :


import serial
import time


class Connection(object):
    def __init__(self, port, baud, x=0, mode=0, verbose=False):
        self.ser = serial.Serial()
        self.port = port
        self.baud = baud
        self.x = x
        self.mode = mode
        self.verbose = verbose

    def open_connection(self):
        try:
            self.ser.baudrate = self.baud
            self.ser.port = self.port
            self.ser.timeout = 0
            self.ser.open()
            if self.ser.isOpen():
                if self.verbose:
                    print("Opened port")
                    print(self.ser)
                self.get_pump_status()
                self.ser.flushInput()
                self.ser.flushOutput()

        except Exception as e:
            if self.verbose:
                print('Failed to connect to pump')
                print(e)
            pass

    def close_connection(self):
        self.ser.close()
        if self.verbose:
            print("Closed connection")

    def send_command(self, command):
        try:
            arg = bytes(str(command), 'utf8') + b'\r'
            self.ser.write(arg)
            time.sleep(0.5)
            response = self.get_response()
            return response
        except TypeError as e:
            if self.verbose:
                print(e)
            self.ser.close()

    def get_response(self):
        try:
            response_list = []
            while True:
                response = self.ser.readlines()
                for line in response:
                    line = line.strip(b'\n').decode('utf8')
                    line = line.strip('\r')
                    if self.verbose:
                        print(line)
                    response_list.append(line)
                break
            return response_list
        except TypeError as e:
            if self.verbose:
                print(e)
            self.close_connection()
        except Exception as f:
            if self.verbose:
                print(f)
            self.close_connection()

    def start_pump(self):
        command = 'start'
        command = self.add_x(command)
        command = self.add_mode(command)
        response = self.send_command(command)
        return response

    def stop_pump(self):
        command = 'stop'
        command = self.add_x(command)
        response = self.send_command(command)
        return response

    def pause_pump(self):
        command = 'pause'
        command = self.add_x(command)
        response = self.send_command(command)
        return response

    def restart_pump(self):
        command = 'restart'
        response = self.send_command(command)
        return response

    def set_units(self, units):
        units_dict = {'mL/min': '0', 'mL/hr': '1', 'μL/min': '2', 'μL/hr': '3'}
        command = 'set units ' + units_dict[units]
        response = self.send_command(command)
        return response

    def set_diameter(self, diameter):
        command = 'set diameter ' + str(diameter)
        response = self.send_command(command)
        return response

    def set_rate(self, rate):
        if isinstance(rate, list):
            # if list of volumes entered, use multi-step command
            command = 'set rate ' + ','.join([str(x) for x in rate])
        else:
            command = 'set rate ' + str(rate)
        response = self.send_command(command)
        return response

    def set_volume(self, volume):
        if isinstance(volume, list):
            # if list of volumes entered, use multi-step command
            command = 'set volume ' + ','.join([str(x) for x in volume])
        else:
            command = 'set volume ' + str(volume)
        response = self.send_command(command)
        return response

    def set_delay(self, delay):
        if isinstance(delay, list):
            # if list of volumes entered, use multi-step command
            command = 'set delay ' + ','.join([str(x) for x in delay])
        else:
            command = 'set delay ' + str(delay)
        response = self.send_command(command)
        return response

    def set_time(self, timer):
        command = 'set time ' + str(timer)
        response = self.send_command(command)
        return response

    def get_parameter_limits(self):
        command = 'read limit parameter'
        response = self.send_command(command)
        return response

    def get_parameters(self):
        command = 'view parameter'
        response = self.send_command(command)
        return response

    def get_displaced_volume(self):
        command = 'dispensed volume'
        response = self.send_command(command)
        return response

    def get_elapsed_time(self):
        command = 'elapsed time'
        response = self.send_command(command)
        return response

    def get_pump_status(self):
        command = 'pump status'
        response = self.send_command(command)
        return response

    def add_mode(self, command):
        if self.mode == 0:
            return command
        else:
            return command + ' ' + str(self.mode - 1)

    def add_x(self, command):
        if self.x == 0:
            return command
        else:
            return str(self.x) + ' ' + command


class Pump(object):
    def __init__(self, port_num, baudrate):
        self.port_num = port_num
        self.baudrate = baudrate
