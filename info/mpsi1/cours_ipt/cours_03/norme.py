from math import sqrt

def norme1(x,y):
    """Norme du vecteur (x,y)
    Précondition : x,y réels"""
    return (x**2+y**2)**.5

def norme2(v):
    """Norme du vecteur v
    Précondition : v couple de nombres"""
    x,y = v
    return sqrt(x**2+y**2)
