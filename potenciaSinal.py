# -*- coding: cp1252 -*-
from math import *
potencias = [-x for x in range(1,102) ]
pl0 = [-7-x for x in potencias]
pt = 0
pd0 = 43.2
d0 = 0.1
n = 1.3
x0 = 5


def distanciaPotenciaSinal(pl0, qtd, pt, pd0, d0, n, x0):
    const1 = (-10)*log(pd0)
    const2 = 10*n*log(d0)
    const3 = const1 + const2 - x0 
    for i in range (0, qtd):
        const4 = const3 + pl0[i]
        d1 = pow(e, const4/10*n)
        print "DISTÂNCIA {:010.010f} \t POTÊNCIA {:03d}".format(d1,pl0[i])

distanciaPotenciaSinal(pl0, len(pl0), pt, pd0, d0, n, x0)

    
