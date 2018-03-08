from math import cos, sin, log, sqrt, pi
import matplotlib.pyplot as plt

def newton(f, fp, x0, eps):
    """Zéro de f par la méthode de Newton
       départ : x0, f' = fp, n pas"""
    u = x0
    v = u - f(u)/fp(u)
    while abs(u-v) > eps
        u, v = v, v - f(v)/fp(v)
    return u

def carre(x):
    """Renvoie x**2-2"""
    return x**2-2

def carrep(x):
    """Renvoie 2*x"""
    return 2*x
    
def msin(x):
    """Renvoie -sin(x)"""
    return -sin(x)

def newton_for(f, fp, x0, n):
    """Zéro de f par la méthode de Newton
       départ : x0, f' = fp, n pas"""
    les_x = [x0]
    u = x0
    v = u - f(u)/fp(u)
    for i in range(n):
        u, v = v, v - f(v)/fp(v)
        les_x.append(u)
    return les_x

def plot_newton(nom_de_fichier,n):
    carre_x = newton_for(carre,carrep,2,n)
    carre_y = [max(abs(t - sqrt(2)),10**-16) for t in carre_x]
    cos_x = newton_for(cos,msin,2,n)
    cos_y = [max(abs(t - pi/2),10**-16) for t in cos_x]
    les_n = [i for i in range(n+1)]
    plt.clf()
    plt.plot(les_n,carre_y,'-ob',linewidth=3,label="Équation $x^2=2$, $x_0=2$")
    plt.plot(les_n,cos_y,'-+r',linewidth=3,label="Équation $\\cos(x)=0$, $x_0=2$")
    plt.yscale('log')
    plt.xlabel('$n$')
    plt.ylabel("Erreur d'approximation après $n$ itérations")
    plt.title('Méthode de Newton, vitesse de convergence')
    plt.legend(loc=0)
    plt.savefig(nom_de_fichier)

def dicho_for(f, a, b, n):
    """Zéro de f sur [a,b] à epsilon près, par dichotomie"""
    c, d = a, b
    fc, fd = f(c), f(d)
    mil = [(c+d) / 2.]
    for i in range(n):
        m = (c + d) / 2.
        fm = f(m)
        if fc * fm <= 0:
            d, fd = m, fm
        else:
            c, fc = m, fm
        mil.append((c+d)/2.)
    return mil

def plot_carre10(nom_de_fichier,n):
    n_x = newton_for(carre,carrep,2,n)
    n_y = [max(abs(t - sqrt(2)),10**-16) for t in n_x]
    d_x = dicho_for(carre,1,2,n)
    d_y = [max(abs(t - sqrt(2)),10**-16) for t in d_x]
    les_n = [i for i in range(n+1)]
    plt.clf()
    plt.plot(les_n,n_y,'-ob',linewidth=3,label='Newton, $x_0=2$')
    plt.plot(les_n,d_y,'-+r',linewidth=3,label='Dichotomie sur $[1,2]$')
    plt.yscale('log')
    plt.xlabel('$n$')
    plt.ylabel("Erreur d'approximation après $n$ itérations")
    plt.title("Comparaison Newton - Dichotomie pour l'équation $x^2=2$")
    plt.legend(loc=0)
    plt.savefig(nom_de_fichier)


if __name__ == '__main__':
    plot_newton('newton_carre_cos.png',8)
    plot_carre10('dicho_vs_newton_carre_decimale.png',8)
