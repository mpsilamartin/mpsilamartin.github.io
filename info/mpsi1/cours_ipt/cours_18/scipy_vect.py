from math import exp
import matplotlib.pyplot as plt
from numpy import linspace, array
from scipy.integrate import odeint

alpha , beta = 1, 10
A0, B0, C0 = 1,0,0
t0, t1 = 0,6
Y0 = array([A0,B0,C0])

def Fvect(Y,t):
    A, B, C = Y
    return array([-alpha*A, alpha*A-beta*B, beta*B])

def trace_odeint(n,nom_de_fichier):
    les_t = linspace(0,6,n+1)
    les_Y = odeint(Fvect, Y0, les_t)
    plt.clf()
    A = [y[0] for y in les_Y]
    B = [y[1] for y in les_Y]
    C = [y[2] for y in les_Y]
    plt.plot(les_t,A,'-b',label="$A(t)$",linewidth=3)
    plt.plot(les_t,B,'-g',label="$B(t)$",linewidth=3)
    plt.plot(les_t,C,'-r',label="$C(t)$",linewidth=3)
    plt.xlabel('$t$')
    plt.ylabel('Concentrations en fonction de $t$')
    plt.legend()
    plt.title("Odeint avec $"+str(n)+"$ segments")
    plt.savefig(nom_de_fichier)

if __name__ == '__main__':
    les_n  = [5,20,35,50,100]
    for n in les_n :
        trace_odeint(n,'odeint_'+str(n)+'.png')
