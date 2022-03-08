import numpy as np
import matplotlib.pyplot as plt
from math import *

#%% CONSTANTES

g = 9.81 #champ de pesanteur (en m/s^2)
l = 50e-2 #longueur du fil (en m)
T=2*np.pi*np.sqrt(l/g) #période du pendule
theta0=10 #angle initial (en °)

s=56.9e-3 #facteur de conversion angle-tension (en V/°)
U0=s*theta0

Te1=1e-2 #fréquence d'échantillonnage (en s)
Te2=1e-1
N1=T/Te1 #nombre de points
N2=T/Te2

#%% FONCTIONS

def s(t,T,S0):

    return S0*np.cos(2*np.pi/T*t)


#LISTE DES X
t1= np.linspace(0,15,floor(N1)) #début, fin, nombre de points
t2= np.linspace(0,15,floor(N2))
t3 = np.linspace(0,15,1000)


#LISTE DES Y
Y1 = s(t1, T, U0)
Y2 = s(t2, T, U0)
Y3 = s(t3, T, U0)
theta1 = s(t1, T, theta0)
theta3 = s(t3, T, theta0)

#%% GRAPHE

plt.plot(t1,Y1, 'r+-', label='Signal discrétisé acquis par la carte ($T_e$ = 0,01 s)')
#plt.plot(t2,Y2, 'r+', label='$T_e$ = 0,1 s')
plt.plot(t3,Y3, label='Signal analogique mesuré par le capteur potentiométrique')
#plt.plot(t1,theta1,'r+-', label='Signal discrétisé après étalonnage ($T_e$ = 0,01 s)')
#plt.plot(t3,theta3, label='Mesurande')
plt.grid()
plt.xlabel("$t$ [en s]")
plt.ylabel("Tension mesurée $U$ [en V]")
#plt.ylabel(r"Angle du pendule $\theta$ [en °]")
plt.show()
plt.legend()




