from lib.TestClasses.Trilateration import *
from lib.Geometrics.Circle import *

#oMovi = Moviment.moviment(1)
#oMovi = oMovi.load("Samples/Tests/hard/01.moviment")
#oTrilaBeacon = Trilateration.trilateration_beacons()
#oTrilaBeacon = oTrilaBeacon.load("Samples/Tests/hard/01.trilateration_beacons")
#oTrilaBeacon.beacons[0].center.x = 0.0
#oTrilaBeacon.beacons[0].center.y = 0.0
#oTrilaBeacon.beacons[1].center.x = -11.5
#oTrilaBeacon.beacons[1].center.y = -20.0
#oTrilaBeacon.beacons[2].center.x = 11.5
#oTrilaBeacon.beacons[2].center.y = -20.0
#oTrilaDistan = Trilateration.trilateration_distances()
#oTrilaDistan = oTrilaDistan.load("Samples/Tests/hard/01.trilateration_distances")
#oTrilaDistan.beacons = oTrilaBeacon
#oTrilaDistan.road = oMovi
#oTrilaDistan.calculate_distances()
#oTrilaDistan.set_points()
#step = 300
#print oTrilaDistan.get_direction(step)
#oTrilaDistan.toGraph(step)
preal = point(-30, 20)
c1 = circle(point(0, 0), int(get_two_points_distance(point(0, 0), preal)))  
c2 = circle(point(10, -10), int(get_two_points_distance(point(10, -10), preal)))  
c3 = circle(point(-10, -10), int(get_two_points_distance(point(-10, -10), preal)))  
print c1
print c2
print c3
print "c1 com c2"
pontos = []
pontos.append(get_two_circles_intersecting_points(c1,c2))
pontos.append(get_two_circles_intersecting_points(c1,c3))                       
pontos.append(get_two_circles_intersecting_points(c2,c3))   
print pontos
otrila = trilateration_beacons()
otrila.append(c1)
otrila.append(c2)
otrila.append(c3)


#otrila.toGraph(xlim=[-100, 100], ylim=[-100, 100])
lero =1 