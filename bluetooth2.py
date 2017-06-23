from lib.Devices import bluetooth
import time

macs = ["544A1638145E", "5C313EFE25F4", "5C313EFE5127"] 


bl1 = bluetooth.bluetooth("/dev/tty.usbserial","544A1638145E")
bl1.start()
bl2 = bluetooth.bluetooth("/dev/ttyAMA0","544A1638145E")
bl2.start()
bl3 = bluetooth.bluetooth("/dev/ttyAMA0","544A1638145E")
bl4.start()

while True:
        time.sleep(1)
        print bl1.resBeacon
        if (not bl1.resBeacon is None) and (not bl2.resBeacon is None) : 
                if(not bl3.resBeacon is None):
                        print "beacon 1 rssi:{}\tbeacon 2 rssi: {}\t beacon 3 rssi: {}".format(bl1.resBeacon.rssi,bl2.resBeacon.rssi,bl3.resBeacon)
