import numpy as np
import matplotlib.pyplot as plt

from scipy import integrate


def simple_pendulum(t, y):
    x, v = y 
    dydt = np.array([v, -x])
    return dydt

x0 = 0
v0 = 1
y0 = (x0, v0) 
t0 = 0 

tf = 10*np.pi  
n = 1001 
t = np.linspace(t0, tf, n)

result = integrate.solve_ivp(fun=simple_pendulum, 
                             t_span=(t0, tf),  
                             y0=y0, 
                             method="RK45", 
                             t_eval=t) 

x, v = result.y
t = result.t

fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].plot(t, x, label=r"$x(t)$")
ax[0].plot(t, v, label=r"$v(t)$")
ax[0].legend(loc=1)
ax[0].set_xlabel("t")
ax[0].set_ylabel("something")

ax[1].plot(v, x, 'k')

ax[1].axis('equal')

ax[1].set_xlabel("x")
ax[1].set_ylabel("v")

plt.show()
