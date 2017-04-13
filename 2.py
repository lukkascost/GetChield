import serial
import time

def readlineCR(port):
    rv = ""
    while True:
        ch = port.read()
        rv += ch
        if ch=='\r' or ch=='':
            return rv

port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3.0)

while True:
    port.write("AT+RENEW")
    rcv = readlineCR(port)
    port.write("\r\nYou sent:" + repr(rcv))
    print rcv
