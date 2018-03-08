import matplotlib.pyplot as plt
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
    y,yp,ypp = X
    yppp = (5-9*(t**2)*ypp-18*t*yp-6*y)/t**3
    return array([yp,ypp,yppp])

   
def plot_solutions(nom_de_fichier,b,n):
    X0 = array([2,0,0])
    les_t,les_X_euler = euler(F,1,b,X0,(b-1)/n)
    les_y_euler = [X[0] for X in les_X_euler]
    les_x_odeint = linspace(1,b,n)
    les_X_odeint = odeint(F,X0,les_x_odeint)
    les_y_odeint = [X[0] for X in les_X_odeint]
    plt.clf()
    plt.plot(les_t,les_y_euler,label="Méthode d'Euler")
    plt.plot(les_x_odeint,les_y_odeint,label="Odeint")
    plt.title("Équation $t^3y'''+9t^2y''+18ty+6y=5$, $y(0)=2$n $y'(0)=y''(0)=0$, $"+str(n)+"$ segments")
    plt.legend(loc=0)
    plt.ylim(1.84,2.1)
    plt.savefig(nom_de_fichier)
    
if __name__ == '__main__':
    plot_solutions('exo_19_0_2_3.png',2,10)
