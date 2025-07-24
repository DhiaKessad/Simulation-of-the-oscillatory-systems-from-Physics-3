#Cylinder system
import numpy as np
import control as ctrl
import matplotlib.pyplot as plt

# Parameters
R = 1 # Raduis of the path
M = 10# Mass of the cylinder
r = 0.1 # Radius of the cylinder
g = 9.81 # gravity

#ODE q" +(gR)/(R^2 + 1/2 r^2)) * q = 0
F = (g * R)/(R**2 + 0.5 * r**2)

# State-space representation
A = np.array([[0, 1],[-F, 0]])
B = np.array([[0], [0]])
C = np.array([[1, 0]])
sys = ctrl.ss(A, B, C, 0)

t = np.arange(0,10,0.1)
[t_anl,q_anl,] = ctrl.initial_response(sys, T=t, X0 = [0.01,0])
q_deg = q_anl * 180 / np.pi  # Convert radians to degrees

plt.figure(figsize=(7,7))
plt.plot(t_anl,q_deg,'k-')
plt.title('Exercise 5: Cylinder System Simulation')
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Angle Theta (deg)')
plt.show()