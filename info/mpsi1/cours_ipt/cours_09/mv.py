def moy(t):
    """Moyenne du tableau t"""
    s = 0 # s == sum([])
    n = len(t) # Longueur de t
    for k in range(n):
        # s == sum(t[:k])
        s = s + t[k]
        # s == sum(t[:k+1])
    # Au dernier tour de boucle, k == n-1
    # Donc s == sum(t[:n+1]) == sum(t)
    return s / n

def moy2(t):
    """Moyenne du tableau t"""
    s = 0 # s == sum([])
    for x in t:
        # s : somme des éléments de t avant x
        s = s + x
        # s : somme des élts de t jusqu'à x
    return s / len(t)

def moy3(t):
    """Moyenne du tableau t"""
    return sum(t) / len(t)

def var(t):
    """Variance de t"""
    v = 0 # v = sum([])
    n = len(t)
    m = moy(t)
    for k in range(n):
        # v == sum([(t[i]-m)**2 for i in range(k)])
        v = v + (t[k]-m)**2
        # v == sum([(t[i]-m)**2 for i in range(k+1)])
    # Au dernier tout, k = n-1, donc
    # v = sum([(t[i]-m)**2] for i in range(n)])
    return v / n

def var2(t):
    """Variance de t"""
    v = 0
    m = moy2(t)
    for x in t:
        v = v + (x-m)**2
    return v / len(t)

def var3(t):
    """Variance de t"""
    m = sum(t)/len(t)
    v = sum([(x-m)**2 for x in t])
    return v / len(t)

def mv(t):
    """(moyenne,variance) de t"""
    s,sc = 0,0
    for x in t :
        #
        s = s + x
        sc = sc + x**2
        #
    m = s / len(t)
    v = sc/len(t) - m**2
    return m,v

t = [i for i in range(1,101)]
