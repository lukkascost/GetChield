import math as mt
import time
import inspect
from threading import Thread
from ..Geometrics.Circle import circle as Circle
from ..Geometrics.Points import point as Point
from serial import Serial


########################################################################
class ibeacon(object):
        """"""
        #----------------------------------------------------------------------
        def __init__(self):
                """Constructor"""
                self.factoryId = None
                self.rssi = 00
                self.uuid = None
                self.minor = None
                self.major = None
                self.mac = None
                self.power = 00
        def set_device_DISI(self,deviceString):
                deviceString = deviceString.split(":")
                self.factoryId  = deviceString[0]
                self.uuid  = deviceString[1]
                self.minor = int(deviceString[2][:4],16)
                self.major = int(deviceString[2][4:8],16)
                self.power = int(deviceString[2][8:],16)
                self.mac = deviceString[3]
                self.rssi = int(deviceString[4][:4])
        def get_distance(self,n=2.0):
                return mt.pow(10, ((6.0-self.rssi)/(10*n)))
        def __str__(self):
                return "ibeacon: {} mac: {} \n\tUUID: {}\n\tmajor {} \tminor {}\tpower {} \n\trssi {}".format(self.factoryId,self.mac, self.uuid, self.major, self.minor, self.power,self.rssi)
                
########################################################################
class bluetooth(Thread):
        """"""
        #----------------------------------------------------------------------
        def __init__(self,port,mac,baud = 115200, timeout = 0.1):
                """Constructor"""
                Thread.__init__(self)
                self.port = port
                self.baud = baud
                self.timeout = timeout
                self.serialPort = Serial(port, baud, timeout=timeout)
                self.searchmac = mac
                self.resBeacon = ibeacon()
		self.circle = None
	def set_point(self, x, y,radius=1100):
		""""""
		self.circle = Circle(Point(x, y), radius)
        def connect(self):
                if (self.serialPort.isOpen() == False):
                        self.serialPort.open()
                self.serialPort.flushInput()
                self.serialPort.flushOutput()   
                return self.send("AT").find("OK")
	def bluetooth_name(self):
		return self.send("AT+NAME?").replace("OK+NAME:","")
        def search_Ibeacons(self):
                inStr = ''
                if self.connect() == -1: return [-1]
                self.serialPort.write("AT+DISI?")
                while (inStr.find("DISCE") == -1):
                        inStr += self.serialPort.readline()
                quebrado = inStr.split("OK+DISC:")
                quebrado = quebrado[1:]
                if quebrado == []: return [-1]
                for j,i in enumerate(quebrado):
                        bl0 = ibeacon()
                        bl0.set_device_DISI(quebrado[j])
                        quebrado[j] = quebrado[j].replace("OK+DISCE","")
                        quebrado[j] = bl0                
                return quebrado
        def search_Ibeacons_mac(self,mac):
                inStr = ''
                start = time.time()                
                if self.connect() == -1: return [-1]
                self.serialPort.write("AT+DISI?")
                while (inStr.find(mac) == -1):
                        inStr += self.serialPort.readline()
                        if (time.time()-start > 7.0): return "Timeout Exception!"
                        if (inStr.find("DISCE")!=-1): 
                                inStr = ""
                                self.serialPort.write("AT+DISI?")
                quebrado = inStr.split("OK+DISC:")
                quebrado = quebrado[1:]
                if quebrado == []: return "Point not found!"
                for j,i in enumerate(quebrado):
                        bl0 = ibeacon()
                        bl0.set_device_DISI(quebrado[j])
                        quebrado[j] = quebrado[j].replace("OK+DISCE","")
                        quebrado[j] = bl0                                
                beacons = quebrado
                for i in beacons:
                        if i.mac == mac: return i
                return "Point not Found!"
        def run(self):
                while True:
                        beacon = self.search_Ibeacons_mac(self.searchmac)
                        if isinstance(beacon,ibeacon) :
                                self.resBeacon = beacon
                        else: 
                                print beacon 
        def get_resbeacon(self): return self.resBeacon
        def send(self, command):
                inStr = ''
                start = time.time()
                self.serialPort.write(command)
                while (inStr.find("OK") == -1):
                        inStr += self.serialPort.readline()
                        if time.time()-start >=2:
                                break
                return inStr            
        def join(self):
                Thread.join(self)
                return "Deu certo"        
