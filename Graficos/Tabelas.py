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


valors = np.zeros((10,1200))
for h,i in enumerate([1,2,3,4,5,6,7,8,9,10]):
        arquivo = open("../Samples/Measurements/One_To_One/Suspend_6dbm/{:04d}cm.txt".format(i*100))
        for j,k in enumerate(arquivo):
                if j == 1200: break
                valors[h,j] = -int(k)
        arquivo.close()
distancias = [float(x) for x in [1]]
mediana  = valors.shape[1]/2
medias  = [np.average(x) for x in valors]
desvios = [np.std(x) for x in valors]
medias50p = [np.average(np.sort(x)[:50]) for x in valors]
medias50m = [np.average(np.sort(x)[-50:]) for x in valors]
desvios50p = [np.std(np.sort(x)[:50]) for x in valors]
desvios50m = [np.std(np.sort(x)[-50:]) for x in valors]

mediana50 = [np.average(np.sort(x)[mediana-25:mediana+25]) for x in valors]
desvios50mediana = [np.std(np.sort(x)[mediana-25:mediana+25]) for x in valors]

for i,j in enumerate(medias):
        print "{:02d}\t{:03.04f}\t±{:03.04f}\t{:03.04f}\t±{:03.04f}\t{:03.04f}\t±{:03.04f}\t{:03.04f}\t±{:03.04f}".format(i+1,medias[i],desvios[i],medias50m[i],desvios50m[i],medias50p[i],desvios50p[i],mediana50[i],desvios50mediana[i])
        
        
        ## Segunda massa de dados: 
        
        