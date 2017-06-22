from methods import *
from matplotlib.lines import Line2D
import time
import collections as cl

def kernel_1(rssi):
        return -np.min(rssi)
def kernel_2(rssi):
        return -np.max(rssi)
def kernel_3(rssi):
        return -cl.Counter(rssi).most_common()[0][0]

def distanceOfSignalPower(power,pd0=6.0,n=3.65):
        exp = ((pd0-float(power))/(10*n))
        distance = mt.pow(10,exp)
        return float(distance)

def calculate_best_n(kernel, rssiArray,distancesArray,pd0=6.0):
        bestRssi = []
        
        for j,i in enumerate(rssiArray):
                n = 2.0
                brs = kernel(i)
                distancia = distanceOfSignalPower(brs, pd0=pd0, n=n)
                if distancia > distancesArray[j]:
                        while distancia > distancesArray[j]:
                                n += 0.0001
                                distancia = distanceOfSignalPower(brs, pd0=pd0, n=n)
                        bestRssi.append(n)
                else :
                        bestRssi.append(n)      
        return bestRssi

pd0 = -23.0
array = [100, 200,300,400,500,600,700,800,900,1000,1100]
n = 4.0
rssi = []
MinimalN = np.zeros(len(array))
MaximalN = np.zeros(len(array))
for j,i in enumerate(array):
        rssi.append(load_archive("Samples/Measurements/One_To_One/Suspend_-23dbm/{:04d}cm.txt".format(i), cast="int"))
bestis =  calculate_best_n(kernel_3 , rssi, array, pd0=6.0)

print bestis
valores = []
for i in rssi[10]:
        valores.append(distanceOfSignalPower(-i, pd0=6.0, n=max(bestis)))
print np.average(valores), np.std(valores)