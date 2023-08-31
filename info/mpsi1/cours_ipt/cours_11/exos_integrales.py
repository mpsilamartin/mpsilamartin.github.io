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

def plot_integrales1(nom_de_fichier):
    """Exercice 1 : calcul des intégrales, rectangles, trapèzes et Simpson"""
    x = list(range(0,1001))
    yRg = [Rg(lambda t:t**p,0,1,1000) for p in x]
    yRd = [Rd(lambda t:t**p,0,1,1000) for p in x]
    yT = [T(lambda t:t**p,0,1,1000) for p in x]
    yS = [S(lambda t:t**p,0,1,1000) for p in x]
    plt.clf()
    plt.plot(x,yRg,'xr',label="$R_n$")
    plt.plot(x,yRd,'+b',label="$R'_n$")
    plt.plot(x,yT,'*g',label="$T_n$")
    plt.plot(x,yS,'pm',label="$S_n$")
    plt.legend(loc=0)
    plt.xlabel("$p$")
    plt.title("Valeur $\\int_{0}^{1} t^p \\mathrm{d}t$ par différentes méthodes, $n=1000$")
    plt.savefig(nom_de_fichier)
    return None

def plot_erreurs1(nom_de_fichier):
    """Exercice 1 : calcul des erreurs, rectangles, trapèzes et Simpson"""
    x = list(range(0,1001))
    yRg = [abs(Rg(lambda t:t**p,0,1,1000)-1/(p+1)) for p in x]
    yRd = [abs(Rd(lambda t:t**p,0,1,1000)-1/(p+1)) for p in x]
    yT = [abs(T(lambda t:t**p,0,1,1000)-1/(p+1)) for p in x]
    yS = [abs(S(lambda t:t**p,0,1,1000)-1/(p+1)) for p in x]
    plt.clf()
    plt.plot(x,yRg,'xr',label="$|R_n-1/(p+1)|$")
    plt.plot(x,yRd,'+b',label="$|R'_n-1/(p+1)|$")
    plt.plot(x,yT,'*g',label="$|T_n-1/(p+1)|$")
    plt.plot(x,yS,'pm',label="$|S_n-1/(p+1)|$")
    plt.legend(loc=0)
    plt.xlabel("$p$")
    plt.ylabel("Erreurs d'approximations")
    plt.title("Erreurs d'approximations de $\\int_{0}^{1} t^p \\mathrm{d}t$ par différentes méthodes, $n=1000$")
    plt.savefig(nom_de_fichier)
    return None

def plot_integrales2(nom_de_fichier):
    """Exercice 1 : calcul des intégrales, rectangles, trapèzes et Simpson"""
    x = list(range(1,1001))
    yRg = [Rg(lambda t:t**2,0,1,k) for k in x]
    yRd = [Rd(lambda t:t**2,0,1,k) for k in x]
    yT = [T(lambda t:t**2,0,1,k) for k in x]
    yS = [S(lambda t:t**2,0,1,k) for k in x]
    plt.clf()
    plt.plot(x,yRg,'xr',label="$R_k$")
    plt.plot(x,yRd,'+b',label="$R'_k$")
    plt.plot(x,yT,'*g',label="$T_k$")
    plt.plot(x,yS,'pm',label="$S_k$")
    plt.legend(loc=0)
    plt.xlabel("$k$")
    plt.title("Valeur $\\int_{0}^{1} t^2 \\mathrm{d}t$ par différentes méthodes")
    plt.savefig(nom_de_fichier)
    return None

def plot_erreurs2(nom_de_fichier):
    """Exercice 2 : calcul des erreurs, rectangles, trapèzes et Simpson"""
    x = list(range(1,1001))
    yRg = [abs(Rg(lambda t:t**2,0,1,k)-1/3) for k in x]
    yRd = [abs(Rd(lambda t:t**2,0,1,k)-1/3) for k in x]
    yT = [abs(T(lambda t:t**2,0,1,k)-1/3) for k in x]
    yS = [abs(S(lambda t:t**2,0,1,k)-1/3) for k in x]
    plt.clf()
    plt.plot(x,yRg,'xr',label="$|R_k-1/(p+1)|$")
    plt.plot(x,yRd,'+b',label="$|R'_k-1/(p+1)|$")
    plt.plot(x,yT,'*g',label="$|T_k-1/(p+1)|$")
    plt.plot(x,yS,'pm',label="$|S_k-1/(p+1)|$")
    plt.legend(loc=0)
    plt.xlabel("$k$")
    plt.ylabel("Erreurs d'approximations")
    plt.title("Erreurs d'approximations de $\\int_{0}^{1} t^2 \\mathrm{d}t$ par différentes méthodes")
    plt.savefig(nom_de_fichier)
    return None

def plot_erreurs2_log(nom_de_fichier):
    """Exercice 2 : calcul des erreurs, rectangles, trapèzes et Simpson"""
    x = list(range(1,1001))
    yRg = [abs(Rg(lambda t:t**2,0,1,k)-1/3) for k in x]
    yRd = [abs(Rd(lambda t:t**2,0,1,k)-1/3) for k in x]
    yT = [abs(T(lambda t:t**2,0,1,k)-1/3) for k in x]
    yS = [abs(S(lambda t:t**2,0,1,k)-1/3) for k in x]
    plt.clf()
    plt.plot(x,yRg,'xr',label="$|R_k-1/(p+1)|$")
    plt.plot(x,yRd,'+b',label="$|R'_k-1/(p+1)|$")
    plt.plot(x,yT,'*g',label="$|T_k-1/(p+1)|$")
    plt.plot(x,yS,'pm',label="$|S_k-1/(p+1)|$")
    plt.legend(loc=0)
    plt.xlabel("$k$")
    plt.ylabel("Erreurs d'approximations")
    plt.xscale('log')
    plt.yscale('log')
    plt.title("Erreurs d'approximations de $\\int_{0}^{1} t^2 \\mathrm{d}t$ par différentes méthodes")
    plt.savefig(nom_de_fichier)
    return None

if __name__ == '__main__':
    plot_integrales1('plot_integrales1.png')
    plot_erreurs1('plot_erreurs1.png')
    plot_integrales2('plot_integrales2.png')
    plot_erreurs2('plot_erreurs2.png')
    plot_erreurs2_log('plot_erreurs2_log.png')
    
