from math import sin, cos
import matplotlib.pyplot as plt

q = 1
b = 10
w0 = 0.2

def dth_dt(t, th, f):
    return f

def pendulum(t, th, f):
    return -q*dth_dt(t, th, f) - sin(th) - b*cos(w0*t)

def rungeKutta(t0, th0, f0, t_end, h):
    n = int((t_end - t0)/h)
    t = t0
    th = th0
    f = f0

    for i in range(n):
        k1 = h * pendulum(t, th, f)
        l1 = h * dth_dt(t, th, f)

        k2 = h * pendulum(t + 0.5*h, th + 0.5*k1, f + 0.5*l1)
        l2 = h * dth_dt(t + 0.5*h, th + 0.5*k1, f + 0.5*l1)

        k3 = h * pendulum(t + 0.5*h, th + 0.5*k2, f + 0.5*l2)
        l3 = h * dth_dt(t + 0.5*h, th + 0.5*k2, f + 0.5*l2)

        k4 = h * pendulum(t + h, th + k3, f + l3)
        l4 = h * dth_dt(t + h, th + k3, f + l3)

        th = th + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        f  = f  + (1/6)*(l1 + 2*l2 + 2*l3 + l4)

        t = t + h

    return th, f


# Initial values
t0 = 0
th0 = 0.2
f0 = 0
h = 0.01

th_list = []
om_list = []
t_list = []

for t in range(1, 100):
    theta, omega = rungeKutta(t0, th0, f0, t, h)
    th_list.append(theta)
    om_list.append(omega)
    t_list.append(t)

plt.figure()
plt.plot(t_list, th_list)
plt.xlabel("Time")
plt.ylabel("Theta")
plt.show()