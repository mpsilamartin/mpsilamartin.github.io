from math import exp
import matplotlib.pyplot as plt
from numpy import linspace, array

alpha , beta = 1, 10
A0, B0, C0 = 1,0,0
t0, t1 = 0,6
Y0 = array([A0,B0,C0])

def Fvect(Y,t):
    A, B, C = Y
    return array([-alpha*A, alpha*A-beta*B, beta*B])

def euler_vectoriel_for(F, a, b, y0, n):
    """Solution de y'=F(y,t) sur [a,b], y(a) = y0, n points"""
    y = y0
    les_y = [y0] # la liste des valeurs renvoyées
    les_t = linspace(a,b,n+1)
    h = (b-a)/n
    for t in les_t[1:]:
        # Invariant : si t = les_t[i],, les_y = [y_0,...,y_{i-1}]
        y = y + h * F(y, t) # Et surtout pas += !
        les_y.append(y)
    return les_t, les_y

vect_t, vect_Y = euler_vectoriel_for(Fvect, t0,t1, Y0, 4)

def trace_vect(n,nom_de_fichier):
    les_t, les_Y = euler_vectoriel_for(Fvect, 0, 6, Y0, n)
    plt.clf()
    A = [y[0] for y in les_Y]
    B = [y[1] for y in les_Y]
    C = [y[2] for y in les_Y]
    plt.plot(les_t,A,'-b',label="$A(t)$",linewidth=3)
    plt.plot(les_t,B,'-g',label="$B(t)$",linewidth=3)
    plt.plot(les_t,C,'-r',label="$C(t)$",linewidth=3)
    plt.xlabel('$t$')
    plt.ylabel('Concentrations en fonction de $t$')
    plt.legend()
    plt.title("Méthode d'Euler vectorielle avec $"+str(n)+"$ segments")
    plt.savefig(nom_de_fichier)

if __name__ == '__main__':
    les_n  = [5,20,35,50,100,1000]
    for n in les_n :
        trace_vect(n,'vect_'+str(n)+'.png')
