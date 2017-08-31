def liste_imax(t):
    """Liste des indices où max(t) est atteint"""
    L = [0]
    for k in range(1,len(t)):
        if t[k]>t[L[0]]:
            L = [k]
        elif t[k] == t[L[0]]:
            L.append(k)
    return L

# À vous d'écrire un invariant. 

t = [15,0,5,-7,8,15,16,17,18,1,18]

