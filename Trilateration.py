from lib.Circle import *
import numpy as np
import matplotlib.pyplot as plt
beacons  = [[0,0,1000],[10,-10,1000],[-10,-10,1000]]
children = np.matrix([[x,x-200] for x in range(100,900)])
real = [[x for x in range(100,900)],[x for x in range(-100,700)]]
distances = np.zeros((len(beacons),children.shape[0],1))
fig, ax = plt.subplots()

## esse trecho do codigo transforma o caminho ideal em distancia para os beacons  ################################################################
for i,j in enumerate(children):
    for k,l in enumerate(beacons):
        distances[k,i,0] = mt.sqrt(mt.pow(j[0,0]-l[0], 2)+mt.pow(j[0,1]-l[1], 2))
##################################################################################################################################################

## esse trecho desenha na tela o circulo de alcance dos beacons baseado no raio de alcance.
t = np.linspace(0,2*mt.pi,num=500)
g = np.zeros((3,t.shape[0],2))
for i in range(len(beacons)):
    graf = np.zeros((t.shape[0],2))
    for j in range(graf.shape[0]):
        graf[j,0] = mt.cos(t[j])*beacons[i][2] + beacons[i][0]
        graf[j,1] = mt.sin(t[j])*beacons[i][2] + beacons[i][1]
    ax.plot(graf[:,0],graf[:,1], label = "alcance Beacon "+str(i), linestyle='--')
##################################################################################################################################################
    

### esse trecho desenha o raio entre os beacons e uma distancia.
#for i in range(len(beacons)):
    #graf = np.zeros((t.shape[0],2))
    #for j in range(graf.shape[0]):
        #graf[j,0] = mt.cos(t[j])*distances[i,0,0] + beacons[i][0]
        #graf[j,1] = mt.sin(t[j])*distances[i,0,0] + beacons[i][1]
    #g[i] = graf.astype(int)
    #ax.plot(graf[:,0],graf[:,1], label = "D0-"+str(i), linestyle='--')
###################################################################################################################################################


## desenha os beacons na tela 
for i,j in enumerate(beacons):
    ax.scatter(j[0],j[1],label="beacons {:02d}".format(i),
            edgecolors='none')
##################################################################################################################################################
x=[]
y=[]
p1 =   point(0, 0)
p2 =   point(10, -10)
p3 =   point(-10, -10)

#for i in range(800):
    #ax.legend()
    #plt.xlim(-1000,1000)
    #plt.ylim(-1000,1000)
    #ax.grid(True)       
    #for k,j in enumerate(beacons):
        #ax.scatter(j[0],j[1],label="beacons {:02d}".format(k),edgecolors='none')     
    #c1 = circle(p1, distances[0,i,0])
    #c2 = circle(p2, distances[1,i,0])
    #c3 = circle(p3, distances[2,i,0])
    #circle_list = [c1, c2, c3]
    #inner_points = []
    #for p in get_all_intersecting_points(circle_list):
        #if is_contained_in_circles(p, circle_list):
            #inner_points.append(p) 
    #if len(inner_points) is not 0:
        #x.append(inner_points[0].x)
        #y.append(inner_points[0].y)
        #ax.scatter(inner_points[0].x,inner_points[0].y,label="beacons {:02d}".format(i),edgecolors='none')        
        #print x[len(x)-1], y[len(y)-1],i
   ## plt.savefig("PONTOS/{:03d}.png".format(i))
    ##ax.clear()
ax.plot(real[0],real[1], label="REAL")
ax.plot(x,y,label="MEDIDO")
ax.legend()
plt.xlim(-1000,1000)
plt.ylim(-1000,1000)
ax.grid(True) 



plt.show()