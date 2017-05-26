import matplotlib.pyplot as plt
import numpy as np
valors = np.zeros((10,1000))
for i in range(0,10):
    arquivo = open("Medicoes/{:01.1f}Metro.txt".format(float(i+1)/10))
    print "Medicoes/{:01.1f}Metro.txt".format(float(i+1)/10)
    for j,k in enumerate(arquivo):
        if j == 999: break
        valors[i,j] = int(k)
    arquivo.close()
    print "ok"
distancias = [float(x)/10 for x in range(1,11)]
medias = [np.average(x) for x in valors]
stDevian = [np.std(x) for x in valors]

print distancias
print medias
print stDevian
plt.plot(distancias,medias,label="Media")
plt.plot(distancias,np.add(medias,stDevian), label="Med + std")
plt.plot(distancias,np.subtract(medias,stDevian), label="Med - std")
plt.grid(True)
plt.show()