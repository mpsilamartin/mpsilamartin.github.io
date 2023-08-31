import matplotlib.pyplot as plt
from numpy import linspace
from scipy.integrate import odeint

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

def F(y,t):
    return -y**2 + t

def trace(h,nom_de_fichier):
    """Résout y'(t)=-y(t)**2 + t, y(0) = 1 sur [0,1]
       par la méthode d'Euler, pas h"""
    les_t, les_y = euler(F, 0, 1, 1, h)
    plt.clf()
    x = linspace(0,1,1000)
    e = odeint(F,1,x)
    plt.plot(les_t,les_y,'-b',label="Méthode d'Euler",linewidth=3)
    plt.plot(x,e,'-r',label='Par odeint',linewidth=3)
    plt.legend()
    plt.title("$y'(t)=-y^2(t)+t$, $y(0) = 1$ sur $[0,1]$, méthode d'Euler de pas $"+str(h)+"$")
    plt.savefig(nom_de_fichier)

if __name__ == '__main__':
    les_h  = [1, 0.1, 0.05, 0.01, 0.001]
    for i,h in enumerate(les_h) :
        trace(h,'exo_pas_{}.png'.format(i))
