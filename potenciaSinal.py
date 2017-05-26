# -*- coding: cp1252 -*-
from math import *
potencias = [-x for x in range(1,110) ]
pl0 = [ -x for x in potencias]
pd0 = 6
n = 4
def distanciaPotenciaSinal(potencias, qtd, pd0, n):
    for i in range (0, qtd):
        expoente = ((pd0-potencias[i])/(10*n))
        print expoente, potencias[i]
        distance = pow(10, expoente)
        mts = distance/100
        print "DISTANCIA {:03.08f} \t\tPOTENCIA {:03d}".format(float(mts),potencias[i])



distanciaPotenciaSinal(potencias, len(potencias),pd0, n)

    
