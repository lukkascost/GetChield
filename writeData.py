#!/usr/bin/env python         
import time
import serial
ser = serial.Serial(port='/dev/ttyUSB0',
               baudrate =9600 ,
               parity=serial.PARITY_NONE,
               timeout=1)
counter=0
while 1:
	print counter
	ser.write("AT+DISI?")
	time.sleep(5)
	counter += 1
