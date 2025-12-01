import random
import numpy as np
import matplotlib.pyplot as plt 


def rand_walk(n):
    N=100
    direction=[1,-1]
    R2_final=0
    R2_emp=[]
    x_plot=[]
    y_plot=[]
    for i in range(N):
        x_in=0
        y_in=0
        for j in range(n):
            x_in+=random.choice(direction)
            y_in+=random.choice(direction)
            x_plot.append(x_in)
            y_plot.append(y_in)
        
         
        R2=x_in**2+y_in**2
        R2_emp.append(R2)
        R2_final+=R2

    Avg_R2=R2_final/N
    std=np.std(R2_emp,ddof=1)
    error=std/N**0.5
    plt.plot(x_plot,y_plot, marker='o')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()  
    

    #return Avg_R2, error

rand_walk(10)
'''n_list = [10, 20, 50, 100, 200]
rand_list = []
error_list = []

for n in n_list:
    avg, err = rand_walk(n)
    rand_list.append(avg)
    error_list.append(err)

log_n = np.log(n_list)
log_R2 = np.log(rand_list)

slope, intercept = np.polyfit(log_n, log_R2, 1)
nu = slope / 2
fit_line = slope * log_n + intercept

plt.errorbar(log_n, log_R2, yerr=error_list, fmt='o', label='Simulation')
plt.plot(log_n, fit_line, 'r-', label=f'Fit: slope={slope:.2f}')
plt.xlabel('log(Number of steps n)')
plt.ylabel('log(<R^2>)')
plt.legend()
plt.show()

print("Estimated ν =", nu)

'''
