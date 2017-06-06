from Points import *
import math as mt
class circle(object):
        def __init__(self, point, radius):
                self.center = point
                self.radius = radius
                
        def save(self,path):
                pk.dump(self, open(path,"w"))
                print "Arquivo salvo com sucesso em ",path

        def load(self,path):
                return copy.copy(pk.load(open(path,"r")))        
        def __str__(self):
                return "Center in {} and radius {:f}cm".format(str(self.center),self.radius)
                
                
def get_two_circles_intersecting_points(c1, c2):
        p1 = c1.center 
        p2 = c2.center
        r1 = c1.radius
        r2 = c2.radius

        d = get_two_points_distance(p1, p2)
        # if to far away, or self contained - can't be done
        if d >= (r1 + r2) or d <= mt.fabs(r1 -r2):
                return None

        a = (pow(r1, 2) - pow(r2, 2) + pow(d, 2)) / (2*d)
        h  = mt.sqrt(pow(r1, 2) - pow(a, 2))
        x0 = p1.x + a*(p2.x - p1.x)/d 
        y0 = p1.y + a*(p2.y - p1.y)/d
        rx = -(p2.y - p1.y) * (h/d)
        ry = -(p2.x - p1.x) * (h / d)
        return [point(x0+rx, y0-ry), point(x0-rx, y0+ry)]


def get_all_intersecting_points(circles):
        points = []
        num = len(circles)
        for i in range(num):
                j = i + 1
                for k in range(j, num):
                        res = get_two_circles_intersecting_points(circles[i], circles[k])
                        if res:
                                points.extend(res)
        return points

def is_contained_in_circles(point, circles):
        for i in range(len(circles)):
                if (get_two_points_distance(point, circles[i].center) > (circles[i].radius)):
                        return False
        return True