#You have to derive the equation of motion before you start developing the code.
# I found the ODE: (0.5* m + I /(18 * r**2 )) * x" + c * x' + 1.5* k * x =0
import numpy as np
import control as ctrl
import matplotlib.pyplot as plt

# Parameters
c = 10 # damping coeff
k = 1000 # spring stiffness
m = 1 # mass
r = 5 # radius
I = 0.5 * m * r**2 # I used the formula for pully moment of inertia

q = (0.5* m + I /(18 * r**2 ))
# ode: x" + c * x' /q + 1.5 * k * x / q = 0
# state space rep matrices
A = np.array([[0, 1 ], [-c/q, -1.5 * k / q]])
B = np.array([[0], [0]])
C = np.array([[1,0]]) #this is called the output matrix, if you want to measure the speed instead, put [0,1] (indexed by [x,x'])
D = np.array([[0]]) #because there is no force- no input
sys = ctrl.ss(A, B, C, D) # this defines the state-space system

t = np.arange(0, 100, 0.1)
[t, x] = ctrl.initial_response(sys, T =t, X0 = [10, 0])


#Plot
plt.figure(figsize=(5,5))
plt.plot(t,x, 'm-')
plt.title('Exercise 1: Pully system simulation')
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.show()