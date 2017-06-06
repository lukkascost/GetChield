from math import sqrt
import pickle as pk
import copy

class point(object):
        def __init__(self, x, y):
                self.x = x
                self.y = y
        def __str__(self):
                return "P({:f},{:f})".format(self.x,self.y)             
                
##########################################################################################################
def get_two_points_distance(p1, p2):
        return sqrt(pow((p1.x - p2.x), 2) + pow((p1.y - p2.y), 2))

