from numpy import array,zeros,transpose

def cherche_pivot(A, j):
    """Cherche et renvoie un i tel que abs(A[i,j]) est maximal, avec i<=j"""
    n = len(A)
    best = j
    for i in range(j+1, n):
        # Inv : pour tout k <= i, abs(A[best,j]) >= abs(A[k,j])
        if abs(A[i,j]) > abs(A[best,j]):
            best = i
            print(best,abs(A[i,j]))
    return best

def echange_lignes(A, i, j):
    """Échange les lignes i et j de la matrice A"""
    A[i,:],A[j,:] = A[j,:].copy(), A[i,:].copy()
    return None

def descente(A,b):
    """Phase de descente de la méthode du pivot pour résoudre Ax = b.
    Préconditions : A et b sont de type array,
    A est inversible,
    b a même nombre de lignes que A.
    Attention: cette fonction modifie A et b."""
    n = len(A)
    for j in range(n-1):
        ip = cherche_pivot(A, j)
        # on met en place la ligne du pivot :
        echange_lignes(A, j, ip)
        echange_lignes(b, j, ip)
        p = A[j, j] # le pivot
        for i in range(j+1, n):
            alpha = - A[i,j] / p # Coefficient multiplicateur
            b[i,:] = b[i,:] + alpha * b[j,:]
            A[i,:] = A[i,:] + alpha * A[j,:]
    return None

def remontee(U,B):
    """Résout le système UX = b.
    Préconditions: U triangulaire supérieure
    b a autant de lignes que U."""
    n, m = B.shape
    X = zeros((n, m))
    for k in range(n):
        i = n-1-k
        # Invariant X[i+1:] est correct
        s = U[i, i+1:].dot(X[i+1:])
        X[i] = (B[i] - s) / U[i, i]
    return X

def resout(A,b):
    """Applique la méthode du pivot pour résoudre Ax = b.
    Renvoie la solution x trouvée.
    Préconditions : A et b sont de type array,
    A est inversible,
    b a même nombre de lignes que A."""
    n = len(A)
    # On copie A et b
    A_, b_ = A.copy(), b.copy()
    descente(A_,b_)
    return remontee(A_,b_)




























# n = 5
# M = array([[ 1/(i+j+1.) for j in range(n)] for i in range(n)])