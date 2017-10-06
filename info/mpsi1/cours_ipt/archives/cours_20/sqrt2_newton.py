f = lambda x : x**2-2
fp = lambda x : 2*x

def newton(f, fp, x0, eps):
    """Zéro de f par la méthode de Newton
       départ : x0, f' = fp, critère d'arrêt epsilon"""
    u = x0
    v = u - f(u)/fp(u)
    while abs(v-u) > eps:
        u, v = v, v - f(v)/fp(v)
    return v
