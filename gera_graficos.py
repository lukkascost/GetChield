import matplotlib.pyplot as plt
import numpy as np
valors = np.zeros((11,999))
for h,i in enumerate([99,199,299,399,499,599,699,799,899,999,1099]):
    arquivo = open("Samples/Measurements/One_To_One/Suspend/{:04d}cm.txt".format((i+1)))
    print "Samples/Measurements/One_To_One/Suspend/{:04d}cm.txt".format((i+1))
    for j,k in enumerate(arquivo):
        if j == 999: break
        valors[h,j] = int(k)
    arquivo.close()
    print "ok"
distancias = [float(x) for x in [100,200,300,400,500,600,700,800,900,1000,1100]]


medias = [np.average(x) for x in valors]
stDevian = [np.std(x) for x in valors]
maximo = [np.max(x) for x in valors]
minimo = [np.min(x) for x in valors]

print valors
plt.plot(distancias,maximo, label="max - std")
plt.plot(distancias,medias, label="media")
plt.plot(distancias,minimo, label="max - std")
plt.grid(True)
plt.show()
