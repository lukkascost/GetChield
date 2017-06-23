from lib.Devices import bluetooth
import time

macs = ["544A1638145E", "5C313EFE25F4", "5C313EFE5127"] 


bl1 = bluetooth.bluetooth("/dev/ttyUSB0","5C313EFE4626")
bl1.start()
#bl2 = bluetooth.bluetooth("/dev/ttyAMA0","5C313EFE4626")
#bl2.start()
while True:
        time.sleep(1)
#        if (not bl1.resBeacon is None) and (not bl2.resBeacon is None) : print "beacon 1 rssi:{} beacon 2 rssi: {}".format(bl1.resBeacon.rssi,bl2.resBeacon.rssi)
