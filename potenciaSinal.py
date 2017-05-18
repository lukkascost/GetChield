# -*- coding: cp1252 -*-
from math import *
potencias = [-x for x in range(1,102) ]
pl0 = [ -x for x in potencias]
pd0 = -30
n = 2.5
def distanciaPotenciaSinal(potencias, qtd, pd0, n):
    for i in range (0, qtd):
        expoente = ((pd0-potencias[i])/(10*n))
        distance = pow(10, expoente)
        mts = distance/100
        print "DISTÂNCIA {:010.10f} \t POTÊNCIA {:03d}".format(mts,potencias[i])



distanciaPotenciaSinal(potencias, len(potencias),pd0, n)

    
