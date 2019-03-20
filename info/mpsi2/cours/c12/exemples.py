import numpy as np
import matplotlib.pyplot as plt


def newton(f, fp, x0, n):
    """Zéro de f par la méthode de Newton
    départ : x0, f’ = fp, critère d’arrêt epsilon"""
    u = x0
    v = u - f(u)/fp(u)
    lu=[u]
    for k in range(n):
        u, v = v, v - f(v)/fp(v)
        lu.append(u)
    return u,lu
    
    
def newton2(f, fp, x0, eps):
    """Zéro de f par la méthode de Newton
    départ : x0, f’ = fp, critère d’arrêt epsilon"""
    u = x0
    v = u - f(u)/fp(u)
    lu=[u]
    while abs(v-u)>eps:
        u, v = v, v - f(v)/fp(v)
        lu.append(u)
    return u,lu
    
def dichotomie(f, a, b, epsilon):
    """Zéro de f sur [a,b] à epsilon près, par dichotomie
    Préconditions : f(a) * f(b) <= 0
    f continue sur [a,b]
    epsilon > 0"""
    c, d = a, b
    fc, fd = f(c), f(d)
    while d - c > 2 * epsilon:
        m = (c + d) / 2.
        fm = f(m)
        if fc * fm <= 0:
            d, fd = m, fm
        else:
            c, fc = m, fm
    return (c + d) / 2.
    
def f1(x):
    return x**2-2
    
def fp1(x):
    return 2*x
    
def f2(x):
    return np.sin(x)
    
def fp2(x):
    return np.cos(x)
    
u,y1=newton(f1, fp1,np.float128(2.0),7)
y1=abs(np.array(y1)-np.sqrt(2))

u,y2=newton(f2, fp2,np.float128(2.0),7)
y2=abs(np.array(y2)-np.pi)

u,y3=newton(f2, fp2,np.float128(1.0),7)
y3=abs(np.array(y3)-np.float128(0.0))
y3[-3:]=1e-16

plt.clf()
plt.plot(range(len(y1)),np.log2(y1),'b*-',linewidth=3,markersize=5,label='$f:x\\mapsto x^2-2, u_0=2,l=\\sqrt{2}$')
plt.plot(range(len(y2)),np.log2(y2),'rs-.',linewidth=3,markersize=5,label='$f:x\\mapsto \\sin x, u_0=2,l=\\pi$')
plt.plot(range(len(y3)),np.log2(y3),'go--',linewidth=3,markersize=5,label='$f:x\\mapsto \\sin x, u_0=1,l=0$')
plt.xlabel('$n$')
plt.ylabel('$log_{2}\\vert u_n-l\\vert$')
plt.grid()
plt.legend(loc=0)
plt.savefig('vitesse_convergence_newton.pdf')


#Q1
print("approximation de cos(\pi/10) "+str(np.cos(np.pi/10)))

u1,lu1=newton2(lambda x:16*x**4-20*x**2+5,lambda x:4*16*x**3-2*20*x, 1, 10**(-10))

yth=[2**(-2**n) for n in range(1,len(lu1)+1)]

plt.clf()
plt.semilogy(abs(np.cos(np.pi/10)-lu1),'*-',label='Méthode de Newton')
plt.semilogy(yth,'r--',label='Convergence théorique : $2^{-2^{-n}}$')
plt.xlabel('n')
plt.ylabel('$\\vert u_n-\\cos\\frac{\\pi}{10}\\vert$')
plt.legend()
plt.savefig('ex1.png')


#Q2
print("Nombre d'or "+str((1+np.sqrt(5))/2))

u2,lu2=newton2(lambda x:x**2-x-1,lambda x:2*x-1, 1, 1e-10)

yth=[2**(-2**n) for n in range(7)]

plt.clf()
plt.semilogy(abs((1+np.sqrt(5))/2-lu2),'*-',label='Méthode de Newton')
plt.semilogy(yth,'r--',label='Convergence théorique : $2^{-2^{-n}}$')
plt.xlabel('n')
plt.ylabel('$\\vert u_n-\\frac{1+\\sqrt{5}}{2}\\vert$')
plt.legend()
plt.savefig('ex2.png')

#Q3
def fxp(x,p):
    S=-1
    for k in range(1,p+1):
        S+=x**k
    return S
    
def fxpp(x,p):
    S=0
    for k in range(1,p+1):
        S+=k*x**(k-1)
    return S
    


u3,lu3=newton2(lambda x:fxp(x,3),lambda x:fxpp(x,3), 1, 10**(-10))
u3d=dichotomie(lambda x:fxp(x,3), 0, 1, 10**(-5))

yth=[2**(-2**n) for n in range(1,len(lu3)+1)]

plt.clf()
plt.semilogy(abs(np.roots(3*[1]+[-1])[2]-lu3),'*-')
plt.semilogy(yth,'r--')
plt.savefig('ex3.png')

def plot_fp(p):
    x=np.arange(-10,10,1)
    y=[fxp(xi,p) for xi in x]
    plt.clf()
    plt.plot(x,y)
    plt.plot([-10,10],[0,0],'--')
    plt.savefig('ex31.png')