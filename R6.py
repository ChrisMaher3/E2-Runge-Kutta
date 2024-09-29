import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def driven_pendulum(t, y, b, omega0, omega_d, A):
    x, v = y
    dxdt = v
    dvdt = -b * v - (omega0 ** 2) * x + A * np.sin(omega_d * t)
    return [dxdt, dvdt]

def loop_through(omega, b, tf, y0, A):
    plt.figure()

    for omega_d in [0.5, 0.75, 1, 0.25]:
        result = integrate.solve_ivp(
            fun=driven_pendulum,
            t_span=(0, tf),
            y0=y0,
            args=(b, omega, omega_d, A), 
            method="RK45",
            t_eval=np.linspace(0, tf, 1001)
        )

        t = result.t
        x, v = result.y

        plt.plot(t, x, label='$x(t): \omega_d = {:.2f}$ '.format(omega_d))

    plt.legend() 
    plt.xlabel('Time (t)')
    plt.ylabel('Position (x)')
    #plt.savefig('R6_Oscillator_driven_multi.svg', bbox_inches='tight')
    plt.show()

x0 = 0   
v0 = 1  
y0 = [x0, v0]
t0 = 0  

b = 0.1
omega0 = 1
A = 1
tf = 100

loop_through(omega0, b, tf, y0, A)