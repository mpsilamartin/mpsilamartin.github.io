from math import exp
import matplotlib.pyplot as plt
from numpy import linspace, array

def euler_for(F, a, b, y0, n):
    """Solution de y'=F(y,t) sur [a,b], y(a) = y0, n points"""
    y = y0
    les_y = [y0] # la liste des valeurs renvoyées
    les_t = linspace(a,b,n+1)
    h = (b-a)/n
    for t in les_t[1:]:
        # Invariant : si t = les_t[i], les_y = [y_0,...,y_{i-1}]
        y += h * F(y, t)
        les_y.append(y)
    return les_t, les_y

alpha , beta = 1, 10
A0, B0, C0 = 1,0,0
t0, t1 = 0,6
n = 3
Y0 = array([A0,B0,C0])

def Fvect(Y,t):
    A, B, C = Y
    return array([-alpha*A, alpha*A-beta*B, beta*B])

les_t, les_Y = euler_for(Fvect, t0,t1, Y0, n)
