from math import sqrt

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
    
def newton(f, fp, x0, epsilon):
    """Zéro de f par la méthode de Newton
       départ : x0, f' = fp, critère d'arrêt epsilon"""
    u = x0
    v = u - f(u)/fp(u)
    while abs(v-u) > epsilon:
        u, v = v, v - f(v)/fp(v)
    return u

def secante(f,u0,u1,eps):
    """Zéro de f par la méthode de la sécante
    u0,u1 : deux premiers points
    eps : critère d'arrêt"""
    u,v = u0,u1
    while abs(u-v) > eps : 
        p = (f(u)-f(v)) / (u-v)
        u,v = v,u - f(u)/p
    return u
    
def f(p,x):
    """x+...+x^p-1"""
    S = 0
    px = x
    for i in range(p):
        # Inv : S = x+x^2+...+x^{i}
        # Inv : px = x^{i+1}
        S = S + px
        px = x*px
    return S-1
    
def fp(p,x):
    """1+2x+3x^2+...+px^p-1"""
    S = 0
    px = 1
    for i in range(p):
        # Inv : S = 1+2x+...+ix^i-1
        # Inv : px = x^{i}
        S = S + (i+1)*px
        px = x*px
    return S

def rep_dicho(p,eps):
    """v.a. de 1=x+x^2+...+x^p à eps près, méthode de la dichotomie"""
    def g(x) : return f(p,x)
    # On préfèrerait utiliser lambda...
    # g = lambda x : f(p,x)
    return dichotomie(g,0,1,eps)
    

def rep_newton(p,eps):
    """v.a. de 1=x+x^2+...+x^p, méthode de Newton, critère d'arrêt eps"""
    def g(x) : return f(p,x)
    def gp(x) : return fp(p,x)
    # On préfèrerait utiliser lambda...
    return newton(g,gp,1,eps)


def rep_secante(p,eps):
    """v.a. de 1=x+x^2+...+x^p, méthode de la sécante, critère d'arrêt eps"""
    def g(x) : return f(p,x)
    # On préfèrerait utiliser lambda...
    return secante(g,0,1,eps)
    
