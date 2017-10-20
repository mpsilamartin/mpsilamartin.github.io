def factorielle(n):
    """n!
    Précondition : n entier naturel"""
    k=1
    f=1
    while k <= n :
        f = f*k
        k = k+1
    return f

# Correct, mais on préfère un for

def factoriellebis(n):
    """n!
    Précondition : n entier naturel"""
    f=1
    for k in range(2,n+1) :
        f = f*k
    return f
