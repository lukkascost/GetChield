# -*- coding: cp1252 -*-
from math import *
from serial import Serial
import time
import numpy as np
measurements = [] 
potencias = [-x for x in range(1,110) ]
pl0 = [ -x for x in potencias]
pd0 = 6
n = 3.6
def distanciaPotenciaSinal(potencias, qtd, pd0, n):
    res = []
    for i in range (0, qtd):
        expoente = ((pd0-potencias[i])/(10*n))
        distance = pow(10, expoente)
        mts = distance/100
        res.append(mts)
    return res
while(n<3.8):
	distances = distanciaPotenciaSinal(potencias, len(potencias),pd0, n)
	arquivo = open("1Metro.txt", mode='r')
	real = []
	distancia= []
	for line in arquivo:
    		for j in line.split(","):
			real.append(int(j))
			distancia.append(distances[int(j)])
	arquivo.close()
	real = np.array(real)
	distancia = np.array(distancia)
	print np.average(distancia), np.std(distancia), n
	n = n+0.001
