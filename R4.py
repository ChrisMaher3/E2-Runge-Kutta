import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def damped_pendulum(t, y, b=0.1, omega0=1):
    x, v = y
    dxdt = v
    dvdt = -b*v-(omega0**2)*x
    dydt = np.array([dxdt, dvdt])
    return dydt

b = 0.1
omega0 = 1 
t_span = (0, 50) 
t_eval = np.linspace(0, 50, 1000)

x0 = 1
v0 = 0
initial_conditions = [x0, v0]

solution = solve_ivp(damped_pendulum, t_span, initial_conditions, args=(b, omega0), t_eval=t_eval)

t = solution.t
x = solution.y[0]
v = solution.y[1]

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(t, x, "k", label="x(t)")
plt.plot(t, v, "C1", label="v(t)")
plt.xlabel('Time')
plt.ylabel('Displacement (x)')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x, v, "k", label=f'Phase Space (b={b})')
plt.xlabel('Displacement (x)')
plt.ylabel('Velocity (v)')
plt.legend()

plt.tight_layout()
plt.show()