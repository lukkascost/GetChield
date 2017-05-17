import serial
ser = serial.Serial('/dev/ttyS0',baudrate = 9600, parity = serial.PARITY_NONE, timeout=0.2)	
print ser.isOpen()
ser.write('AT+NAME')
data = ser.read(0)
print data
