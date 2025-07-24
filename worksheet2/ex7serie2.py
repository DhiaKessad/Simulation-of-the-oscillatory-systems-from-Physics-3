#System of Pully and Mass
#In this exercise we will take into account the potential energy of the mass
# I used theta as my variable for the displacement of the mass
# you use x by theta = R * x
import numpy as np
import control as ctrl
import matplotlib.pyplot as plt

# Parameters
m = 0.5 # mass
k = 60# spring stiffness
M = 2 # mass of the pulley
R = 0.2 # radius of the pulley
g = 9.81

#ODE q" + k/(m + 0.5 * M) * q = -m * g /(R * (m + 0.5 * M))
F = 1/(m + 0.5 * M)

# State-space representation
A = np.array([[0, 1],[-k/F, 0]])
B = np.array([[0], [-m * g / (R * F)]])
C = np.array([[1, 0]])
sys = ctrl.ss(A, B, C, 0)

t = np.arange(0,3,0.1)
[t_anl,q_anl,] = ctrl.initial_response(sys, T=t, X0 = [np.pi/25,0])
q_deg = q_anl * 180 / np.pi

plt.figure(figsize=(7,7))
plt.plot(t_anl,q_deg,'k-')
plt.title('Exercise 7: Pully system')
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Angle (deg)')
plt.show()