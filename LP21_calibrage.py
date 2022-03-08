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

Te=0.001 #période d'échantillonnage
N=T/Te #nombre de points
c=0.5 #calibre

#%% FONCTIONS

def s(t,T,S0):

    return S0*np.cos(2*np.pi/T*t)

delta_e=c/(2**11) #quantification en tension [en V]

def quantification(U):
    n=len(U)
    U_cal=np.zeros(n)
    for i in range (n):
        k=floor(U[i]/delta_e)
        if U[i]>c:
            U_cal[i]=c
        elif U[i]<-c:
            U_cal[i]=-c
        elif U[i]<k*delta_e+delta_e/2:
            U_cal[i]=k*delta_e
        else :
            U_cal[i]=(k+1)*delta_e
    return U_cal

#LISTE DES ABSCISSES
t= np.linspace(0,15,floor(N)) #début, fin, nombre de points

#LISTE DES ORDONNEES
U = s(t, T, U0)
U_cal = quantification(U)

#%% GRAPHE

plt.plot(t,U, label='Signal échantillonné en temps')
plt.plot(t,U_cal, 'r+', label='Signal échantillonné en temps et en tension')
plt.xlim(0,1)
plt.ylim(-1,1)
plt.grid()
plt.xlabel("$t$ [en s]")
plt.ylabel("Tension mesurée $U$ [en V]")
plt.show()
plt.legend()
