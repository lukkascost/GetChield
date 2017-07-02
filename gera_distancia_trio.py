from lib.Devices.bluetooth import bluetooth,ibeacon


bl1 = bluetooth("/dev/ttyAMA0","544A1638145E")
bl1.set_point(0, 0)     
bl2 = bluetooth("/dev/ttyUSB0","544A1638145E")
name = bl2.bluetooth_name()
bl3 = bluetooth("/dev/ttyUSB1","544A1638145E")
if name.find("BLE3")!=-1:
        bl2.set_point(12.5,-21.6)
        bl3.set_point(-12.5,-21.6)
elif name.find("BLE1")!=-1:
        bl2.set_point(-12.5,-21.6)
        bl3.set_point(12.5,-21.6)
else: 
        exit()

with open("Samples/Measurements/Tree_To_One/blackboard/d25/5m_225g.txt", mode='w') as f:
        f.write("{},{},{}\n".format(bl1.circle.center.x,bl2.circle.center.x,bl3.circle.center.x))
cont = 0
while(cont<70):
	save = 1
	print cont,1
        beacon = bl1.search_Ibeacons_mac(bl1.searchmac)
        if isinstance(beacon,ibeacon) :
                bl1.resBeacon = beacon
        else: 
                save = 0         
        print cont,2
        beacon = bl2.search_Ibeacons_mac(bl2.searchmac)
        if isinstance(beacon,ibeacon) :
                bl2.resBeacon = beacon
        else: 
                save = 0                         
        print cont,3
        beacon = bl3.search_Ibeacons_mac(bl3.searchmac)
        if isinstance(beacon,ibeacon) :
                bl3.resBeacon = beacon
        else: 
                save = 0         
        if save == 1:
		cont = cont + 1
		print bl1.resBeacon.rssi,bl2.resBeacon.rssi,bl3.resBeacon.rssi
                with open("Samples/Measurements/Tree_To_One/blackboard/d25/5m_225g.txt", mode='a') as f:
                        f.write("{},{},{}\n".format(bl1.resBeacon.rssi,bl2.resBeacon.rssi,bl3.resBeacon.rssi))
        
