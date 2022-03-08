import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from math import *

"""
Etude de la corde de Melde
"""
#Données issues du manuel scolaire Lelivrescolaire, Enseignement scientique 1re.

#%%Définitions de l'abcisse et de l'ordonnée

L = np.array([85e-2,80e-2,75e-2,70e-2,65e-2,60e-2,55e-2]) #tableau des longueurs de la corde en mètres
F = np.array([15,15.8,16.8,17.2,18.8,20.4,22.8])#tableau des fréquences fondamentales mesurées en hertz

Y = 1/L#inverse de la longueur de la corde

#%%Régression linéaire

slope, intercept, rvalue, pvalue, stderr = stats.linregress(Y,F)
print("pente = {}".format(slope))
print("ordonnée à l'origine = {}".format(intercept))
print("R2 = {}".format(rvalue**2))

def predict(x):
    return slope * x + intercept

fitLine = predict(Y)

#%%Tracé du graphe

plt.title("Fondamental de la corde de Melde en fonction de l'inverse de sa longueur")
plt.grid()
plt.xlabel('Inverse de la longueur de la corde (m^-1)')
plt.ylabel('Fréquence fondamentale (Hz)')
plt.plot(Y,F,'o',label="Points expérimentaux")
plt.plot(Y,fitLine,color='r',label="Droite de régression linéaire\n y = {}x + {}".format(round(slope,4),round(intercept,4)))
plt.legend()
plt.show()
