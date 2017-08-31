def maxi(t):
    """Maximum de t"""
    m = t[0]
    for x in t:
        if x > m:
            m = x
    return m

def maxi2(t):
    """Maximum de t"""
    m = t[0] # m == max(t[:1])
    for i in range(1,len(t)):
        # m == max(t[:i])
        if t[i] > m:
            m = t[i]
        # m == max(t[:i+1])
    # Au dernier tour, i = len(t)-1,
    # donc m == max(t)
    return m

def indice_maxi(t):
    """Indice où max(t) est atteint"""
    im = 0
    for i in range(1,len(t)):
        # t[im] == max(t[:i])
        if t[i] > t[im]:
            im = i
        # t[im] == max(t[:i+1])
    # Au dernier tour, i = len(t)-1
    # Donc t[im] == max(t)
    return im

t = [-1,8,2,-4,7,-42,8,15.15,0,0,15.15,4]
