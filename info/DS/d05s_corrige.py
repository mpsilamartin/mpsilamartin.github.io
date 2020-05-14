import numpy as np
import matplotlib.pyplot as plt

alpha=32

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
    return np.sqrt(1+4*x**2)


n=1000

print('Q1 : '+str(rect_gauche(f,0,alpha,1000)))
print('Q2 : '+str(rect_droit(f,0,alpha,1000)))
print('Q3 : '+str(trapeze(f,0,alpha,1000)))

#Exercice 2

def proie_seule(u,t):
    return a*u



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



u0=alpha
v0=alpha+10
a=alpha*1e-2
b=alpha*1e-3
c = alpha*1e-2
d = 0.2*alpha*1e-3
t0,t1,h = 0,20,.01

# Question 4 : Donner la population de la proie au bout de 20 unités de temps.

t_list,A_list = euler(proie_seule,t0,t1,u0,h)
print('Q4 : '+str(A_list[-1]))



# Question 2 Donner la population de proies et prédateurs au bout de 300 unités de temps.

def proie_predateur(X,t):
    u,v = X
    return np.array([u*(a-b*v),-v*(c-d*u)])

#
X0 = np.array([u0,v0])
t_list, X_list = euler(proie_predateur,0,300,X0,h)

print('Q5 : '+str(X_list[-1][0]))
print('Q6 : '+str(X_list[-1][1]))



u_list = [X[0] for X in X_list]
v_list = [X[1] for X in X_list]
plt.clf()

plt.plot(t_list,u_list,label='Proie')
plt.plot(t_list,v_list,label='Prédateur')

plt.xlabel('Temps ($s$)')
plt.ylabel('Population')
plt.grid()
plt.savefig('proie_predateur.png')