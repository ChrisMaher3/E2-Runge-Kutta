import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

a = 1
b = 1

def nonlinear1(t, y):
    dydt = -a*y**3 + b*np.sin(t)
    return dydt

def main():
    y0 = np.array([0])
    t0 = 0
    tf = 20
    n = 101
    t = np.linspace(t0, tf, n)
    result = integrate.solve_ivp(fun=nonlinear1, 
                                 t_span=(t0, tf), 
                                 y0=y0, 
                                 method="RK45", 
                                 t_eval=t)
    y = result.y[0]
    t = result.t
    
    plt.plot(t,y,'k.', label = "a = 1, b = 1")
    plt.xlabel("T")
    plt.ylabel("Y")
    plt.legend(loc = "upper right")
    #plt.savefig("a80_b100.svg",bbox_inches='tight') 
    plt.show()
    
if __name__ == '__main__':
    main()