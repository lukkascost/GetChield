from lib.TestClasses import Trilateration,Moviment
from lib.Geometrics import Circle,Points
import matplotlib.pyplot as plt
beacons = Trilateration.trilateration_beacons()
road = Moviment.moviment(0.028571428571429)
distances = Trilateration.trilateration_distances()
fig, ax = plt.subplots()

beacons.append(Circle.circle(Points.point(0, 0), 1000))
beacons.append(Circle.circle(Points.point(10, -10), 1000))
beacons.append(Circle.circle(Points.point(-10, -10), 1000))
atual = [0,0]
for x in range(200):
        atual[0] = x+200
        road.append(Points.point(atual[0], atual[1]))
for x in range(200):
        atual[1]=x
        road.append(Points.point(atual[0], atual[1]))
for x in range(200,0,-1):
        atual[0]= x+200
        road.append(Points.point(atual[0], atual[1]))
for x in range(200,0,-1):
        atual[1]=x
        road.append(Points.point(atual[0], atual[1]))
#road.toGraph()     
distances.beacons = beacons
distances.road = road
distances.calculate_distances()
distances.set_points()
distances.toImages("Samples/Tests/middle/Images/")
road.save("Samples/Tests/middle/01.moviment")
beacons.save("Samples/Tests/middle/01.trilateration_beacons")
distances.save("Samples/Tests/middle/01.trilateration_distances")
beacons.appendToAx(ax)
#road.appendToAx(ax)

        
ax.legend()
ax.grid(1)
plt.xlim([-1000,1000])
plt.ylim([-1000,1000])
plt.show()
ax.clear()