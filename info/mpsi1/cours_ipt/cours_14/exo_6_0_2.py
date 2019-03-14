from math import sqrt
phi = (1+sqrt(5)) / 2

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
    
def f(x):
    """16*x**4-20*x**2+5"""
    return x**2-x-1
    
def fp(x):
    """f'(x)"""
    return 2*x-1
    

    
