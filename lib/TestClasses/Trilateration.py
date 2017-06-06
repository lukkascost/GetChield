from ..Geometrics import Circle,Points
import matplotlib.pyplot as plt
import numpy as np
import math as mt
import pickle as pk
import copy
class trilateration_beacons(object):
        def __init__(self):
                self.beacons = []
                self.nbeacons = 0
        def append(self,node):
                self.beacons+=[node]
                self.nbeacons+=1
        
        def save(self,path):
                pk.dump(self, open(path,"w"))
                print "Arquivo salvo com sucesso em ",path

        def load(self,path):
                return copy.copy(pk.load(open(path,"r")))          
        
        def __str__ (self):
                returned = ""
                for i,j in enumerate(self.beacons):
                        returned += "Beacon {:02d}: {}\n".format(i+1,str(j))
                return returned
        def toGraph(self,xlim=[-1100,1100],ylim=[-1100,1100]):
                fig, ax = plt.subplots()
                for i,j in enumerate(self.beacons):
                        ax.scatter(j.center.x,j.center.y,label="Beacon {:02d}".format(i),edgecolors='none')
                t = np.linspace(0,2*mt.pi)
                for i in range(self.nbeacons):
                        graf = np.zeros((t.shape[0],2))
                        for j in range(graf.shape[0]):
                                graf[j,0] = mt.cos(t[j])*self.beacons[i].radius + self.beacons[i].center.x
                                graf[j,1] = mt.sin(t[j])*self.beacons[i].radius + self.beacons[i].center.y
                        ax.plot(graf[:,0],graf[:,1], label = "radius Beacon {:02d}".format(i+1), linestyle='--')
                ax.legend()
                ax.grid(1)
                plt.xlim(xlim)
                plt.ylim(ylim)
                plt.show()
                ax.clear()
        def appendToAx(self,ax):
                for i,j in enumerate(self.beacons):
                        ax.scatter(j.center.x,j.center.y,label="Beacon {:02d}".format(i),edgecolors='none')
                t = np.linspace(0,2*mt.pi)
                for i in range(self.nbeacons):
                        graf = np.zeros((t.shape[0],2))
                        for j in range(graf.shape[0]):
                                graf[j,0] = mt.cos(t[j])*self.beacons[i].radius + self.beacons[i].center.x
                                graf[j,1] = mt.sin(t[j])*self.beacons[i].radius + self.beacons[i].center.y
                        ax.plot(graf[:,0],graf[:,1], label = "radius Beacon {:02d}".format(i+1), linestyle='--')      
        def distance_circles(self,oPoint):
                distances = []
                for i,j in enumerate(self.beacons):
                        distances+= [Circle.circle(j.center,Points.get_two_points_distance(j.center, oPoint))]
                return distances
        
        
class trilateration_distances(object):
        def __init__(self):
                self.beacons = None
                self.road = None
                self.distances = []
                self.points = []
        def calculate_distances(self):
                for k,h in enumerate(self.road.points):
                        dist = []
                        for i,j in enumerate(self.beacons.beacons):
                                dist+= [Circle.circle(j.center,Points.get_two_points_distance(j.center, h))]
                        self.distances+=[dist]
        def set_points(self):
                for i in self.distances:
                        inner_points = []
                        for p in Circle.get_all_intersecting_points(i):
                                if Circle.is_contained_in_circles(p,i):
                                        self.points.append(p)
                                        break    
                                
        def toGraph(self,step,xlim=[-1100,1100],ylim=[-1100,1100]):
                fig, ax = plt.subplots()
                ax.scatter(self.points[step].x,self.points[step].y,label="found Point",edgecolors='none') 
                t = np.linspace(0,2*mt.pi)
                for i in range(self.beacons.nbeacons):
                        graf = np.zeros((t.shape[0],2))
                        for j in range(graf.shape[0]):
                                graf[j,0] = mt.cos(t[j])*self.distances[step][i].radius + self.distances[step][i].center.x
                                graf[j,1] = mt.sin(t[j])*self.distances[step][i].radius + self.distances[step][i].center.y
                        ax.plot(graf[:,0],graf[:,1], label = "distance Beacon {:02d}".format(i+1), linestyle='-.')
                ax.legend()
                ax.grid(1)
                plt.xlim(xlim)
                plt.ylim(ylim)
                plt.show()
                ax.clear()   
                
        def appendToAx(self,ax,step):
                ax.scatter(self.points[step].x,self.points[step].y,label="found Point",edgecolors='none') 
                t = np.linspace(0,2*mt.pi)
                for i in range(self.beacons.nbeacons):
                        graf = np.zeros((t.shape[0],2))
                        for j in range(graf.shape[0]):
                                graf[j,0] = mt.cos(t[j])*self.distances[step][i].radius + self.distances[step][i].center.x
                                graf[j,1] = mt.sin(t[j])*self.distances[step][i].radius + self.distances[step][i].center.y
                        ax.plot(graf[:,0],graf[:,1], label = "distance Beacon {:02d}".format(i+1), linestyle='-.')          
                
        def save(self,path):
                pk.dump(self, open(path,"w"))
                print "Arquivo salvo com sucesso em ",path

        def load(self,path):
                return copy.copy(pk.load(open(path,"r")))          
                