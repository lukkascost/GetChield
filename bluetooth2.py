from lib.Devices import bluetooth
from lib.Geometrics.Circle import * 
from Classes import *
import math as mt
import time

macs = ["544A1638145E", "5C313EFE25F4", "5C313EFE5127"] 


bl1 = bluetooth.bluetooth("/dev/ttyAMA0","544A1638145E")
bl1.set_point(0.0,0.0)
bl1.start()
bl2 = bluetooth.bluetooth("/dev/ttyUSB0","544A1638145E")
name = bl2.bluetooth_name()
bl2.start()
bl3 = bluetooth.bluetooth("/dev/ttyUSB1","544A1638145E")
bl3.start()
print name
if name.find("BLE3")!=-1:
	bl2.set_point(12.5,-21.8)
	bl3.set_point(-12.5,-21.8)
elif name.find("BLE1")!=-1:
	bl2.set_point(-12.5,-21.8)
	bl3.set_point(12.5,-21.8)
else: 
	exit()

pontos = []
radian = 0
string = ""
while True:
	time.sleep(1)
	d1 = circle(bl1.circle.center, distanceOfSignalPower(bl1.resBeacon.rssi, n=2.75)*100) 
	d2 = circle(bl2.circle.center, distanceOfSignalPower(bl2.resBeacon.rssi, n=2.75)*100) 
	d3 = circle(bl3.circle.center, distanceOfSignalPower(bl3.resBeacon.rssi, n=2.75)*100) 
	anterior = bl1.circle.center
	cont = 0
	for p in get_all_intersecting_points([d1,d2,d3]):
		if is_contained_in_circles(p,[d1,d2,d3]):
			cont+=1
			rad = mt.atan2(p.y,p.x)
			radian = int(rad*(180/mt.pi))	
			if radian <0:
				radian += 360
			if (radian >337.5 and radian <=360.0) or (radian>=0.0 and radian<=22.5):
				string = "DIR"#Leste
			elif (radian >22.5 and radian<=67.5):
				string = "DIR"#NORDESTE
			elif (radian >67.5 and radian<=112.5):
				string = "FRENTE"#NORTE
			elif (radian >112.5 and radian<=157.5):
				string = "ESQ"#NOROESTE
			elif (radian >157.5 and radian<=202.5):
				string = "ESQ"#OESTE
			elif (radian >202.5 and radian<=247.5):
				string = "ESQ"#SUDOESTE
			elif (radian >247.5 and radian<=292.5):
				string = "TRAS"#SUL
			elif (radian >292.5 and radian<=337.5):
				string = "DIR"#SUDESTE
			print radian,cont,string
			
	#pontos.append((str(anterior),string,radian))
	#print pontos
	#print "beacon 1 rssi:{}\tbeacon 2 rssi: {}\t beacon 3 rssi: {}".format(bl1.resBeacon.rssi,bl2.resBeacon.rssi,bl3.resBeacon.rssi)
			
