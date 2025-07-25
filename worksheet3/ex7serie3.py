#A simple oscillatory system of ode mx' + c x' + kx = 0
import numpy as np
import control as ctrl
import matplotlib.pyplot as plt

# Parameters
m = 20 #10kg
c = 47
k = 219

#state space rep
A = np.array([[0,1], [-c/m, -k/m]])
B = np.array([[0], [0]])
C = np.array([[1, 0]])
D = np.array([[0]])
sys = ctrl.ss(A,B,C,D)

#solving the system
t = np.arange(0,50, 0.1)
[t, x] = ctrl.initial_response(sys, T=t, X0 = [0.01,0])

#plot
plt.figure(figsize=(6,6))
plt.plot(t, x, 'k-')
plt.grid()
plt.title('Exercise 7: Simple Harmonic Oscillator Simulation')
plt.xlabel('Time(s)')
plt.ylabel('Displacement (m)')
plt.show()