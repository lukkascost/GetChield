from lib.Devices import bluetooth
from lib.Geometrics.Circle import * 
from Classes import *
import math as mt
from datetime import datetime
import time

macs = ["544A1638145E", "5C313EFE25F4", "5C313EFE5127"] 
search_mac = "544A1638145E" #HM-10
#search_mac = "F75DEAB95758" #EST VERDE
#search_mac = "DBEE5864CDF2" #EST AZUL
#search_mac = "DBEE5864CDF2" #kontact
#search_mac = "B0481AC1361E" #Iphone lucas
#search_mac = "F079602AD48F" # MACBOOK


bl1 = bluetooth.bluetooth("/dev/ttyAMA0",search_mac)
bl1.set_point(0.0,0.0)
bl1.start()
bl2 = bluetooth.bluetooth("/dev/ttyUSB0",search_mac)
name = bl2.bluetooth_name()
bl2.start()
bl3 = bluetooth.bluetooth("/dev/ttyUSB1",search_mac)
bl3.start()

bl4 = bluetooth.bluetooth("/dev/ttyACM0",search_mac)

print name
if name.find("BLE3")!=-1:
	bl2.set_point(12.5,-21.8)
	bl3.set_point(-12.5,-21.8)
elif name.find("BLE1")!=-1:
	bl2.set_point(-12.5,-21.8)
	bl3.set_point(12.5,-21.8)
else: 
	exit()
while(True):
	pontos = []
	radian = 0
	string = ""
	while string=="":
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
	
	
	
	date = datetime.now()
	d1  = int(d1.radius)
	d2  = int(d2.radius)
	d3  = int(d3.radius)
	angulo = radian
	print d1,d2,d3
	
	print date
	
	year = date.year/100
	year = year*100
	year = date.year - year
	print year
	
		
	day =       "{0:05b}".format(date.day)
	month =     "{0:04b}".format(date.month)
	year =      "{0:07b}".format(year)
	hour =      "{0:05b}".format(date.hour)
	minute =    "{0:06b}".format(date.minute)
	distance1 = "{0:04b}".format(d1/100)
	distance2 = "{0:04b}".format(d2/100)
	distance3 = "{0:04b}".format(d3/100)
	angle =     "{0:09b}".format(angulo)
	
	
	stringBit =  day+month+year+hour+minute+distance1+distance2+distance3+angle
	print stringBit
	print day,month,year,hour,minute,distance1,distance2,distance3,angle
	print hex(int(stringBit,2))[-12:].upper()
	
	
	bl4.send("1\n")
	time.sleep(1)
	bl4.send("22\n")
	time.sleep(1)
	bl4.send("4\n")
	time.sleep(1)
	bl4.send(hex(int(stringBit,2))[-12:].upper() + "\n")
	time.sleep(1)
