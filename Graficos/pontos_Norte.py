import matplotlib.pyplot as plt
import sys 
import os
sys.path.append(os.path.abspath(".."))
from lib.Geometrics.Circle import *
from lib.Geometrics.Points import *
from lib.TestClasses.Trilateration import *
from Classes import *
import  math as mt

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
data.load_archive("../Samples/Measurements/Tree_To_One/blackboard/d50/2m_090g.txt")
erroMedio = 0
quantidade = 0
resultados = np.zeros(100)
for j,i in enumerate(data.data):
        fig, ax = plt.subplots()
        c1 = circle(point(data.locate1, 0), distanceOfSignalPower(i[0])*100)
        c2 = circle(point(data.locate2, -43.3), distanceOfSignalPower(i[1])*100)
        c3 = circle(point(data.locate3, -43.3), distanceOfSignalPower(i[2])*100)
        distancia =  min([c1.radius,c2.radius,c3.radius])
        erroMedio += abs(distancia-100)
        quantidade+=1
        pontos = []
        pontos.append(get_two_circles_intersecting_points(c1,c2))
        pontos.append(get_two_circles_intersecting_points(c1,c3))                       
        pontos.append(get_two_circles_intersecting_points(c2,c3)) 
        cont = 0
        for p in get_all_intersecting_points([c1,c2,c3]):
                if is_contained_in_circles(p,[c1,c2,c3]):
                        cont+=1
                        rad = mt.atan2(p.y,p.x)
                        radian = int(rad*(180/mt.pi))	
                        if radian <0:
                                radian += 360
                        if (radian >337.5 and radian <=360.0) or (radian>=0.0 and radian<=22.5):
                                string = "DIR"#Leste
                        elif (radian >22.5 and radian<=67.5):
                                string = "DIR"#NORDESTE
                        elif (radian >67.5 and radian<=112.5):
                                string = "FRENTE"#NORTE
                        elif (radian >112.5 and radian<=157.5):
                                string = "ESQ"#NOROESTE
                        elif (radian >157.5 and radian<=202.5):
                                string = "ESQ"#OESTE
                        elif (radian >202.5 and radian<=247.5):
                                string = "ESQ"#SUDOESTE
                        elif (radian >247.5 and radian<=292.5):
                                string = "TRAS"#SUL
                        elif (radian >292.5 and radian<=337.5):
                                string = "DIR"#SUDESTE
                        resultados[j] = radian
        otrila = trilateration_beacons()
        otrila.append(c1)
        otrila.append(c2)
        otrila.append(c3)        
print resultados