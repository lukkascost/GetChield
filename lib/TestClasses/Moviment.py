from ..Geometrics import Points
import matplotlib.pyplot as plt
import pickle as pk
import copy
class moviment(object):
        def __init__(self,dtime):
                self.points = []
                self.npoints = 0
                self.dtime = dtime
        def append(self,point):
                self.points+=[point]
                self.npoints+=1
        
        def save(self,path):
                pk.dump(self, open(path,"w"))
                print "Arquivo salvo com sucesso em ",path

        def load(self,path):
                return copy.copy(pk.load(open(path,"r")))          
        def toGraph(self,xlim=[-1100,1100],ylim=[-1100,1100]):
                fig, ax = plt.subplots()
                ax.plot([h.x for h in self.points],[h.y for h in self.points],label = "Ideal Road")
                ax.legend()
                ax.grid(1)
                plt.xlim(xlim)
                plt.ylim(ylim)
                plt.show()
                ax.clear()
        def appendToAx(self,ax):
                ax.plot([h.x for h in self.points],[h.y for h in self.points],label = "Ideal Road")
                
        def __str__ (self):
                returned = "{:d} Points, sampling time {:.4f}\n".format(self.npoints,self.dtime)
                for i,j in enumerate(self.points):
                        returned += "Point {:02d}: {} instant {:f}s\n".format(i+1,str(j),self.dtime*i)
                return returned
