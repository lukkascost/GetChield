import matplotlib.pyplot as plt
import numpy as np
valors = np.zeros((4,999))
for h,i in enumerate([9,19,29,42]):
    arquivo = open("Medicoes/{:01.1f}Metro.txt".format(float(i+1)/10))
    print "Medicoes/{:01.1f}Metro.txt".format(float(i+1)/10)
    for j,k in enumerate(arquivo):
        if j == 999: break
        valors[h,j] = int(k)
    arquivo.close()
    print "ok"
distancias = [float(x)/10 for x in [10,20,30,43]]


medias = [np.average(x) for x in valors]
stDevian = [np.std(x) for x in valors]
maximo = [np.max(x) for x in valors]
minimo = [np.min(x) for x in valors]

print valors
plt.plot(distancias,maximo, label="max - std")
plt.plot(distancias,minimo, label="max - std")
plt.grid(True)
plt.show()
