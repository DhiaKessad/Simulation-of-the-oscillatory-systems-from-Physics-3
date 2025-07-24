#Rod, mass and spring system
import numpy as np
import control as ctrl
import matplotlib.pyplot as plt

# Parameters
m = 1 # point like mass
M = 10 # Mass of the rod
k = 1# spring stiffness
L = 0.5
a = 0.4
g = 9.81 # gravity
#ODE q" +((1/2gLM + mgL) + ka^2)/(1/3ML^2 +mL^2) * q = 0
F = ((0.5 * g * L * M + m * g * L) + k * a**2)/(0.333 * M * L**2 + m * L**2)

# State-space representation
A = np.array([[0, 1],[-F, 0]])
B = np.array([[0], [0]])
C = np.array([[1, 0]])
sys = ctrl.ss(A, B, C, 0)

t = np.arange(0,10,0.1)
[t_anl,q_anl,] = ctrl.initial_response(sys, T=t, X0 = [0.1,0])
q_deg = q_anl * 180 / np.pi  # Convert radians to degrees

plt.figure(figsize=(7,7))
plt.plot(t_anl,q_deg,'k-')
plt.title('Exercise 4: Rod, Mass and Spring System Simulation')
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Angle Theta (deg)')
plt.show()
