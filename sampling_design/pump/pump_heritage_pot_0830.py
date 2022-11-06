# -*- coding = utf-8 -*-
# @Time : 2020/9/10 16:25
# @Auther : LJ
# @File : Pump.py
# @Software:PyCharm
import time
import serial
import datetime

# from Power import Power
import logging


class Pump(object):
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate

    def open_connection(self):
        self.ser = serial.Serial()
        self.ser.timeout = 2
        self.ser.baudrate = self.baudrate
        self.ser.port = "COM%s" % str(self.port)
        self.ser.open()
        self.ser.flushOutput()
        self.ser.flushInput()

        if self.ser.isOpen():
            print("Open" + self.ser.portstr)
        else:
            print("Failed to connect to pump")
        return self.ser

    def close_connection(self):
        pass

    def communicate_pump(self, ser, message, pumpType):
        self.ser.flushOutput()
        self.ser.flushInput()

        mss = str.encode(message + "\r\n")
        day = datetime.date.today()
        logger = logging.getLogger('Pump_Control_Log')
        logging.basicConfig(filename=r"test_data_file" + "{0}-".format(day.isoformat()) + 'pump_control_log.txt',
                            level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        logger.debug("COM{0} receive '{1}'".format(self.port, message))
        ser.write(mss)
        time.sleep(0.5)
        # while True:
        #     answer = ser.readline()
        #     if len(answer) > 0:
        #         break
        #     # time.sleep(0.1)
        #     print('no answer from pump yet')
        # answer = answer.decode()
        # print('{0} gave {1}'.format(pumpType, answer))

    def start(self):
        self.communicate_pump(self.ser, "start", self.port)
        now = datetime.datetime.now()
        ts = now.strftime('%Y-%m-%d %H:%M:%S')
        print(self.port, ' 泵开始指令已发送:', ts)

    def stop(self):
        self.communicate_pump(self.ser, "stop", self.port)
        now = datetime.datetime.now()
        ts = now.strftime('%Y-%m-%d %H:%M:%S')
        print(self.port, ' 泵停止指令已发送:', ts)

    def set_rate(self, rate):
        self.communicate_pump(self.ser, "set rate %s" % str(rate), self.port)
        now = datetime.datetime.now()
        ts = now.strftime('%Y-%m-%d %H:%M:%S')
        print(self.port, ' Rate=%s指令已发送:' % str(rate), ts)

    def set_id(self, id):
        self.communicate_pump(self.ser, "set diameter %s" % str(id), self.port)
        now = datetime.datetime.now()
        ts = now.strftime('%Y-%m-%d %H:%M:%S')
        print(self.port, ' ID=%s指令已发送:' % str(id), ts)

    def set_volume(self, volume):
        self.communicate_pump(self.ser, "set volume %s" % str(volume), self.port)
        now = datetime.datetime.now()
        ts = now.strftime('%Y-%m-%d %H:%M:%S')
        print(self.port, '  volume=%s指令已发送:' % str(volume), ts)

    def set_time(self, time):
        self.communicate_pump(self.ser, "set time %s" % str(time), self.port)
        now = datetime.datetime.now()
        ts = now.strftime('%Y-%m-%d %H:%M:%S')
        print(self.port, '  time=%s指令已发送:' % str(time), ts)

    def initiate(self, **kwargs):
        # What process does it take to initiate a pump?
        # Port, Baudrate,{volume, id, rate}
        self.volume = kwargs['volume']
        self.id = kwargs['id']
        self.rate = kwargs['rate']

        self.open_connection()
        self.set_volume(volume=self.volume)
        self.set_id(id=self.id)
        self.set_rate(rate=self.rate)

    def set_multi_rate(self, rate_list):
        command = "set rate "
        for i in range(int(len(rate_list) / 2)):
            i = i * 2
            command = command + "{0}/{1},".format(str(rate_list[i]), str(rate_list[i + 1]))

        self.communicate_pump(self.ser, command[:-1], self.port)
        now = datetime.datetime.now()
        ts = now.strftime('%Y-%m-%d %H:%M:%S')
        print(self.port, "  {0}指令已发送: ".format(command[:-1]), ts)

    def set_multi_time(self, Time):
        command = "set time "
        for i in range(int(len(Time))):
            command = command + "{0},".format(str(Time[i]))
        self.communicate_pump(self.ser, command[:-1], self.port)
        now = datetime.datetime.now()
        ts = now.strftime('%Y-%m-%d %H:%M:%S')
        print(self.port, "  {0}指令已发送: ".format(command[:-1]), ts)

    def set_multi_volume(self, volume):
        command = "set volume "
        for i in range(int(len(volume))):
            command = command + "{0},".format(str(volume[i]))
        self.communicate_pump(self.ser, command[:-1], self.port)
        now = datetime.datetime.now()
        ts = now.strftime('%Y-%m-%d %H:%M:%S')
        print(self.port, "  {0}指令已发送: ".format(command[:-1]), ts)

    def set_units(self, unit):
        self.communicate_pump(self.ser, "set volume %s" % str(unit), self.port)
        now = datetime.datetime.now()
        ts = now.strftime('%Y-%m-%d %H:%M:%S')
        print(self.port, '  Unit=%s指令已发送:' % str(unit), ts)


if __name__ == "__main__":
    FusionRed = Pump(5, 38400)
    FusionRed.open_connection()
    # FusionACN = Pump(9, 38400)
    # FusionACN.Open_Connection()
    FusionAM = Pump(11, 38400)
    FusionAM.open_connection()

    FusionRed.set_volume(30)  # 60ml 29.3mm
    FusionRed.set_id(22.03)
    #

    FusionAM.set_volume(30)
    FusionAM.set_id(22.03)
    #

    #
    FusionRed.set_rate(0.01)

    FusionAM.set_rate(0.01)
    FusionAM.start()

    FusionRed.start()
    for i in range(5):
        FusionRed.set_rate(i * 0.1)

        FusionAM.set_rate(i * 0.1)
        time.sleep(10)
    #

    FusionAM.stop()

    FusionRed.stop()

    # FusionCat = Pump(11, 38400)
    # FusionCat.Open_Connection()
    #
    # FusionCat.Set_volume(30)
    # FusionCat.Set_ID(22.03)
    # #
    # FusionCat.Set_rate(0.30)
    #
    # FusionCat.Start()
    # for i in range(4):
    #     FusionCat.Set_rate(0.33+0.01*i)
    #     time.sleep(10)
    # FusionCat.Stop()
    #
