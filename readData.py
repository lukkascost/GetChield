#!/usr/bin/env python
import time
import serial
ser = serial.Serial(              
               port='/dev/serial0',
               baudrate = 9600,
               timeout=0.5
           )
counter=0
while 1:
	x=ser.readline()
	print x
