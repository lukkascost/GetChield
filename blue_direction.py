from lib.TestClasses import Moviment
from lib.TestClasses import Trilateration

oMovi = Moviment.moviment(1)
oMovi = oMovi.load("Samples/Tests/hard/01.moviment")
oTrilaBeacon = Trilateration.trilateration_beacons()
oTrilaBeacon = oTrilaBeacon.load("Samples/Tests/hard/01.trilateration_beacons")
oTrilaBeacon.beacons[0].center.x = 0.0
oTrilaBeacon.beacons[0].center.y = 0.0
oTrilaBeacon.beacons[1].center.x = -11.5
oTrilaBeacon.beacons[1].center.y = -20.0
oTrilaBeacon.beacons[2].center.x = 11.5
oTrilaBeacon.beacons[2].center.y = -20.0
oTrilaDistan = Trilateration.trilateration_distances()
oTrilaDistan = oTrilaDistan.load("Samples/Tests/hard/01.trilateration_distances")
oTrilaDistan.beacons = oTrilaBeacon
oTrilaDistan.road = oMovi
oTrilaDistan.calculate_distances()
oTrilaDistan.set_points()
step = 300
print oTrilaDistan.get_direction(step)
oTrilaDistan.toGraph(step)