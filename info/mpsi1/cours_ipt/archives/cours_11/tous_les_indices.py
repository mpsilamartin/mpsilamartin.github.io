def tous_les_indices(e,t):
    """Liste des occurences de e dans t"""
    S = []
    # S contient toutes les occurences de e dans t[:0] = []
    for k in range(len(t)):
        # Inv : S contient toutes les occurences de e dans t[:k]
        if t[k] == e:
            S.append(k)
        # On a rajouté k ssi t[k] est une occurence de e.
        # Inv : S contient toutes les occurences de e dans t[:k+1]
    # Au dernier tour, k = len(t) - 1
    # Inv : S contient toutes les occurences de e dans t[:len(t)]=t
    return S

t = [0,1,4,0,1,5,4,8,0,0,1]
