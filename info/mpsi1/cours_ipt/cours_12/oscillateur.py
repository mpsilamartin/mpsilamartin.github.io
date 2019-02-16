import matplotlib.pyplot as plt
from numpy import linspace, array
from scipy.integrate import odeint

m = 250 # kg 
k = 1000 # kg * s**-2
c = 100 # kg * s**-1
y0,yp0 = 1,0 # m, m*s**-1
a,b = 0,20 # s,s

def F(X,t):
    y,yp = X
    ypp = (-c*yp-k*y) / m
    return array([yp,ypp])
    
X0 = array([y0,yp0])# Condition initiale

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

def trace_oscillations(h,nom_de_fichier):
    """Résout my''+cy'+ky=0, y(0) = 1, y'(0)=0 sur [0,20]
       par la méthode d'Euler, pas h"""
    t_list, X_list = euler(F, a, b, X0, h)
    plt.clf()
    y_list = [X[0] for X in X_list]
    x = linspace(a,b,1000)
    E_list = odeint(F,X0,x)
    e_list = [X[0] for X in E_list] 
    plt.plot(t_list,y_list,'-b',label="Méthode d'Euler, pas $"+str(h)+"$",linewidth=3)
    plt.plot(x,e_list,'-r',label='Par odeint',linewidth=3)
    plt.xlabel("$t$ en $s$")
    plt.ylabel("$y(t)$ en $m$")
    plt.legend()
    plt.title("$my''(t)+cy'(t)+ky(t)=0$, $y(0) = 1$, $y'(0) = 0$, sur $[0,20]$")
    plt.savefig(nom_de_fichier)
    
def trace_phase_oscillations(h,nom_de_fichier):
    """Résout my''+cy'+ky=0, y(0) = 1, y'(0)=0 sur [0,20]
       par la méthode d'Euler, pas h"""
    _, X_list = euler(F, a, b, X0, h)
    plt.clf()
    y_list = [X[0] for X in X_list]
    yp_list = [X[1] for X in X_list]
    x = linspace(a,b,1000)
    E_list = odeint(F,X0,x)
    e_list = [X[0] for X in E_list]
    ep_list = [X[1] for X in E_list] 
    plt.plot(y_list,yp_list,'-b',label="Méthode d'Euler, pas $"+str(h)+"$",linewidth=3)
    plt.plot(e_list,ep_list,'-r',label='Par odeint',linewidth=3)
    plt.xlabel("$y(t)$ en $m$")
    plt.ylabel("$y'(t)$ en $m s^{-1}$")
    plt.legend()
    plt.title("$my''(t)+cy'(t)+ky(t)=0$, $y(0) = 1$, $y'(0) = 0$, sur $[0,20]$")
    plt.savefig(nom_de_fichier)

if __name__ == '__main__':
    les_h  = [1, 0.1, 0.05, 0.01, 0.001]
    for i,h in enumerate(les_h) :
        trace_oscillations(h,'oscillations_pas_{}.png'.format(i))
    for i,h in enumerate(les_h) :
        trace_phase_oscillations(h,'phase_oscillations_pas_{}.png'.format(i))
