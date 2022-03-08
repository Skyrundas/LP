import numpy as np
import matplotlib.pyplot as plt
from math import *
import scipy.optimize

#%% Définition des fonctions

#Pour la trajectoire
def y(x):
    return -x**2-x+100

X=[0,0.3,0.6,0.9,1.2,1.5,1.8,2.1,2.4]
Y=[0,0.25,0.4,0.46,0.42,0.28,0.04,-0.3,-0.74]

#Calcul des coordonnées Vx et Vy des vecteurs vitesse
Vx=[]
for i in range(len(X)-1) :
    Vx=Vx+[X[i+1]-X[i]]#on prend un pas de temps égal à 1
Vy=[]
for i in range(len(Y)-1) :
    Vy=Vy+[Y[i+1]-Y[i]]

#Calcul des coordonnées des vecteurs variation de vitesse
DVx=[]
for i in range(len(Vx)-1) :
    DVx=DVx+[(Vx[i+1]-Vx[i])]

DVy=[]
for i in range(len(Vy)-1) :
    DVy=DVy+[(Vy[i+1]-Vy[i])]

#%% Tracé du graphe

#plt.xlim(0,10)
#plt.ylim(0,15)
plt.title("Tracer un vecteur variation de vitesse avec Python")
plt.xlabel("$x$")
plt.ylabel("$y$")

plt.plot(X,Y,'r+',ms=20)# tracé des points, ms détermine la taille des marqueurs.

#Tracé des vecteurs vitesses
v=plt.arrow(X[0],Y[0],(X[1]-X[0]),(Y[1]-Y[0]) , shape='full', lw=1, length_includes_head=True, rasterized=True, color='c', head_width=.05,fc='c')#pour la légende
for i in range(1,8):
    plt.arrow(X[i],Y[i],(X[i+1]-X[i]),(Y[i+1]-Y[i]) , shape='full', lw=1, length_includes_head=True, rasterized=True, color='c', head_width=.05,fc='c')

#Tracé des vecteurs variation de vitesse
Dv=plt.arrow(X[1],Y[1],DVx[0],DVy[0] , shape='full', lw=1, length_includes_head=True, rasterized=True, color='b', head_width=.02,fc='b')#pour la légende
for i in range(1,7):
   plt.arrow(X[i+1],Y[i+1],DVx[i],DVy[i] , shape='full', lw=1, length_includes_head=True, rasterized=True, color='b', head_width=.02,fc='b')

plt.show()
plt.legend([v,Dv],['Vecteurs vitesses','Vecteurs variation de vitesse'])