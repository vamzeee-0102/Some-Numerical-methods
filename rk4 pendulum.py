from math import sin, cos
import matplotlib.pyplot as plt

# Parameters
q = 0      # damping
b = 0   # driving strength
w0 = 0.2   # driving frequency


def dth_dt(th, f):
    return f

def pendulum(th, f, t):
    return -q*f - sin(th) - b*cos(w0*t)

# One RK4 step
def rk4_step(th, f, t, h):
    k1 = h * dth_dt(th, f)
    l1 = h * pendulum(th, f, t)

    k2 = h * dth_dt(th + 0.5*k1, f + 0.5*l1)
    l2 = h * pendulum(th + 0.5*k1, f + 0.5*l1, t + 0.5*h)

    k3 = h * dth_dt(th + 0.5*k2, f + 0.5*l2)
    l3 = h * pendulum(th + 0.5*k2, f + 0.5*l2, t + 0.5*h)

    k4 = h * dth_dt(th + k3, f + l3)
    l4 = h * pendulum(th + k3, f + l3, t + h)

    th_new = th + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    f_new  = f  + (1/6)*(l1 + 2*l2 + 2*l3 + l4)

    return th_new, f_new

# Initial conditions
th = 0.2
f = 0
t = 0
h = 0.01
T = 100

th_list = []
om_list = []
t_list = []

steps = int(T/h)

for i in range(steps):
    th, f = rk4_step(th, f, t, h)
    th_list.append(th)
    om_list.append(f)
    t_list.append(t)
    t += h

# Plot both graphs
plt.figure(figsize=(10,4))

# Theta vs Time
plt.subplot(1,2,1)
plt.plot(t_list, th_list)
plt.xlabel("Time")
plt.ylabel("Theta")
plt.title("Theta vs Time")

# Phase portrait
plt.subplot(1,2,2)
plt.plot(th_list, om_list, '.', markersize=1)
plt.xlabel("Theta")
plt.ylabel("Omega")
plt.title("Phase Portrait")

plt.tight_layout()
plt.show()
