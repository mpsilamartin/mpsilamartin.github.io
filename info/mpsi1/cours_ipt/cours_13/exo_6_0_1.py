from math import cos, pi

def f(x):
    return 16*x**4-20*x**2+5

def fp(x):
    return 64*x**3-40*x

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

def newton(f, fp, x0, eps):
    """Zéro de f par la méthode de Newton
       départ : x0, f' = fp, critère d'arrêt epsilon"""
    u = x0
    v = u - f(u)/fp(u)
    while abs(v-u) > eps:
        u, v = v, v - f(v)/fp(v)
    return v
