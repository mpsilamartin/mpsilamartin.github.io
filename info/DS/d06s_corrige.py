import numpy as np
import matplotlib.pyplot as plt

alpha=43
L=alpha
m=1+0.01*alpha
theta0=np.pi/(4*alpha)
g=9.81

#Exercice 1
def rect_gauche(f,a,b,n):
    h=(b-a)/n
    S=0
    for k in range(n):
        S+=f(a+k*h)
    return S*h

def rect_droit(f,a,b,n):
    h=(b-a)/n
    S=0
    for k in range(1,n+1):
        S+=f(a+k*h)
    return S*h

def trapeze(f,a,b,n):
    h=(b-a)/n
    S=0.5*(f(a)+f(b))
    for k in range(1,n):
        S+=f(a+k*h)
    return S*h

def f(x):
    return 4/np.sqrt(2*g/L*(np.cos(x)-np.cos(theta0)))


n=10
Tg=rect_gauche(f,0,theta0,100)
Td=rect_droit(f,0,theta0-theta0/1000,100)
Tt=trapeze(f,0,theta0-theta0/1000,100)
T_0=np.sqrt(L/g)*2*np.pi

print('Q1 : '+str(np.sqrt(L/g)*2*np.pi))
print('Q2 : '+str(rect_gauche(f,0,theta0,100)))
print('Q3 : '+str(rect_droit(f,0,theta0-theta0/1000,100)))
print('Q4 : '+str(trapeze(f,0,theta0-theta0/1000,100)))
print("Q5 - epsG",abs(Tg-T_0))
print("Q5 - epsD",abs(Td-T_0))
print("Q5 - epst",abs(Tt-T_0))

#Exercice 2

# declaration des fonctions
from scipy.integrate import odeint

def euler(F, a, b, y0, h):
    """Solution de y'=F(y,t) sur [a,b], y(a) = y0, pas h"""
    y = y0
    t = a
    y_list = [y0]
    t_list = [a]
    while t+h <= b:

        y = y + h * F(y, t)
        y_list.append(y)
        t = t + h
        t_list.append(t)
    return t_list, y_list

def F(X,t):
    vm=1.5+alpha/100
    vc=8.0
    vecteur_CM=np.array([vm*t-X[0],-X[1]])
    return vc*vecteur_CM/np.linalg.norm(vecteur_CM)

# programme principal

X0=np.array([100+alpha*m,300+alpha*m])
X0=np.array([100+alpha,300+alpha])
t=np.linspace(0,38,100)
t_list, X_list=euler(F,0,38,X0,38/100)
X=[x[0] for x in X_list]
Y=[x[1] for x in X_list]
#plt.axis([0,100,0,300])
plt.plot(X,Y)
#plt.savefig('trajectoire_du_chien.png')
#plt.show()

print('Q5 : '+str(X0))
print('Q6 : '+str(X[-1]))
print('Q7 : '+str(Y[-1]))