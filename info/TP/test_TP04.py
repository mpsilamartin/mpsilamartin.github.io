# -*- coding: utf-8 -*-
### TPn°04, correction

from prog import *

# Q39

from math import floor, sqrt

def cor_racine(x):
    """Racine carrée de x, de type int ou float"""
    s = sqrt(x)
    if s  == floor(s):
        s = int(s)
    return s

def test_01_racine() :
    c1 = cor_racine(0)
    c2 = racine(0)
    assert c1 == c2
    
def test_02_racine() :
    c1 = cor_racine(16**2)
    c2 = racine(16**2)
    assert c1 == c2
    
def test_03_racine() :
    c1 = cor_racine(16**2+1)
    c2 = racine(16**2+1)
    assert c1 == c2

# Q40

def cor_touche(a,b,x):
    """Le navire se trouve entre les cases a et b, indique si le tir
    en x touche de navire"""
    xa,ya=a
    xb,yb=b
    xx,yx=x
    return ((xa==xb==xx) and  (ya-yx)*(yb-yx) <= 0) or ((yb==ya==yx)\
            and  (xa-xx)*(xb-xx) <= 0 )


def test_04_touche() :
    """Alignés verticalement, touche pas"""
    a,b,x = (3,2),(6,2),(0,2)
    c1 = cor_touche(a,b,x)
    c2 = touche(a,b,x)
    assert c1 == c2
    
def test_05_touche() :
    """Alignés verticalement, touche"""
    a,b,x = (2,0),(2,3),(2,1)
    c1 = cor_touche(a,b,x)
    c2 = touche(a,b,x)
    assert c1 == c2
    
def test_06_touche() :
    """Idem que 05 mais renversés"""
    a,b,x = (2,3),(2,0),(2,1)
    c1 = cor_touche(a,b,x)
    c2 = touche(a,b,x)
    assert c1 == c2
    
def test_07_touche() :
    """Alignés horizontalement, touche pas"""
    a,b,x = (3,5),(3,2),(3,8)
    c1 = cor_touche(a,b,x)
    c2 = touche(a,b,x)
    assert c1 == c2
    
def test_08_touche() :
    """Alignés horizontalement, touche"""
    a,b,x = (7,2),(7,8),(7,4)
    c1 = cor_touche(a,b,x)
    c2 = touche(a,b,x)
    assert c1 == c2

def test_10_touche() :
    """Pas alignés verticalement"""
    a,b,x = (5,1),(3,1),(4,0)
    c1 = cor_touche(a,b,x)
    c2 = touche(a,b,x)
    assert c1 == c2

def test_11_touche() :
    """Pas alignés horizontalement"""
    a,b,x = (7,2),(7,8),(8,4)
    c1 = cor_touche(a,b,x)
    c2 = touche(a,b,x)
    assert c1 == c2

    
# Q41

#a
def cor_reste_a_payer(p,t,m,d):
    """p = montant du pret en euros
       t = taux mensuel
       m = mensualites
       d = duree en annees
       Calcule le montant restant a payer a l'echeance   du pret"""
    montant = p
    for mois in range(d*12):
        montant = montant*(1+t)-m
    return montant


    
def test_01_reste_a_payer() :
    pret = 400000
    taux = 0.0025
    mensualite = 1431.93
    duree = 40
    c1 = cor_reste_a_payer(pret,taux,mensualite,duree)
    c2 = reste_a_payer(pret,taux,mensualite,duree)
    assert abs(c1 - c2) < 10**-5
    
def test_02_reste_a_payer() :
    pret = 200000
    taux = 0.0015
    mensualite = 11268.65
    duree = 15 
    c1 = cor_reste_a_payer(pret,taux,mensualite,duree)
    c2 = reste_a_payer(pret,taux,mensualite,duree)
    assert abs(c1 - c2) < 10**-5

#b
def cor_somme_totale_payee(p,t,m,d):
    """p = montant du pret
       t = taux
       m = mensualites
       d = duree en annees
       Calcule le montant total paye"""
    total = cor_reste_a_payer(p,t,m,d) + 12*d*m
    return total

    
def test_01_somme_totale_payee() :
    pret = 400000
    taux = 0.0025
    mensualite = 1431.93
    duree = 40
    c1 = cor_somme_totale_payee(pret,taux,mensualite,duree)
    c2 = somme_totale_payee(pret,taux,mensualite,duree)
    assert abs(c1 - c2) < 10**-5

def test_02_somme_totale_payee() :
    pret = 200000
    taux = 0.0015
    mensualite = 11268.65
    duree = 15 
    c1 = cor_somme_totale_payee(pret,taux,mensualite,duree)
    c2 = somme_totale_payee(pret,taux,mensualite,duree)
    assert abs(c1 - c2) < 10**-5

# c 
def cor_cout_total(p,t,m,d):
    """p = montant du pret
       t = taux
       m = mensualites
       d = duree en annees
       Calcule le cout total du credit"""
    cout = cor_somme_totale_payee(p,t,m,d) - p
    return cout

def test_01_cout_total() :
    pret = 400000
    taux = 0.0025
    mensualite = 1431.93
    duree = 40
    c1 = cor_cout_total(pret,taux,mensualite,duree)
    c2 = cout_total(pret,taux,mensualite,duree)
    assert abs(c1 - c2) < 10**-5

