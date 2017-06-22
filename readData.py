#!/usr/bin/env python
import time
import serial
ser = serial.Serial(              
               port='/dev/ttyUSB0',
               baudrate = 9600,
               timeout=0.2
           )
counter=0
while 1:
	x=ser.readline()
	print x
