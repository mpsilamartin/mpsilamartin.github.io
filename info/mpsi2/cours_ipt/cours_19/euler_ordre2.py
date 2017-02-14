from math import cos
import matplotlib.pyplot as plt
from numpy import linspace, array

def euler_vectoriel(F, a, b, y0, h):
    """Solution de y'=F(y,t) sur [a,b], y(a) = y0, pas h"""
    y = y0
    t = a
    les_y = [y0] # la liste des valeurs renvoyées
    les_t = [a]
    while t+h <= b:
        # Variant : floor((b-t)/h)
        # Invariant : au tour k, les_y = [y_0,...,y_k], les_t = [t_0,...,t_k]
        y = y + h * F(y, t) # surtout pas += !
        les_y.append(y)
        t += h
        les_t.append(t)
    return les_t, les_y

m = 250 # kg
omega = 1 # s ** (-1)
alpha = 0 # N
k = 1000 # N / m
# c = 500 # N * m * s**(-1)
y0 = 1 # m
yp0 = 0 # m . s**(-1)
t0 = 0
t1 = 20 # s
# n = 1000
# h = float(t1 - t0) / n


def trace_amortisseur(c,n,nom_de_fichier):
    h = float(t1 - t0) / n # Pas temporel
    def F(Y, t) :
        y, yp = Y
        ypp = (-c*yp - k*y + alpha*cos(omega*t)) / m
        return array([yp, ypp])
    les_t, les_y = euler_vectoriel(F, t0, t1, array([y0, yp0]), h)
    y = [x[0] for x in les_y] # Liste des positions
    plt.clf()
    plt.plot(les_t,y,label='Mobile',linewidth=3)
    plt.legend()
    plt.title('Amortisseur, $c={}$, $n={}$'.format(c,n))
    plt.savefig(nom_de_fichier)

def trace_phase_amortisseur(c,n,nom_de_fichier):
    h = float(t1 - t0) / n
    def F(Y, t) :
        y, yp = Y
        ypp = (-c*yp - k*y + alpha*cos(omega*t)) / m
        return array([yp, ypp])
    les_t, les_y = euler_vectoriel(F, t0, t1, array([y0, yp0]), h)
    y = [x[0] for x in les_y] # Liste des positions
    yp = [x[1] for x in les_y] # Liste des vitesses
    plt.clf()
    plt.plot(y,yp,label='Mobile',linewidth=3)
    plt.legend()
    plt.title('Portrait de phase, amortisseur, $c={}$, $n={}$'.format(c,n))
    plt.savefig(nom_de_fichier)

if __name__ == '__main__':
    les_c = [0,100,200,400,600,1000,1200]
    les_n = [10,100,1000,10000]
    for c in les_c :
        for n in les_n :
            trace_amortisseur(c,n,'amortisseur_c{}_n{}.png'.format(c,n))
            trace_phase_amortisseur(c,n,'phase_c{}_n{}.png'.format(c,n))

