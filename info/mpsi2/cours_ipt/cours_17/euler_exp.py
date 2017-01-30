def euler(F, a, b, y0, h):
    """Solution de y'=F(y,t) sur [a,b], y(a) = y0, pas h"""
    y = y0
    t = a
    les_y = [y0] # la liste des valeurs renvoyées
    les_t = [a]
    while t+h <= b:
        # Variant : floor((b-t)/h)
        # Invariant : au tour k, les_y = [y_0,...,y_k], les_t = [t_0,...,t_k]
        y = y + h * F(y, t)
        les_y.append(y)
        t = t + h
        les_t.append(t)
    return les_t, les_y

from math import exp
import matplotlib.pyplot as plt
from numpy import linspace

def Fexp(y,t):
    return y

def trace_exp(h,nom_de_fichier):
    """Résout y'=y, y(0) = 1 sur [0,3]
       par la méthode d'Euler, pas h"""
    les_t, les_y = euler(Fexp, 0, 3, 1, h)
    plt.clf()
    x = linspace(0,3,1000)
    e = [exp(t) for t in x]
    plt.plot(les_t,les_y,'-b',label="Méthode d'Euler",linewidth=3)
    plt.plot(x,e,'-r',label='$\\exp$',linewidth=3)
    plt.legend()
    plt.title("$y'=y$, $y(0) = 1$ sur $[0,3]$, méthode d'Euler de pas $"+str(h)+"$")
    plt.savefig(nom_de_fichier)

if __name__ == '__main__':
    les_h  = [1, 0.1, 0.05, 0.01, 0.001]
    for h in les_h :
        trace_exp(h,'exp_pas_'+str(h)+'.png')
