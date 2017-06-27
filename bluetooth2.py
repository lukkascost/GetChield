from lib.Devices import bluetooth
import time

macs = ["544A1638145E", "5C313EFE25F4", "5C313EFE5127"] 


bl1 = bluetooth.bluetooth("/dev/ttyAMA0","544A1638145E")
bl1.x , bl1.y = 0,0
bl1.start()
bl2 = bluetooth.bluetooth("/dev/ttyUSB0","544A1638145E")
name = bl2.bluetooth_name()
bl2.start()
bl3 = bluetooth.bluetooth("/dev/ttyUSB1","544A1638145E")
bl3.start()
#print "Conectado em USB0:",bl2.bluetooth_name()
print name
if name.find("BLE3")!=-1:
	print "ok1"
	bl2.x,bl2.y =  11.5,-20.0
	bl3.x,bl3.y = -11.5,-20.0
elif name.find("BLE1")!=-1:
	print "ok2" 
	bl2.x,bl2.y = -11.5,-20.0
	bl3.x,bl3.y =  11.5,-20.0
else: 
	print "ok3" 
	exit()

while True:
        time.sleep(1)
#        print bl1.resBeacon
        if (not bl1.resBeacon is None) and (not bl2.resBeacon is None) : 
                if(not bl3.resBeacon is None):
                        print "beacon 1 rssi:{}\tbeacon 2 rssi: {}\t beacon 3 rssi: {}".format(bl1.resBeacon.rssi,bl2.resBeacon.rssi,bl3.resBeacon.rssi)
