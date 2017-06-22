from serial import Serial
import time
macs = ["544A1638145E", "5C313EFE25F4", "5C313EFE5127"] 
bl1 = Serial("/dev/ttyAMA0", 9600, timeout=2.0)
bl2 = Serial("/dev/ttyUSB0", 9600, timeout=2.0)
if (bl1.isOpen() == False):
        bl1.open()
bl1.flushInput()
bl1.flushOutput()
if (bl2.isOpen() == False):
        bl2.open()
bl2.flushInput()
bl2.flushOutput()

time.sleep(0.2)

def enviaCommando(command, serial): 
        inStr = ''
        while (inStr is ""):
                serial.write(command)
                time.sleep(0.05)
                inStr = serial.read(serial.inWaiting())
        
                if(inStr is not ""):
                        print "Resultado: {}".format(inStr)
                        break
                else:
                        pass
print "Conectando bl1..."
enviaCommando("AT+CON{}".format(macs[0]), serial)
enviaCommando("AT+CLEAR".format(macs[0]), serial)
print "Conectando bl2..."
enviaCommando("AT+RSSI?".format(macs[2]), serial)
enviaCommando("AT+CON{}".format(macs[2]), serial)
enviaCommando("AT+CLEAR".format(macs[2]), serial)
print "Conectando bl3..."



