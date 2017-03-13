import matplotlib.pyplot as plt
from math import sqrt,log

def sqrt1(a,u0,eps=10**(-10)):
    """Racine carrée de a par la méthode de Newton"""
    u = u0
    v = 0.5*(u+a/u)
    while abs(u-v) > eps:
        u,v = v, 0.5*(v+a/v)
    return v

def sqrt2(a,u0,eps=10**(-10)):
    """Racine carrée de a par la méthode de Newton"""
    u = u0
    v = 0.5*u*(3-a*u**2)
    while abs(u-v) > eps:
        u,v = v, 0.5*v*(3-a*v**2)
    return a*v

def secante(f,u0,u1,eps=10**-10):
    """Solution de f(x)=0 par la méthode de la sécante"""
    u,v = u0,u1
    while abs(u-v)>eps:
        u,v = v, v-f(v)*(v-u)/(f(v)-f(u))
    return v

def carre(a):
    """Renvoie x -> x**2-a"""
    return lambda x : x**2-a

def log10(x):
    """Troncature de log_10(x) à 10**-16"""
    if x < 1e-15 :
        return -16
    else :
        return log(x,10)

def plot_sqrt(a,n,u0,u1,nom_de_fichier):
    """Compare ces trois méthodes jusqu'au rang n"""
    # Liste des abscisses
    les_k = range(0,n+1)
    # Liste des ordonnées pour sqrt1
    u,v = u0, 0.5*(u0+a/u0)
    les_sqrt1 = [] 
    for k in range(n+1):
        les_sqrt1.append(log10(abs(u-sqrt(a))))
        u,v = v, 0.5*(v+a/v)
    # Liste des ordonnées pour sqrt2
    u = 1/sqrt(u0)
    v = 0.5*u*(3-a*u**2)
    les_sqrt2 = [] 
    for k in range(n+1):
        les_sqrt2.append(log10(abs(abs(a*u)-sqrt(a))))
        u,v = v, 0.5*v*(3-a*v**2)
    # Liste des ordonnées pour sécante
    f = carre(a)
    u,v = u0,u1
    les_secante=[]
    for k in range(n+1):
        les_secante.append(log10(abs(u-sqrt(a))))
        if u == v:
            u,v = u,v
        else :
            u,v = v, v-f(v)*(v-u)/(f(v)-f(u))
    # Tracé
    plt.clf()
    plt.plot(les_k,les_sqrt1,linewidth=3,label='Méthode de Newton, sqrt1')
    plt.plot(les_k,les_sqrt2,linewidth=3,label='Méthode de Newton, sqrt2')
    plt.plot(les_k,les_secante,linewidth=3,label='Méthode de la sécante')
    plt.xlabel('$n$')
    plt.ylabel('$\\log_{10}\\left| u_n-\\sqrt{'+str(a)+'} \\right|$')
    plt.title('Comparaison de plusieurs méthodes de calcul de $\\sqrt{'+str(a)+'}$')
    plt.legend(loc=0)
    plt.savefig(nom_de_fichier)
        
if __name__ == '__main__':
    plot_sqrt(2,10,1.5,1,'comparaisons_sqrt2.png')

