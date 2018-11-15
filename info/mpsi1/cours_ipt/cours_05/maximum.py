def maxi(t):
    """Maximum du tableau t
       Précondition : t tableau de nombres non vide"""
    m = t[0] # Maximum de la tranche déjà inspectée
    for x in t:
        if x > m:
            m = x
    return m

def maxi_invariant(t):
    """Maximum du tableau t
       Précondition : t tableau de nombres non vide"""
    m = t[0] # Maximum de la tranche déjà inspectée
    for i in range(1,len(t)):
        # m = max(t[:i])
        if t[i] > m:
            m = t[i]
    return m
