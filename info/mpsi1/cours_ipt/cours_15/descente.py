from remontee import *

def cherche_pivot(A, j):
    """Cherche et renvoie un i tel que abs(A[i][j]) est maximal, avec i>=j"""
    n = len(A)
    best = j
    for i in range(j+1, n):
        # Inv : pour tout k <= j, abs(A[best][i]) >= abs(A[k][i])
        if abs(A[i,j]) > abs(A[best,j]):
            best = i
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

# A = np.array([[8., 5., 8.],
#          [4., 5., 2.],
#          [4., 3., 2.]])
# Ac = np.array([[8., 5., 8.],
#          [4., 5., 2.],
#          [4., 3., 2.]])
# b = np.array([[1.],[2.],[3.]])
# bc = np.array([[1.],[2.],[3.]])

#descente(Ac,bc)
#X = remontee(Ac,bc)
#A.dot(X)

C = np.array([[1.,-1.],[2.,5.],[3.,42.]])
Cc = np.array([[1.,-1.],[2.,5.],[3.,42.]])
A = np.array([[8., 5., 8.],
         [4., 5., 2.],
         [4., 3., 2.]])
Ac = np.array([[8., 5., 8.],
         [4., 5., 2.],
         [4., 3., 2.]])
# descente(Ac,Cc)
# Y = remontee(Ac,Cc)
# A.dot(Y)
