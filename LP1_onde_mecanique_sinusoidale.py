import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(10,5))
ax.set(xlim=(0,3),ylim=(-1,1))
plt.xlabel('X (cm)', fontsize=16)
plt.ylabel('Y', fontsize=16, rotation='horizontal')
x = np.linspace(0,3,300)
t = np.linspace(1,2,300)
X2,T2 = np.meshgrid(x,t)

#Paramètres de l'onde
A = 0.9
v = 2
T = 0.25
k = 2*np.pi/(v*T)

F = A*np.sin(2*np.pi/T*T2-k*X2) # Fonction de deux  variables
# line = ax.plot(x,F[0,:], color='r', lw=2)[0]
print(F)
print(F[0])
line = ax.plot(x,F[0], color='g', lw=2)[0]

def animate(i):
    # line.set_ydata(F[i,:])
    line.set_ydata(F[i])
    line.set_xdata(x)
anim = FuncAnimation(fig, animate, interval=50, frames=300)
plt.show()
