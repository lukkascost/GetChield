from lib.TestClasses import Trilateration,Moviment
from lib.Geometrics import Circle,Points
import matplotlib.pyplot as plt

beacons = Trilateration.trilateration_beacons()
road = Moviment.moviment(0.00)
distances = Trilateration.trilateration_distances()



road = road.load("Samples/Tests/easy/01.moviment")
beacons = beacons.load("Samples/Tests/easy/01.trilateration_beacons")
distances = distances.load("Samples/Tests/easy/01.trilateration_distances")
for step in range(800):
        fig, ax = plt.subplots()
        distances.appendToAx(ax,step)
        beacons.appendToAx(ax)
        road.appendToAx(ax)
        
        ax.legend()
        ax.grid(1)
        plt.xlim([-1000,1000])
        plt.ylim([-1000,1000])
        plt.savefig("Samples/Tests/easy/Images/{:04d}.png".format(step),bbox_inches='tight',dpi=400)
        plt.show()
        ax.clear()