from math import exp
import matplotlib.pyplot as plt
from numpy import linspace

def euler_for(F, a, b, y0, n):
    """Solution de y'=F(y,t) sur [a,b], y(a) = y0, n segments"""
    y = y0
    les_y = [y0] # la liste des valeurs renvoyées
    les_t = linspace(a,b,n+1)
    h = (b-a)/n
    for t in les_t[1:]:
        # Invariant : si t = les_t[i], les_y = [y_0,...,y_{i-1}]
        y = y + h * F(y, t)
        les_y.append(y)
    return les_t, les_y

alpha = 1
A0 = 1
t0, t1 = 0, 6


def FA(y,t):
    return -alpha*y

def trace_A(n,nom_de_fichier):
    """Résout A'=-alpha*Ay, A(0) = A0 sur [0,6]
       par la méthode d'Euler, n points"""
    les_t, les_A = euler_for(FA, 0, 6, A0, n)
    plt.clf()
    x = linspace(0,6,1000)
    A = [exp(-alpha*t) for t in x]
    plt.plot(les_t,les_A,'-b',label="Méthode d'Euler",linewidth=3)
    plt.plot(x,A,'-r',label='$A$ théorique',linewidth=3)
    plt.legend()
    plt.title("$A'=-\\alpha\\times A$, $A(0) = "+str(A0)+ "$ sur $[0,6]$, méthode d'Euler avec $"+str(n)+"$ segments")
    plt.savefig(nom_de_fichier)

if __name__ == '__main__':
    les_n  = [3,4,5,10,20,100]
    for n in les_n :
        trace_A(n,'A_'+str(n)+'.png')
