from math import sqrt

def trinome(a,b,c):
    """Racines de aX**2+bX+c"""
    D = b**2-4*a*c
    if D == 0:
        x0 = -b/(2*a)
        return (x0,)
    elif D > 0:
        sD = sqrt(D)
        x1 = (-b+sD) / (2*a)
        x2 = (-b-sD) / (2*a)
        return (x1,x2)
    else :
        return ()

def trinome_bis(a,b,c):
    """Racines de aX**2+bX+c"""
    D = b**2-4*a*c
    if D >= 0:
        sD = sqrt(D)
        x1 = (-b+sD) / (2*a)
        x2 = (-b-sD) / (2*a)
        return (x1,x2)
    else :
        return ()
