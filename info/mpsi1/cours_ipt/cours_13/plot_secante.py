from math import cos, sin, log, sqrt, pi
import matplotlib.pyplot as plt

def secante(f, x0, x1, eps):
    """Zéro de f par la méthode de la sécante
       départ : x0, x1, , critère d'arrêt epsilon"""
    u,v = x0,x1
    while abs(v-u) > eps:
        p = (f(u)-f(v))/(u-v)
        u, v = v, v - f(v)/p
    return v

def carre(x):
    """Renvoie x**2-2"""
    return x**2-2

def carrep(x):
    """Renvoie 2*x"""
    return 2*x

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
    
def secante_for(f, x0 ,x1 , n):
    """Zéro de f par la méthode de la sécante
       départ : x0, f' = fp, n pas"""
    les_x = [x0]
    u,v = x0,x1
    for i in range(n):
        p = (f(u)-f(v)) / (u-v)
        u,v = v,u - f(u)/p
        les_x.append(u)
    return les_x

def plot_newton_secante(nom_de_fichier,n):
    newton_x = newton_for(carre,carrep,2,n)
    newton_y = [max(abs(t - sqrt(2)),10**-16) for t in newton_x]
    secante_x = secante_for(carre,2,1,n)
    secante_y = [max(abs(t - sqrt(2)),10**-16) for t in secante_x]
    les_n = [i for i in range(n+1)]
    plt.clf()
    plt.plot(les_n,newton_y,'-ob',linewidth=3,label="Méthode de Newton, $x_0=2$")
    plt.plot(les_n,secante_y,'-+r',linewidth=3,label="Méthode de la sécante, $x_0=2$, $x_1=1$")
    plt.yscale('log')
    plt.xlabel('$n$')
    plt.ylabel("Erreur d'approximation après $n$ itérations")
    plt.title("Comparaison Newton-sécante pour l'équation $x^2=2$")
    plt.legend(loc=0)
    plt.savefig(nom_de_fichier)



if __name__ == '__main__':
    plot_newton_secante('newton_secante.png',8)
