from math import cos, pi, log
import matplotlib.pyplot as plt
from numpy import linspace
from scipy.integrate import quad

def Rg(f,a,b,N):
    """Approximation de l'intégrale de a à b de f 
    Méthode des rectangles à gauche, N rectangles"""
    S = 0
    h = (b-a)/N
    for k in range(N) : 
        S = S + f(a + k*h)
    return S*h

def Rd(f,a,b,N):
    """Approximation de l'intégrale de a à b de f 
    Méthode des rectangles à droite, N rectangles"""
    S = 0
    h = (b-a)/N
    for k in range(1,N+1) : 
        S = S + f(a + k*h)
    return S*h

def T(f,a,b,N):
    """Approximation de l'intégrale de a à b de f 
    Méthode des trapèzes, N trapèzes"""
    S = 0.5*(f(a) + f(b))
    h = (b-a)/N
    for k in range(1,N) : 
        S = S + f(a + k*h)
    return S*h

def S(f,a,b,N):
    """Approximation de l'intégrale de a à b de f 
    Méthode de Simpson, N polynomes"""
    h = (b-a)/N
    S = f(a) + f(b)
    S1,S2 = 0,0
    for k in range(1,N):
        S1 = S1 + f(a+k*h)
    for k in range(1,N+1) : 
        S2 = S2 + f(a+(k-0.5)*h)
    S = S/6 + S1/3 + 2*S2/3
    return S*h
        
def plot_erreurs(nom_de_fichier):
    """Trace les erreurs des méthodes des rectangles, trapèzes et Simpson sur cos"""
    x = list(range(1,101))
    yRg = [abs(Rg(cos,0,0.5*pi,k)-1) for k in x]
    yRd = [abs(Rd(cos,0,0.5*pi,k)-1) for k in x]
    yT = [abs(T(cos,0,0.5*pi,k)-1) for k in x]
    yS = [abs(S(cos,0,0.5*pi,k)-1) for k in x]
    plt.clf()
    plt.plot(x,yRg,'xr',label="$|R_k-1|$")
    plt.plot(x,yRd,'+b',label="$|R'_k-1|$")
    plt.plot(x,yT,'*g',label="$|T_k-1|$")
    plt.plot(x,yS,'pm',label="$|S_k-1|$")
    plt.legend(loc=0)
    plt.xlabel("$k$")
    plt.ylabel("Erreurs d'approximations")
    plt.title("Erreurs d'approximations de $\\int_{0}^{\\pi/2} \\cos$ par différentes méthodes")
    plt.savefig(nom_de_fichier)
    return None

def plot_erreurs_semilog(nom_de_fichier):
    """Trace les erreurs des méthodes des rectangles, trapèzes et Simpson sur f
       Échelle semi-logarithmique"""
    x = list(range(1,101))
    yRg = [abs(Rg(cos,0,0.5*pi,k)-1) for k in x]
    yRd = [abs(Rd(cos,0,0.5*pi,k)-1) for k in x]
    yT = [abs(T(cos,0,0.5*pi,k)-1) for k in x]
    yS = [abs(S(cos,0,0.5*pi,k)-1) for k in x]
    plt.clf()
    plt.plot(x,yRg,'xr',label="$|R_{k}-1|$")
    plt.plot(x,yRd,'+b',label="$|R'_{k}-1|$")
    plt.plot(x,yT,'*g',label="$|T_{k}-1|$")
    plt.plot(x,yS,'pm',label="$|S_{k}-1|$")
    plt.legend(loc=0)
    plt.xlabel("$k$")
    plt.ylabel("Erreurs d'approximations (échelle logarithmique)")
    plt.yscale('log')
    plt.title("Erreurs d'approximations de $\\int_{0}^{\\pi/2} \\cos$ par différentes méthodes")
    plt.savefig(nom_de_fichier)
    return None

def plot_erreurs_log(nom_de_fichier):
    """Trace les erreurs des méthodes des rectangles, trapèzes et Simpson sur f
       Échelle logarithmique"""
    x = [int(10**k) for k in linspace(0,7)]
    yRg = [abs(Rg(cos,0,0.5*pi,k)-1) for k in x]
    yRd = [abs(Rd(cos,0,0.5*pi,k)-1) for k in x]
    yT = [abs(T(cos,0,0.5*pi,k)-1) for k in x]
    yS = [abs(S(cos,0,0.5*pi,k)-1) for k in x]
    plt.clf()
    plt.plot(x,yRg,'xr',label="$|R_{k}-1|$")
    plt.plot(x,yRd,'+b',label="$|R'_{k}-1|$")
    plt.plot(x,yT,'*g',label="$|T_{k}-1|$")
    plt.plot(x,yS,'pm',label="$|S_{k}-1|$")
    plt.legend(loc=0)
    plt.xlabel("$k$")
    plt.ylabel("Erreurs d'approximations (échelle logarithmique)")
    plt.xscale('log')
    plt.yscale('log')
    plt.title("Erreurs d'approximations de $\\int_{0}^{\\pi/2} \\cos$ par différentes méthodes")
    plt.savefig(nom_de_fichier)
    return None

if __name__ == '__main__':
    plot_erreurs('plot_erreurs.png')
    plot_erreurs_semilog('plot_erreurs_semilog.png')
    plot_erreurs_log('plot_erreurs_log.png')
    
