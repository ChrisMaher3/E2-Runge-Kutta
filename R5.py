import numpy as np
import matplotlib.pyplot as plt

from scipy import integrate


def damped_pendulum(t, y, b, omega0):
    x, v = y
    dxdt = v
    dvdt = -b*v-(omega0**2)*x
    dydt = np.array([dxdt, dvdt])
    return dydt

lfun = lambda t, y, : damped_pendulum(t, y, b, omega0)

x0 = 0  
v0 = 1 
y0 = (x0, v0)  
t0 = 0  

b = 0.1
omega0 = 1


tf = 30
n = 1001  


t = np.linspace(t0, tf, n) 

result = integrate.solve_ivp(fun=lfun, 
                             t_span=(t0, tf), 
                             y0=y0,
                             method="RK45", 
                             t_eval=t)


x, v = result.y
t = result.t


epsilon = 1e-3

for i in range(len(t)):
    if np.abs(x[i]) < epsilon and np.abs(v[i]) < epsilon:
        print(f"Oscillator is considered 'at rest' at t = {t[i]:.2f} seconds.")
        break

fig, ax = plt.subplots(1, 2, figsize=(12, 6))  

ax[0].plot(t, x, label="x(t)")
ax[0].plot(t, v, label="v(t)")
ax[0].set_xlabel("Time (t)")
ax[0].set_ylabel("Displacement(x)")
ax[0].legend(loc=1)

ax[1].plot(v, x, 'k')
ax[1].axis('equal')
ax[1].set_xlabel("Displacement (x)")
ax[1].set_ylabel("Velocity (v)")
#plt.savefig("R5_B5_t25.83_overdamped.svg",bbox_inches='tight') 
plt.show()