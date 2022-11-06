import time

from test_copy_pump_0830 import Pump

chemyx_1 = Pump(6, 38400)
chemyx_1.Open_Connection()
chemyx_1.Set_volume(20)
chemyx_1.Set_ID(22.03)
chemyx_1.Set_rate(1)

rate_li = [0.01, 0.5]

while True:

    # chemyx_1.Set_volume("1,-5")
    # chemyx_1.Set_rate("1,5")

    chemyx_1.Set_volume(-20)
    chemyx_1.Set_rate(5)
    chemyx_1.Start()
    time.sleep(10)
    chemyx_1.Stop()

    chemyx_1.Set_volume(20)
    chemyx_1.Set_rate(5)
    chemyx_1.Start()
    time.sleep(10)
    chemyx_1.Stop()
#
# chemyx_1.Set_volume(-20)
# chemyx_1.Set_rate(5)
# chemyx_1.Start()
# time.sleep(5)
# chemyx_1.Stop()