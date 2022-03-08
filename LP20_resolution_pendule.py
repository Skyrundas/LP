import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import scipy.misc
import scipy.integrate

"""
PENDULE
"""
g = 9.81#m/s^2
m = 0.1#kg
l = 0.5#m
theta0 = 1#rad que l'on peut changer entre 0.1 et 2 par exemple (différence visible à partir de 1)
thetap0 = 0#rad/s

#Définition du temps
t = np.linspace(0,10,1000)

#Cas résolu analytiquement, approximation des petits angles
def theta(temps):
    return(theta0*np.cos(np.sqrt(g/l)*t))

#Résolution numérique
def func(y, t):
    theta, thetap = y
    #Non amorti
    return np.array([thetap, -(g/l)*np.sin(theta)])
    #Amorti
    # return np.array([thetap, -thetap -(g/l)*np.sin(theta)])
sol = scipy.integrate.odeint(func,[theta0,thetap0],t)

# Calcul des énergies associées, caculées dans ce script avec l'angle numérique
Ep = m*g*l*(1-np.cos(sol[...,0]))
Ec = (m/2)*(l*sol[...,1])**2
Em = Ec+Ep

fig, axes = plt.subplots(2)
fig.suptitle("Résolution numérique et analytique du pendule simple\n Énergies calculées avec la résolution numérique")

axes[0].set(xlim=[0,2.5])
axes[1].set(xlim=[0,2.5])
axes[1].set(xlabel="Temps (s)")
axes[0].set(ylabel="Énergie (J)")
axes[1].set(ylabel="Angle (rad)")

#Tracé des énergies
axes[0].plot(t,Ep,label="Ep")
axes[0].plot(t,Ec,label="Ec")
axes[0].plot(t,Em,label="Em")
axes[0].legend()
#Tracés de l'angle
axes[1].plot(t,sol[...,0],label="Angle")
axes[1].plot(t,theta(t),label="Angle analytique")
axes[1].legend()
plt.show()
