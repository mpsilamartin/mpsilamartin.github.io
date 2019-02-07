def euler(F, a, b, y0, h):
    """Solution de y'=F(y,t) sur [a,b], y(a) = y0, pas h"""
    y = y0
    t = a
    y_list = [y0] # la liste des valeurs renvoyées
    t_list = [a]
    while t+h <= b:
        # Variant : floor((b-t)/h)
        # Invariant : au tour k, y_list = [y_0,...,y_k], t_list = [t_0,...,t_k]
        y = y + h * F(y, t)
        y_list.append(y)
        t = t + h
        t_list.append(t)
    return t_list, y_list

def euler_for(F, a, b, y0, n):
    """Solution de y'=F(y,t) sur [a,b], y(a) = y0,
    n segments"""
    h = (b-a) / n
    y = y0
    t = a
    y_list = [y0] # la liste des valeurs renvoyées
    t_list = [a]
    for k in range(n):
        # Invariant : au tour k, y_list = [y_0,...,y_k], t_list = [t_0,...,t_k]
        y = y + h * F(y, t)
        y_list.append(y)
        t = t + h
        t_list.append(t)
    return t_list, y_list

from math import exp
import matplotlib.pyplot as plt
from numpy import linspace
from scipy.integrate import odeint

def Fexp(y,t):
    return y

def trace_exp(h,nom_de_fichier):
    """Résout y'=y, y(0) = 1 sur [0,3]
       par la méthode d'Euler, pas h"""
    t_list, y_list = euler(Fexp, 0, 3, 1, h)
    plt.clf()
    x = linspace(0,3,1000)
    e = [exp(t) for t in x]
    plt.plot(t_list,y_list,'-b',label="Méthode d'Euler",linewidth=3)
    plt.plot(x,e,'-r',label='$\\exp$',linewidth=3)
    plt.legend()
    plt.title("$y'=y$, $y(0) = 1$ sur $[0,3]$, méthode d'Euler de pas $"+str(h)+"$")
    plt.savefig(nom_de_fichier)
    
def trace_exp_odeint(h,nom_de_fichier):
    """Résout y'=y, y(0) = 1 sur [0,3]
       par la méthode d'Euler, pas h"""
    t_list, y_list = euler(Fexp, 0, 3, 1, h)
    y_odeint = odeint(Fexp,1,t_list)
    plt.clf()
    x = linspace(0,3,1000)
    e = [exp(t) for t in x]
    plt.plot(t_list,y_list,'-b',label="Méthode d'Euler",linewidth=3)
    plt.plot(x,e,'-r',label='$\\exp$',linewidth=3)
    plt.plot(t_list,y_odeint,'-m',label="odeint",linewidth=3)
    plt.legend()
    plt.title("$y'=y$, $y(0) = 1$ sur $[0,3]$, méthode d'Euler de pas $"+str(h)+"$")
    plt.savefig(nom_de_fichier)
    
if __name__ == '__main__':
    les_h  = [1, 0.1, 0.05, 0.01, 0.001]
    for i,h in enumerate(les_h) :
        trace_exp(h,'exp_pas_{}.png'.format(i))
        trace_exp_odeint(h,'exp_odeint_pas_{}.png'.format(i))
