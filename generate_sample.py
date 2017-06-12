from lib.TestClasses import Trilateration,Moviment
from lib.Geometrics import Circle,Points
import matplotlib.pyplot as plt
import numpy as np
import math as mt
beacons = Trilateration.trilateration_beacons()
road = Moviment.moviment(0.028571428571429)
distances = Trilateration.trilateration_distances()
fig, ax = plt.subplots()

beacons.append(Circle.circle(Points.point(0, 0), 1000))
beacons.append(Circle.circle(Points.point(10, -10), 1000))
beacons.append(Circle.circle(Points.point(-10, -10), 1000))
atual = [0,0]

t = np.linspace(0,2*mt.pi,num=800)
for i in range(beacons.nbeacons):
        graf = np.zeros((t.shape[0],2))
        for j in range(graf.shape[0]):
                graf[j,0] = mt.cos(t[j])*700 + 0
                graf[j,1] = mt.sin(t[j])*700 + 0

for i in graf:
        road.append(Points.point(i[0], i[1]))
        
#road.toGraph()     
distances.beacons = beacons
distances.road = road
distances.calculate_distances()
distances.set_points()
distances.toImages("Samples/Tests/hard/Images/")
road.save("Samples/Tests/hard/01.moviment")
beacons.save("Samples/Tests/hard/01.trilateration_beacons")
distances.save("Samples/Tests/hard/01.trilateration_distances")
beacons.appendToAx(ax)
road.appendToAx(ax)
distances.appendToAx(ax,0)

        
ax.legend()
ax.grid(1)
plt.xlim([-1000,1000])
plt.ylim([-1000,1000])
plt.show()
ax.clear()