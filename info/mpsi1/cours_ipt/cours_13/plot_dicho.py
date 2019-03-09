from math import sqrt, sin, pi
import matplotlib.pyplot as plt

def carre(x):
    """Renvoie x**2-2"""
    return x**2-2
    
def dichotomie(f, a, b, epsilon):
    """Zéro de f sur [a,b] à epsilon près, par dichotomie"""
    c, d = a, b
    fc, fd = f(c), f(d)
    while d - c > 2 * epsilon:
        # Inv : fc*fd <=0
        m = (c + d) / 2.
        fm = f(m)
        if fc * fm <= 0:
            d, fd = m, fm
        else:
            c, fc = m, fm
    return (c + d) / 2.
    
def dicho_for(f, a, b, n):
    """Zéro de f sur [a,b] à epsilon près, par dichotomie"""
    c, d = a, b
    fc, fd = f(c), f(d)
    mil_list = [(c+d) / 2.] # liste des milieux des segments
    for i in range(n):
        m = (c + d) / 2.
        fm = f(m)
        if fc * fm <= 0:
            d, fd = m, fm
        else:
            c, fc = m, fm
        mil_list.append((c+d)/2.)
    return mil_list
    
def plot_dicho(nom_de_fichier,n):
    carre_x = dicho_for(carre,1,2,n)
    carre_y = [max(abs(t - sqrt(2)),10**-16) for t in carre_x]
    sin_x = dicho_for(sin,3,4,n)
    sin_y = [max(abs(t - pi),10**-16) for t in sin_x]
    les_n = [i for i in range(n+1)]
    maj_theorique = [1/2**(i+1) for i in range(n+1)]
    plt.clf()
    plt.plot(les_n,carre_y,'-ob',linewidth=3,label="Équation $x^2=2$ sur $[1,2]$")
    plt.plot(les_n,sin_y,'-xr',linewidth=3,label="Équation $\\sin(x)=0$ sur $[3,4]$")
    plt.plot(les_n,maj_theorique,'-g',linewidth=3,label="Majoration théorique")
    plt.yscale('log')
    plt.xlabel('$n$')
    plt.ylabel("Erreur d'approximation après $n$ itérations")
    plt.title('Méthode de la dichotomie, vitesse de convergence')
    plt.legend(loc=0)
    plt.savefig(nom_de_fichier)
    
if __name__ == '__main__':
    plot_dicho('dichotomie.png',52)
