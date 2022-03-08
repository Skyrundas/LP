import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from math import *

"""
Etude du phénomène de diffraction
"""
#Données issues du manuel scolaire Hachette éducation, Physique-chimie TS -Enseignement spécifique (p. 75).

#%%Définitions de l'abcisse et de l'ordonnée

L = np.array([128,64,26,20,14,12])*1e-6 #tableau des largeurs de la tache centrale
A = np.array([20,40,100,130,180,220])*1e-3#tableau des ouvertures de la fente

Y = 1/A#inverse de l'ouverture de la fente

#%%Régression linéaire

slope, intercept, rvalue, pvalue, stderr = stats.linregress(Y,L)
print("pente = {}".format(slope))
print("ordonnée à l'origine = {}".format(intercept))
print("R2 = {}".format(rvalue**2))

def predict(x):
    return slope * x + intercept

fitLine = predict(Y)

#%%Tracé du graphe

plt.title("Evolution de la largeur de la tache centrale de diffraction en fonction de l'ouverture de la fente")
plt.grid()
plt.xlabel("Inverse de l'ouverture de la fente (m^-1)")
plt.ylabel('Largeur de la tache centrale (m)')
plt.plot(Y,L,'o',label="Points expérimentaux")
plt.plot(Y,fitLine,color='r',label="Droite de régression linéaire\n y = {}x + {}".format(round(slope,7),round(intercept,8)))
plt.legend()
plt.show()
