from lib.TestClasses import Trilateration,Moviment
from lib.Geometrics import Circle,Points
import matplotlib.pyplot as plt
beacons = Trilateration.trilateration_beacons()
road = Moviment.moviment(0.028571428571429)
fig, ax = plt.subplots()

beacons.append(Circle.circle(Points.point(0, 0), 1000))
beacons.append(Circle.circle(Points.point(10, -10), 1000))
beacons.append(Circle.circle(Points.point(-10, -10), 1000))

for x in range(800):
        road.append(Points.point(x+200, 0))
road.save("Samples/Tests/easy/01.moviment")
beacons.save("Samples/Tests/easy/01.trilateration_beacons")
beacons.appendToAx(ax)
road.appendToAx(ax)
distances = beacons.distance_circles(road.points[0])
for i in Trilateration.position_point(distances):
        print i 
        
ax.legend()
ax.grid(1)
plt.xlim([-1000,1000])
plt.ylim([-1000,1000])
plt.show()
ax.clear()