import scipy.optimize as so
import scipy.integrate as si
from math import sqrt, sin, cos, atan
from numpy import array
import numpy as np

alpha = 5
print("alpha = ",alpha)


def trapeze(f,a,b,n):
    h=(b-a)/n
    S=0.5*(f(a)+f(b))
    for k in range(1,n):
        S+=f(a+k*h)
    return S*h

def dichotomie(f, a, b, epsilon):
    """Zéro de f sur [a,b] à epsilon près, par dichotomie
       Préconditions : f(a) * f(b) <= 0
                       f continue sur [a,b]
                       epsilon > 0"""
    c, d = a, b
    fc, fd = f(c), f(d)
    k=0
    while d - c > 2 * epsilon:
        m = (c + d) / 2.
        fm = f(m)
        if fc * fm <= 0:
            d, fd = m, fm
        else:
            c, fc = m, fm
        k+=1
    return (c + d) / 2.,k

def newton(f, fp, x0, epsilon):
    """Zéro de f par la méthode de Newton
       départ : x0, f' = fp, critère d'arrêt epsilon"""
    u = x0
    v = u - f(u)/fp(u)
    k=0
    while abs(v-u) > epsilon:
        u, v = v, v - f(v)/fp(v)
        k+=1
    return u,k

#Qu. 1 :
print("Qu. 1 : ", trapeze(lambda x : cos(sqrt(x)),alpha,alpha+1,1000))

# Qu. 2 :

def f2(t):
    return t**2+t**0.5-10-alpha

def f2p(t):
    return 2*t+0.5*t**(-0.5)

print("Qu. 2 : méthode de Newton ", newton(f2,f2p,alpha,1e-5)[0])


print("Qu. 2 : méthode de dichotomie ", dichotomie(f2, 0, 12+alpha, 1e-5)[0])

# print("Qu. 2 : méthode de brentq ", so.brentq(lambda x : x**2 + sqrt(x) -10 -alpha,3,11))

# Qu. 3 :
print("Qu. 3 : méthode de Newton ", newton(f2,f2p,alpha,1e-5)[1])
# Qu. 4 :
print("Qu. 4 : méthode de dichotomie ", dichotomie(f2, 0, 12+alpha, 1e-5)[1])

# Qu. 5 :
# print("Qu. 5 : ", so.brentq(lambda t : trapeze(lambda x : 2+sqrt(x)+cos(x),alpha,alpha+t,1000)-10,0,50))
#
# print("Qu. 5 : ", so.brentq(lambda t : trapeze(lambda x : 2+sqrt(x)+cos(x),alpha,alpha+t,100000)-10,0,50))
#
# print("Qu. 5 : ", dichotomie(lambda t : trapeze(lambda x : 2+sqrt(x)+cos(x),alpha,alpha+t,100000)-10,0,50,1e-5))

print("Qu. 5 : ", dichotomie(lambda t : trapeze(lambda x : 2+sqrt(x)+cos(x),alpha,alpha+t,1000)-10,0,50,1e-5))

# Qu. 6 :

def F (x,t) :
    return 3*cos(x) + t

les_t = [i/10000 for i in range(10001)]

print("Qu. 6 : ", si.odeint(F,alpha,les_t)[-1,0])


# Qu. 7 :

def G (X,t) :
    a,b = X[0],X[1]
    return array([b,1+sin(t+a)])

les_t = [i*(1+alpha/10)/10000 for i in range(10001)]

print("Qu. 7 : ", si.odeint(G,array([0,0]),les_t)[-1,0])
#
#
#
# Qu. 6 :
#
# print("Qu. 6 : ", si.odeint(G,array([0,1]),les_t)[-1,0])
#


# Qu. 8 :

def H (X,t) :
    a,b = X[0],X[1]
    return array([b,1+atan(t+a)])

les_t = [i*(1+alpha/10)/10000 for i in range(10001)]

f = lambda beta : si.odeint(H,array([0,beta]),les_t)[-1,0]-1-(2/3)*alpha

print("Qu. 8 : ",so.brentq(f,-2,2))


# Qu. 9 :

A=array([[0,1,32,243],[1,32,243,1024],[32,243,1024,3125],[243,1024,3125,7776]])
B=array([[1],[2],[3],[alpha]])

X=np.linalg.solve(A,B)

print("Qu. 9 : ",X[0][0])

# Qu. 10 :
B=np.dot(A,np.dot(A,A))
print("Qu. 10 : ",B[0][0]%(10000+alpha))
# Ap=A
# Ap[0,0]=alpha









