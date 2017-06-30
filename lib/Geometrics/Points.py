from math import sqrt
import pickle as pk
import copy

class point(object):
        def __init__(self, x, y):
                self.x = x
                self.y = y
        def __str__(self):
                return "P({:f},{:f})".format(self.x,self.y)             
        def __eq__(self, other):
                if not isinstance(other, self.__class__): return False                
                if int(self.x) == int(other.x) or int(self.x) == int(other.x)+1 or int(self.x) == int(other.x)-1:
                        if int(self.y) == int(other.y) or int(self.y) == int(other.y)+1 or int(self.y) == int(other.y)-1:
                                return True
                        else: return False
                else: return False      
        def __add__(self,other):
                if not isinstance(other, self.__class__): return False   
                return point(self.x+other.x, self.y+other.y)
                
##########################################################################################################
def get_two_points_distance(p1, p2):
        return sqrt(pow((p1.x - p2.x), 2) + pow((p1.y - p2.y), 2))

