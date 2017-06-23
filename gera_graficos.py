import matplotlib.pyplot as plt
import numpy as np
from Classes import *
valors = np.zeros((1,800))
for h,i in enumerate([0]):
    arquivo = open("{}m.txt".format((i+1)))
    for j,k in enumerate(arquivo):
        if j == 800: break
        valors[h,j] = int(k)
    arquivo.close()
distancias = [float(x) for x in [1]]

valors = np.multiply(valors, -1)   
medias = [np.average(x) for x in valors]
stDevian = [np.std(x) for x in valors]
maximo = [np.max(x) for x in valors]
minimo = [np.min(x) for x in valors]

maximo = np.multiply(maximo, -1)
minimo = np.multiply(minimo, -1)
medias = np.multiply(medias, -1)

medi = np.zeros((11,2))
for k,g in enumerate(valors[0]):
    if(g>=48 and g<=55):
        medi[0,0]+=g
        medi[0,1]+=1
print "media de 1 metro entre 18 e 25: ", distanceOfSignalPower(medi[0,0]/medi[0,1], n=2.7), medi[0,1]   
for j in range(1):
    print "Medias para {} centimentros.".format((j+1)*100)
    for i in range(1,11):
        print "\tmedia {:02d}: {:04.04f} distancia: {:04.04f}".format(i,np.average(valors[j,(i-1)*100:i*100]), distanceOfSignalPower(np.average(valors[j,(i-1)*100:i*100]),n=2.7,pd0=6.0))

#print valors
#print minimo
#print maximo
#print medias
#print stDevian
plt.scatter([x for x in range(800)],valors[0], label="pontos")
#plt.plot(distancias,maximo, label="maximo")
#plt.plot(distancias,medias, label="media")
#plt.plot(distancias,minimo, label="minimo")
plt.grid(True)
plt.legend()
plt.show()
