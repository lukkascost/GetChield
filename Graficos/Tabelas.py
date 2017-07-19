import matplotlib.pyplot as plt
import sys 
import os
sys.path.append(os.path.abspath(".."))
from lib.Geometrics.Circle import *
from lib.Geometrics.Points import *
from lib.TestClasses.Trilateration import *
from Classes import *
import  math as mt
import copy as cp


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

fig, ax = plt.subplots()
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
ponderada = [-43.240833333333335, -51.151666666666664, -49.806666666666665, -56.199166666666663, -55.019166666666663, -54.225833333333334, -56.052500000000002, -54.383333333333333, -57.975833333333334, -61.126666666666665]
mediana50 = [np.average(np.sort(x)[mediana-25:mediana+25]) for x in valors]
desvios50mediana = [np.std(np.sort(x)[mediana-25:mediana+25]) for x in valors]


#plt.subplot(212)
toPlot = medias
#toPlot = mediana50
#toPlot = medias50m
#toPlot = medias50p
#toPlot = ponderada

buscado = -70
x, y = np.array([x for x in range(1,11)]), np.array(toPlot)
z = np.polyfit(x,y,4)
p = np.poly1d(z)
print p
p2 = np.poly1d([-0.1105,2.7307,-22.9094,-21.0808])
xp = np.linspace(-1,11,100)
plt.plot(xp,p(xp),label = "Equacao nossa")
#plt.plot(xp,p2(xp),label = "Equacao do artigo")
#plt.title("dados do experimento 1")
plt.scatter([x for x in range(1,11)],toPlot)
#plt.legend()
plt.xlabel("Distance (m)")
plt.ylabel("RSSI (dbm)")
plt.grid()
plt.show()
distances = np.zeros(100)
x = 0
while(x>-100):
        controle = -3
        while(p(controle)>x):controle+=0.01
        distances[abs(x)] = controle
        x-=1
rmse = []
for k in range(10):
        distancias1m = []
        for i in valors[k]:
                distancias1m.append(((k+1)-distances[abs(int(i))])**2 )
        rmse += [np.sqrt(np.mean(distancias1m))]
for i in rmse:
        print "{:03.04f}".format(i)
#for i,j in enumerate(medias):
        #print "{:02d}\t{:03.04f}\t±{:03.04f}\t{:03.04f}\t±{:03.04f}\t{:03.04f}\t±{:03.04f}\t{:03.04f}\t±{:03.04f}\t{:03.04f}".format(i+1,medias[i],desvios[i],medias50m[i],desvios50m[i],medias50p[i],desvios50p[i],mediana50[i],desvios50mediana[i],ponderada[i])


### Segunda massa de dados: 
#valors = []
#for k in range(5):
        #valors.append([])
        #for i in [0,45,90,135,180,225,270,315]:
                #data = dataStore()
                #data.load_archive("../Samples/Measurements/Tree_To_One/blackboard/d25/{:d}m_{:03d}g.txt".format(k+1,i))
                #for j in np.matrix(data.data)[:,0]:
                        #valors[k].append(j[0,0])
#valors = np.array(valors)

#print "Valores da segunda coleta de dados"
#mediana  = valors.shape[1]/2
#medias  = [np.average(x) for x in valors]
#desvios = [np.std(x) for x in valors]
#medias50p = [np.average(np.sort(x)[:50]) for x in valors]
#medias50m = [np.average(np.sort(x)[-50:]) for x in valors]
#desvios50p = [np.std(np.sort(x)[:50]) for x in valors]
#desvios50m = [np.std(np.sort(x)[-50:]) for x in valors]


#mediana50 = [np.average(np.sort(x)[mediana-25:mediana+25]) for x in valors]
#desvios50mediana = [np.std(np.sort(x)[mediana-25:mediana+25]) for x in valors]

##for i,j in enumerate(medias):
        ##print "{:02d}\t{:03.04f}\t±{:03.04f}\t{:03.04f}\t±{:03.04f}\t{:03.04f}\t±{:03.04f}\t{:03.04f}\t±{:03.04f}\t{:03.04f}".format(i+1,medias[i],desvios[i],medias50m[i],desvios50m[i],medias50p[i],desvios50p[i],mediana50[i],desvios50mediana[i],ponderada[i])


#toPlot = medias
##toPlot = mediana50
##toPlot = medias50m
##toPlot = medias50p
##toPlot = ponderada
#plt.subplot(221)

#x, y = np.array([x for x in range(1,6)]), np.array(toPlot)
#z = np.polyfit(x,y,3)
#p = np.poly1d(z)
#xp = np.linspace(0,11,100)
#p2 = np.poly1d([-0.1105,2.7307,-22.9094,-21.0808])
#plt.plot(xp,p(xp),label = "Equacao nossa")
#plt.plot(xp,p2(xp),label = "Equacao do artigo")
#plt.title("dados do experimento 2 D25")
#plt.scatter([x for x in range(1,6)],toPlot)
#plt.grid()
#plt.legend()
#plt.show()


#distances = np.zeros(100)
#x = 0
#while(x>-100):
        #controle = -3
        #while(p(controle)>x):controle+=0.01
        #distances[abs(x)] = controle
        #x-=1
#rmse = []
#for k in range(5):
        #distancias1m = []
        #for i in valors[k]:
                #distancias1m.append(((k+1)-distances[abs(int(i))])**2 )
        #rmse += [np.sqrt(np.mean(distancias1m))]
#for i in rmse:
        #print "{:03.04f}".format(i)

#print "Valores da Terceira coleta de dados"
#mediana  = valors.shape[1]/2
#medias  = [np.average(x) for x in valors]
#desvios = [np.std(x) for x in valors]
#medias50p = [np.average(np.sort(x)[:50]) for x in valors]
#medias50m = [np.average(np.sort(x)[-50:]) for x in valors]
#desvios50p = [np.std(np.sort(x)[:50]) for x in valors]
#desvios50m = [np.std(np.sort(x)[-50:]) for x in valors]


#mediana50 = [np.average(np.sort(x)[mediana-25:mediana+25]) for x in valors]
#desvios50mediana = [np.std(np.sort(x)[mediana-25:mediana+25]) for x in valors]

#for i,j in enumerate(medias):
        #print "{:02d}\t{:03.04f}\t±{:03.04f}\t{:03.04f}\t±{:03.04f}\t{:03.04f}\t±{:03.04f}\t{:03.04f}\t±{:03.04f}\t{:03.04f}".format(i+1,medias[i],desvios[i],medias50m[i],desvios50m[i],medias50p[i],desvios50p[i],mediana50[i],desvios50mediana[i],ponderada[i])


#toPlot = medias
##toPlot = mediana50
##toPlot = medias50m
##toPlot = medias50p
##toPlot = ponderada
#plt.subplot(222)

#x, y = np.array([x for x in range(1,6)]), np.array(toPlot)
#z = np.polyfit(x,y,4)
#p = np.poly1d(z)
#xp = np.linspace(0,11,100)
#p2 = np.poly1d([-0.1105,2.7307,-22.9094,-21.0808])
#plt.plot(xp,p(xp),label = "Equacao nossa")
#plt.plot(xp,p2(xp),label = "Equacao do artigo")
#plt.title("dados do experimento 2 D50")
#plt.scatter([x for x in range(1,6)],toPlot)
#plt.grid()
#plt.legend()


#plt.show()
