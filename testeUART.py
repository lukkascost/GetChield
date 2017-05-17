from serial import Serial
import time

serialPort = Serial("/dev/ttyS0", 9600, timeout=2.0)	
if (serialPort.isOpen() == False):
    serialPort.open()
serialPort.flushInput()
serialPort.flushOutput()

while(1==1):
<<<<<<< HEAD
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
=======
    outStr = raw_input('COMANDO: ')
    inStr = ''
>>>>>>> d1f5562807ec512e6abd4bcd92be8af9c9a99d79


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

