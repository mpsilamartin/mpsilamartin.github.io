def ind_appartient_dicho(e,t):
    """ """
    g,d = 0, (len(t) -1)
    while g <= d:
        # Variant : d-g
        # Inv : si e est dans t, t[g] <= e <= t[d]
        m = (g+d) // 2
        pivot = t[m]
        if pivot == e:
            return m
        elif pivot < e:
            g = m+1
        else :
            d = m-1
    # g > d
    # Si e est dans t, au tour précédent, t[g] <= e <= t[d]
    # On montre qu'au tour précédent g == d
    # -> absurde
    return None

t = list(range(42,1515))
