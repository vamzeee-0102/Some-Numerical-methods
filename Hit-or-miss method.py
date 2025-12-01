import random
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2

N = int(input("Input N: "))
c = 0
x_min = 0
x_max = 10
f_max = f(x_max) 

x_points = []
y_points = []

for i in range(N):
    x_rand = random.uniform(x_min, x_max)
    y_rand = random.uniform(0, f_max)
    
    x_points.append(x_rand)
    y_points.append(y_rand)
    
    if y_rand < f(x_rand):
        c += 1

area_estimate = (c / N) * (x_max - x_min) * f_max
print("Estimated area =", area_estimate)


plt.scatter(x_points, y_points, s=5, color='blue', label='Random points')

x_curve = np.linspace(x_min, x_max, 1000)  # 1000 points from x_min to x_max
y_curve = f(x_curve)
plt.plot(x_curve, y_curve, color='red', label='y = x^2')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
