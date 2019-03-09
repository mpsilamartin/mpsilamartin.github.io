import matplotlib.pyplot as plt
from math import exp
from numpy import array,linspace
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
    
def F(X,t):
    y,yp = X
    ypp = 5-2*yp-y
    return array([yp,ypp])
    
def y(x):
    return (x-2)*exp(-x)+5    
   
def plot_solutions(nom_de_fichier,n):
    x_list = linspace(0,10,1000)
    y_list = [y(t) for t in x_list]
    X0 = array([3,3])
    t_list,X_list_euler = euler(F,0,10,X0,10/n)
    y_list_euler = [X[0] for X in X_list_euler]
    X_list_odeint = odeint(F,X0,t_list)
    y_list_odeint = [X[0] for X in X_list_odeint]
    plt.clf()
    plt.plot(x_list,y_list,label="Solution exacte")
    plt.plot(t_list,y_list_euler,label="Méthode d'Euler")
    plt.plot(x_list_odeint,y_list_odeint,label="Odeint")
    plt.title("$y''+2y'+y=5$, $y(0)=y'(0)=3$, ${}$ segments".format(n))
    plt.legend(loc=0)
    plt.savefig(nom_de_fichier)
    
if __name__ == '__main__':
    plot_solutions('exo_8_0_2_1.png',10)
