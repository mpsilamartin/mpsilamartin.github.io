def liste_imax(t):
    """Renvoie la liste des indices du max de t"""
    L = []
    m = t[0]
    for i in range(len(t)):
        # Inv : m = max(t[:i])
        # Inv : L est la liste des 0<=j<i tq t[j]=m
        if t[i]>m:
            m = t[i]
            L = [i]
        elif t[i] == m:
            L.append(i)
    return L

t = [0,4,2,5,3,5,-1,5]

# ou bien

def liste_imax2(t):
    maxi = max(t) # A écrire
    L = []
    for i in range(len(t)):
        if t[i] == maxi:
            L.append(i)
    return L



        