def test_02_cout_total() :
    pret = 200000
    taux = 0.0015
    mensualite = 11268.65
    duree = 15 
    c1 = cor_cout_total(pret,taux,mensualite,duree)
    c2 = cout_total(pret,taux,mensualite,duree)
    assert abs(c1 - c2) < 10**-5

# Q42

def cor_duree_mensualite(p,t,m):
    assert m > t*p, "mensualite insuffisante"
    emprunt = p
    d = 0
    while emprunt >= m:
        d = d+1
        emprunt = (1+t)*emprunt-m
    return d

def test_01_duree_mensualite() :
    pret = 400000
    taux = 0.0025
    mensualite = 1431.93
    c1 = cor_duree_mensualite(pret,taux,mensualite)
    c2 = duree_mensualite(pret,taux,mensualite)
    assert c1 == c2

def test_02_duree_mensualite() :
    pret = 500000
    taux = 0.0025
    mensualite = 1250.00000001
    c1 = cor_duree_mensualite(pret,taux,mensualite)
    c2 = duree_mensualite(pret,taux,mensualite)
    assert c1 == c2
    

# Q43


def cor_comb(p,n):
    """p = entier 
       n = entier naturel
       Calcule p parmi n en utilisant la formule de recurrence
       C(n,p) = C(n-1,p-1)*n/p"""
    assert n >= 0, 'Argument incompatible : n<0'
    if (p<0) or (p>n):
        combinaison = 0
    else:
        combinaison = 1
        for k in range(p):
            combinaison = combinaison*(n-p+k+1)//(k+1)
    return combinaison

def test_01_comb() :
    c1 = cor_comb(15,32)
    c2 = comb(15,32)
    assert c1 == c2 and type(c1) == type(c2)
    
def test_02_comb() :
    c1 = cor_comb(0,32)
    c2 = comb(0,32)
    assert c1 == c2 and type(c1) == type(c2)

def test_03_comb() :
    c1 = cor_comb(-5,32)
    c2 = comb(-5,32)
    assert c1 == c2 and type(c1) == type(c2)

# Q44

def cor_fib(n):
    """n = entier naturel 
       Calcule le n-eme terme de la suite de Fibonnaci"""
    assert n >=0, 'Argument incompatible : n<0'   
    F = [1, 0]
    for k in range(n):
        F[0],F[1] = F[0]+F[1],F[0]
    return F[1]


def test_01_fib() :
    c1 = cor_fib(0)
    c2 = fib(0)
    assert c1 == c2
    
def test_02_fib() :
    c1 = cor_fib(1)
    c2 = fib(1)
    assert c1 == c2

def test_03_fib() :
    c1 = cor_fib(10)
    c2 = fib(10)
    assert c1 == c2

def test_04_fib() :
    c1 = cor_fib(450)
    c2 = fib(450)
    assert c1 == c2

# Q45

def cor_f(n):
    """n = entier naturel
       Calcule le n-eme terme de la suite u (TP04, exo 44)"""
    assert n >=0, 'Argument incompatible : n<0'
    u = 1
    v = 1
    for k in range(n):
	# Invariants : u = u_k et v = v_k
        u = (u+(k+1)/u)/2
        v = v + (1/u**5)
        # u = u_(k+1) et v = v_(k+1)
    # v = v_(n-1+1)
    return v

def test_01_f() :
    c1 = cor_f(0)
    c2 = f(0)
    assert abs(c1 - c2) < 10**-5

def test_02_f() :
    c1 = cor_f(1)
    c2 = f(1)
    assert abs(c1 - c2) < 10**-5

def test_03_f() :
    c1 = cor_f(2)
    c2 = f(2)
    assert abs(c1 - c2) < 10**-5

def test_04_f() :
    c1 = cor_f(10)
    c2 = f(10)
    assert abs(c1 - c2) < 10**-5
    
def test_05_f() :
    c1 = cor_f(10**6)
    c2 = f(10**6)
    assert abs(c1 - c2) < 10**-5

# Q46

def cor_somme1(n):
    """n = entier naturel non nul
       Calcule la somme des 1/(i+j**2), pour 1<=i,j<=n"""
    assert n>0, 'Argument incompatible : n<1'
    s = 0
    for i in range(n):
        for j in range(n):
            s = s + 1/(i+1+(j+1)**2)
    return s


def test_01_somme1() :
    c1 = cor_somme1(1)
    c2 = somme1(1)
    assert abs(c1-c2) < 10**(-5)
    
def test_02_somme1() :
    c1 = cor_somme1(100)
    c2 = somme1(100)
    assert abs(c1-c2) < 10**(-5)


def cor_somme2(n):
    """n = entier naturel superieur ou egal a 2.
       Calcule la somme des 1/(i+j**2), pour 1<=i<j<=n"""
    assert n>1, 'Argument incompatible : n<2'
    s = 0
    for k in range(n-1):
        ## Moralement : k+1 = j-1 -> j varie de 2 a n
        for i in range(k+1):
            s = s + 1/(i+1+(k+2)**2)
    return s


def test_01_somme2() :
    c1 = cor_somme2(2)
    c2 = somme2(2)
    assert abs(c1-c2) < 10**(-5)
    
def test_02_somme2() :
    c1 = cor_somme2(100)
    c2 = somme2(100)
    assert abs(c1-c2) < 10**(-5)
