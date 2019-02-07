import numpy as np
import matplotlib.pyplot as plt

def Rg(f,a,b,N):
    """Approximation de l’intégrale de a à b de f
    Méthode des rectangles à gauche, N rectangles"""
    S = 0
    h = (b-a)/N
    for k in range(N) :
        S = S + f(a + k*h)
    return S*h
    
def Rd(f,a,b,N):
    """Approximation de l’intégrale de a à b de f
    Méthode des rectangles à droite, N rectangles"""
    S = 0
    h = (b-a)/N
    for k in range(1,N+1) :
        S = S + f(a + k*h)
    return S*h
    
def T(f,a,b,N):
    """Approximation de l’intégrale de a à b de f
    Méthode des trapèzes, N trapèzes"""
    S = 0.5*(f(a) + f(b))
    h = (b-a)/N
    for k in range(1,N) :
        S = S + f(a + k*h)
    return S*h

IRG=[]
IRD=[]
IT=[]

#f=lambda x:x**2
def f(x):
    return x**2

N=np.linspace(1,200,200)

for vn in N:
    IRG.append(Rg(f,0,1,int(vn)))
    IRD.append(Rd(f,0,1,int(vn)))
    IT.append(T(f,0,1,int(vn)))
    
plt.clf()
plt.loglog(1/N,abs(np.array(IRG)-1/3),label='Méthode des rectangles à gauche')
plt.loglog(1/N,abs(np.array(IRD)-1/3),label='Méthode des rectangles à droite')
plt.loglog(1/N,abs(np.array(IT)-1/3),label='Méthode des trapèzes')
#plt.log(N,1/3*np.ones(len(N)),'k--',label='Valeur exacte')
plt.xlabel('n')
plt.ylabel('Approximation de $\int_0^1t^2dt$')
plt.legend(loc='best')
plt.show()
    
