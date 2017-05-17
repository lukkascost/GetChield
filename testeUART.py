from serial import Serial
import time

serialPort = Serial("/dev/ttyS0", 9600, timeout=2.0)	
if (serialPort.isOpen() == False):
    serialPort.open()
serialPort.flushInput()
serialPort.flushOutput()

while(1==1):
	outStr = raw_input('COMANDO: ')
	inStr = ''
	while (inStr is ""):
	    serialPort.write(outStr)
	    time.sleep(0.05)
	    inStr = serialPort.read(serialPort.inWaiting())
	    
	    print "inStr =  " + inStr
	    print "outStr = " + outStr
	
	    if(inStr is not ""):
	        print "WORKED! "
		break
	    else:
	        print "failed"

serialPort.close()

