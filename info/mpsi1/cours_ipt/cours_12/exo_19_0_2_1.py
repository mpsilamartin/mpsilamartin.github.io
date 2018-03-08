import matplotlib.pyplot as plt
from math import exp
from numpy import array,linspace
from scipy.integrate import odeint

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
    
def F(X,t):
    y,yp = X
    ypp = 5-2*yp-y
    return array([yp,ypp])
    
def y(x):
    return (x-2)*exp(-x)+5    
   
def plot_solutions(nom_de_fichier,n):
    les_x = linspace(0,10,1000)
    les_y = [y(t) for t in les_x]
    X0 = array([3,3])
    les_t,les_X_euler = euler(F,0,10,X0,10/n)
    les_y_euler = [X[0] for X in les_X_euler]
    les_x_odeint = linspace(0,10,n)
    les_X_odeint = odeint(F,X0,les_x_odeint)
    les_y_odeint = [X[0] for X in les_X_odeint]
    plt.clf()
    plt.plot(les_x,les_y,label="Solution exacte")
    plt.plot(les_t,les_y_euler,label="Méthode d'Euler")
    plt.plot(les_x_odeint,les_y_odeint,label="Odeint")
    plt.title("Équation $y''+2y'+y=5$, $y(0)=y'(0)=3$, $"+str(n)+"$ segments")
    plt.legend(loc=0)
    plt.savefig(nom_de_fichier)
    
if __name__ == '__main__':
    plot_solutions('exo_19_0_2_1.png',10)
