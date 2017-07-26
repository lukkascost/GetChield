import matplotlib.pyplot as plt
import sys 
import os
from lib.Geometrics.Circle import *
from lib.Geometrics.Points import *
from lib.TestClasses.Trilateration import *
from Classes import *
import math as mt
import copy as cp

path = "Samples/Measurements/Tree_To_One/blackboard/d25/1m_090g.txt"
realPoint = point(0, 100)
data  = []
for f in  open(path, mode="r").readlines():
        f = f.split(",")
        data.append([float(f[0]),float(f[1]),float(f[2])])
locate1 = data[0][0]
locate2 = data[0][1]
locate3 = data[0][2]
del data[0]
distances = np.zeros(100)
z = [-0.001061, -0.09526, 1.933, -11.85, -43.53]
p = np.poly1d(z)
x = 0
while(x>-100):
        controle = -3
        while(p(controle)>x):controle+=0.01
        distances[abs(x)] = controle*100
        x-=1
rmse = []
LE = []
pontos = []
for i in data:
        c1 = circle(point(locate1, 0), distances[int(abs(i[0]))])
        c2 = circle(point(locate2, -21.6), distances[int(abs(i[1]))])
        c3 = circle(point(locate3, -21.6), distances[int(abs(i[2]))])
        
        c1p = circle(point(locate1, 0), distances[int(abs(i[0]))+1])        
        c1s = circle(point(locate1, 0), distances[int(abs(i[0]))-1])
        c2p = circle(point(locate2, -21.6), distances[int(abs(i[0]))+1])        
        c2s = circle(point(locate2, -21.6), distances[int(abs(i[0]))-1])
        c3p = circle(point(locate3, -21.6), distances[int(abs(i[0]))+1])        
        c3s = circle(point(locate3, -21.6), distances[int(abs(i[0]))-1])      
        
        pontos.append([])
        #with c
        intersect  = get_two_circles_intersecting_points(c1, c2)
        if (intersect == None):
                intersect  = get_two_circles_intersecting_points(c2, c3)
                if intersect == None:
                        intersect  = get_two_circles_intersecting_points(c1, c3)
        pontos[-1].append(intersect)
        # with c+
        intersect  = get_two_circles_intersecting_points(c1p, c2)
        if (intersect == None):
                intersect  = get_two_circles_intersecting_points(c2, c3p)
                if intersect == None:
                        intersect  = get_two_circles_intersecting_points(c1p, c3p)
        pontos[-1].append(intersect)
        # with c-
        intersect  = get_two_circles_intersecting_points(c1s, c2)
        if (intersect == None):
                intersect  = get_two_circles_intersecting_points(c2, c3s)
                if intersect == None:
                        intersect  = get_two_circles_intersecting_points(c1s, c3s)
        pontos[-1].append(intersect)        
for li, i in enumerate(pontos):
        print "RESULTADOS LINHA ",li
        for j in i:
                if j is not None:
                        for k in j:
                                print "\t",k
                else:
                        print "\tJ is None"