from lib.Devices.bluetooth import bluetooth,ibeacon


bl1 = bluetooth("/dev/ttyAMA0","544A1638145E")
bl1.set_point(0, 0)     
bl2 = bluetooth("/dev/ttyUSB0","544A1638145E")
name = bl2.bluetooth_name()
bl3 = bluetooth("/dev/ttyUSB1","544A1638145E")
if name.find("BLE3")!=-1:
        bl2.set_point(11.5,-20.0)
        bl3.set_point(-11.5,-20.0)
elif name.find("BLE1")!=-1:
        bl2.set_point(-11.5,-20.0)
        bl3.set_point(11.5,-20.0)
else: 
        exit()

with open("Samples/Measurements/Tree_To_One/blackboard/d25/1m.txt", mode='w') as f:
        f.write("{},{},{}\n".format(bl1.circle.center.x,bl2.circle.center.x,bl3.circle.center.x))
while(1==1):
        save = 1
        beacon = bl1.search_Ibeacons_mac(bl1.searchmac)
        if isinstance(beacon,ibeacon) :
                bl1.resBeacon = beacon
        else: 
                save = 0         
        beacon = bl2.search_Ibeacons_mac(bl2.searchmac)
        if isinstance(beacon,ibeacon) :
                bl2.resBeacon = beacon
        else: 
                save = 0                         
        beacon = bl3.search_Ibeacons_mac(bl3.searchmac)
        if isinstance(beacon,ibeacon) :
                bl3.resBeacon = beacon
        else: 
                save = 0         
        if save == 1:
                with open("Samples/Measurements/Tree_To_One/blackboard/d25/1m.txt", mode='a') as f:
                        f.write("{},{},{}\n".format(bl1.resBeacon.rssi,bl2.resBeacon.rssi,bl3.resBeacon.rssi))
        