# -*- coding: cp1252 -*-
from math import *
potencias = [-x for x in range(1,110) ]
pl0 = [ -x for x in potencias]
pd0 = -23
n = 2.5

def distanciaPotenciaSinal(potencias, qtd, pd0, n):
    for i in range (0, qtd):
        expoente = ((pd0-potencias[i])/(10*n))
        distance = pow(10, expoente)
        res = distance
        print "DISTANCIA {:03.08f} \t\tPOTENCIA {:03d}".format(float(res),potencias[i])



distanciaPotenciaSinal(potencias, len(potencias),pd0, n)

    
