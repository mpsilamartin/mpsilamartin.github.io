import matplotlib.pyplot as plt
from numpy import linspace, array
from scipy.integrate import odeint

m = 250
omega = 1
k = 1000
c = 100
y0,yp0 = 1,0
a,b = 0,20

def F(X,t):
    y,yp = X
    ypp = (-c*yp-k*y) / m
    return array([yp,ypp])
    
X0 = array([y0,yp0])# Condition initiale

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

def trace_oscillations(h,nom_de_fichier):
    """Résout my''+cy'+ky=0, y(0) = 1, y'(0)=0 sur [0,20]
       par la méthode d'Euler, pas h"""
    les_t, les_X = euler(F, a, b, X0, h)
    plt.clf()
    les_y = [X[0] for X in les_X]
    x = linspace(a,b,1000)
    les_E = odeint(F,X0,x)
    les_e = [X[0] for X in les_E] 
    plt.plot(les_t,les_y,'-b',label="Méthode d'Euler, pas $"+str(h)+"$",linewidth=3)
    plt.plot(x,les_e,'-r',label='Par odeint',linewidth=3)
    plt.xlabel("$t$ en $s$")
    plt.ylabel("$y(t)$ en $m$")
    plt.legend()
    plt.title("$my''(t)+cy'(t)+ky(t)=0$, $y(0) = 1$, $y'(0) = 0$, sur $[0,20]$")
    plt.savefig(nom_de_fichier)
    
def trace_phase_oscillations(h,nom_de_fichier):
    """Résout my''+cy'+ky=0, y(0) = 1, y'(0)=0 sur [0,20]
       par la méthode d'Euler, pas h"""
    _, les_X = euler(F, a, b, X0, h)
    plt.clf()
    les_y = [X[0] for X in les_X]
    les_yp = [X[1] for X in les_X]
    x = linspace(a,b,1000)
    les_E = odeint(F,X0,x)
    les_e = [X[0] for X in les_E]
    les_ep = [X[1] for X in les_E] 
    plt.plot(les_y,les_yp,'-b',label="Méthode d'Euler, pas $"+str(h)+"$",linewidth=3)
    plt.plot(les_e,les_ep,'-r',label='Par odeint',linewidth=3)
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
