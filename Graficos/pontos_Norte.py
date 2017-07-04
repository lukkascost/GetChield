import matplotlib.pyplot as plt
import sys 
import os
sys.path.append(os.path.abspath(".."))
from lib.Geometrics.Circle import *
from lib.Geometrics.Points import *
from lib.TestClasses.Trilateration import *
from Classes import *

class dataStore(object):
        def __init__(self):
                self.data = []
                self.locate1 = 0
                self.locate2 = 0
                self.locate3 = 0
        def load_archive(self, path):
                for f in  open(path, mode="r").readlines():
                        f = f.split(",")
                        self.data.append([float(f[0]),float(f[1]),float(f[2])])
                self.locate1 = self.data[0][0]
                self.locate2 = self.data[0][1]
                self.locate3 = self.data[0][2]
                del self.data[0]
        def __str__(self):
                string = ""
                string += "Posx1:{:03.3f}\tPosx2:{:03.3f}\tPosx3:{:03.3f}\n".format(self.locate1,self.locate2,self.locate3)
                for i in self.data:
                        string += "Rssi1:{:03.2f}\tRssi2:{:03.2f}\tRssi3:{:03.2f}\n".format(i[0],i[1],i[2])
                return string
        

data = dataStore()
data.load_archive("../Samples/Measurements/Tree_To_One/blackboard/d25/1m_090g.txt")
erroMedio = 0
quantidade = 0
for i in data.data:
        fig, ax = plt.subplots()
        c1 = circle(point(data.locate1, 0), distanceOfSignalPower(i[0])*100)
        c2 = circle(point(data.locate2, -21.6), distanceOfSignalPower(i[1])*100)
        c3 = circle(point(data.locate3, -21.6), distanceOfSignalPower(i[2])*100)
        distancia =  min([c1.radius,c2.radius,c3.radius])
        erroMedio += abs(distancia-100)
        quantidade+=1
        
        otrila = trilateration_beacons()
        otrila.append(c1)
        otrila.append(c2)
        otrila.append(c3)        
        otrila.appendToAx(ax)
        plt.scatter(0,100,label="ponto real")
        ax.legend()
        ax.grid(1)
        plt.xlim([-400,400])
        plt.ylim([-400,400])        
        plt.show()
        
print erroMedio/quantidade