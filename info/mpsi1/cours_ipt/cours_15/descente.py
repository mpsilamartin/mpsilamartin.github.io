from remontee import *

def cherche_pivot(A, i):
    """Cherche et renvoie un j tel que abs(A[j][i]) est maximal, avec j>=i"""
    n = len(A)
    best = i
    for j in range(i+1, n):
        # Inv : pour tout k <= j, abs(A[best][i]) >= abs(A[k][i])
        if abs(A[j,i]) > abs(A[best,i]):
            best = j
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
    for i in range(n-1):
        ip = cherche_pivot(A, i)
        # on met en place la ligne du pivot :
        echange_lignes(A, i, ip)
        echange_lignes(b, i, ip)
        p = A[i, i] # le pivot
        for j in range(i+1, n):
            alpha = - A[j,i] / p # Coefficient multiplicateur
            b[j,:] = b[j,:] + alpha * b[i,:]
            A[j,:] = A[j,:] + alpha * A[i,:]
    return None

def resout(A,b):
    """Applique la méthode du pivot pour résoudre Ax = b.
    Renvoie la solution x trouvée.
    Préconditions : A et b sont de type array,
                    A est inversible,
                    b a même nombre de lignes que A."""
    # On copie A et b
    A_, b_ = A.copy(), b.copy()
    descente(A_,b_)
    return remontee(A_,b_)

A = np.array([[8., 5., 8.],
         [4., 5., 2.],
         [4., 3., 2.]])
Ac = A.copy()
b = np.array([[1.],[2.],[3.]])
bc = b.copy()

descente(Ac,bc)
X = remontee(Ac,bc)
A.dot(X)

C = np.array([[1.,-1.],[2.,5.],[3.,42.]])
Cc = C.copy()
Ac = A.copy()
descente(Ac,Cc)
Y = remontee(Ac,Cc)
A.dot(Y)
