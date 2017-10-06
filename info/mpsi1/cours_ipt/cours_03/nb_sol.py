def nb_sol(a,b,c):
    """Nb de solutions réelles de a * x**2 + b * x + c == 0
    Précondition : a,b,c flottants et a != 0"""
    D = b**2 - 4*a*c
    if D > 0:
        return 2
    elif D == 0 :
        return 1
    else :
        return 0
