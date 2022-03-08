import numpy as np
import matplotlib.pyplot as plt
from math import *
import scipy.optimize

#%% Définition des constantes

g=9.81#champ de pesanteur [m/s^2]
h=500#hauteur initiale [m]

#%% Définition des fonctions

#Pour la trajectoire
def z(t):
    return h-g/2*t**2

T=np.linspace(0,10,10)
X=np.zeros(10)
Z=z(T)

#Calcul de la vitesse du système

Vz=[]
for i in range(len(Z)-1) :
    Vz=Vz+[Z[i+1]-Z[i]]

#Calcul du vecteur variation de vitesse

DVz=[]
for i in range(len(Vz)-1) :
    DVz=DVz+[(Vz[i+1]-Vz[i])]

#%% Tracé du graphe

plt.xlim(-0.5,0.5)
#plt.ylim(0,15)
plt.title("Tracé du vecteur variation de vitesse pour une chute libre")
#plt.xlabel("")
plt.ylabel("$z$")

plt.plot(X,Z,'r+',ms=5)# tracé des points, ms détermine la taille des marqueurs.

for i in range(len(DVz)):
    # tracé des vecteurs variation de vitesse
   plt.arrow(0,Z[i+1],0,DVz[i], shape='full', lw=1, length_includes_head=False, rasterized=True, color='b', head_width=.01,head_length=15,fc='b')

plt.show()