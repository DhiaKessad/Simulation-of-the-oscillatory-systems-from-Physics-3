#mass and two springs in series
#didn't take into account gravity and potential energy
import numpy as np
import control as ctrl
import matplotlib.pyplot as plt

# Parameters
m = 0.5 # mass
k = 100# spring stiffness
#ODE q" + 2k/m * q = 0
F = 2 * k / m

# State-space representation
A = np.array([[0, 1],[-F, 0]])
B = np.array([[0], [0]])
C = np.array([[1, 0]])
sys = ctrl.ss(A, B, C, 0)

t = np.arange(0,10,0.1)
[t_anl,q_anl,] = ctrl.initial_response(sys, T=t, X0 = [0.01,0])

plt.figure(figsize=(7,7))
plt.plot(t_anl,q_anl,'k-')
plt.title('Exercise 6: Mass, two springs System Simulation')
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.show()
