from methods import *
pd0 = 6.0
n = 4.0
MinimalN = np.zeros(10)
MaximalN = np.zeros(10)
for j,i in enumerate([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.9,1.0]):
        medStd = 0
        n = 4
        values = np.array(load_archive("Medicoes/{}Metro.txt".format(i), cast="int"))
        while(medStd<i):
                resultado = distanceOfSignalPower(np.average(values),pd0=pd0, n=n)
                devian = distanceOfSignalPower(np.std(values), pd0=pd0, n=n)
                medStd = resultado-devian
                MinimalN[j] = n
                n-=0.001
        #print MinimalN[j], medStd
        
for j,i in enumerate([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.9,1.0]):
        medStd = 10000
        n = 2
        values = np.array(load_archive("Medicoes/{}Metro.txt".format(i), cast="int"))
        while(medStd>i):
                resultado = distanceOfSignalPower(np.average(values),pd0=pd0, n=n)
                devian = distanceOfSignalPower(np.std(values), pd0=pd0, n=n)
                medStd = resultado+devian
                MaximalN[j] = n
                n+=0.001
conjuntos = []
for i in range(10):
        conjuntos.append([])
        atual = MinimalN[i]
        while(atual<=MaximalN[i]):
                conjuntos[i].append(round(float(atual),3))
                atual+=0.001
bestn = []
n = 2.0
while(n<4.0):
        adiciona = True
        for i in range(10):
                if n not in conjuntos[i]:
                        print n," nao esta em ", conjuntos[i]
                        adiciona = False
        if adiciona: bestn.append(n)
        n+=0.001
        
print bestn