import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

v = 10
r = 50
l = 100

def differential_rl(t, i):
    dIdt = (v-r*i)/l
    return dIdt

def main():
    i0 = np.array([0])
    t0 = 0
    tf = 20
    h = 0.5
    t = np.arange(t0, tf+h, h)
    result = integrate.solve_ivp(fun=differential_rl, 
                                 t_span=(t0, tf), 
                                 y0=i0, 
                                 method="RK45", 
                                 t_eval=t)
    i_differential = result.y[0]
    t = result.t
    i_exact = (v / r) * (1 - np.exp(-r * t / l))
    
    plt.plot(t, i_differential, "k-", label = "Differential Equation")
    plt.plot(t, i_exact, "C1--", label = "Exact Solution")
    plt.xlabel("Time (s)")
    plt.ylabel("Current (A)")
    plt.legend()
    plt.savefig("R2_Exact_vs_Dif_h0.5.svg",bbox_inches='tight') 
    plt.show()
    
if __name__ == '__main__':
    main()
