#1

def test(L):
    bool=True
    i=0
    while i<=len(L)-2 and L[i]<=L[i+1]:
        i+=1
    return i==len(L)-1

# 2

def tri_insertion(L):
    n=len(L)
    for i in range(1,n):
        j=i
        while j>=1 and (L[j]<L[j-1]):
            L[j],L[j-1]=L[j-1],L[j]
            j=j-1

# Cout de l'algorithme: dans le pire des cas, pour chaque i, il y a i échanges. D'où une complexité de (n(n+1))/2 soit quadratique.

def insertion_triee_rec(L, i):
    x = L[i]
    if i >= 1 and L[i-1] > x:
        L[i],L[i-1] = L[i-1],L[i]
        insertion_triee_rec(L, i-1)

def tri_insertion_rec(L):
    n = len(L)
    if n >= 1:
        x = L.pop()
        tri_insertion_rec(L)
        L.append(x)
        # les éléments d'indices 0 à n-2 sont triés
        insertion_triee_rec(L, n-1)

from random import randint

L = [randint(0, 99) for k in range(10)]
#print(L)
tri_insertion(L)
#print(L)

#3

def minimum_liste(L:list):
    m=L[0]
    indice = 0
    for i in range(1,len(L)):
        if L[i]<m:
            m=L[i]
            indice = i
    return indice


def tri_selection(L):
    n=len(L)
    for i in range(len(L)):
        indice=minimum_liste(L[i:])   # Attention indice est relatif a la liste L[i:] et non L
        L[indice+i],L[i]=L[i],L[indice+i]
    return None

L = [randint(0, 99) for k in range(10)]
print(L)
tri_selection(L)
print(L)

## 4  Tri par comptage


def tri_comptage(L,k):  ## avec effet de bord
    n=len(L)
    C=[0]*k
    M=[]
    for i in range(n):
        C[L[i]]+=1
    cpt=0
    for i in range(k):
        for j in range(C[i]):
            compteur()
            L[cpt]=i
            cpt+=1
    return(None)

def tri_comptage_02(L,k):   ## Sans effet de bord
    n=len(L)
    C=[0]*k
    M=[]
    for i in range(n):
        C[L[i]]+=1
    for i in range(k):
        for j in range(C[i]):
            M.append(i)
    return(M)



Liste=[6,5,3,4,4,2,4,6,8,5]

#Un tri stable respecte l'ordre. Si i<j et ti<=tj, alors ti restera avant tj. Un tri par comptage l'est.
# Le tri en place agit sur place. Il faut un effet de bord, c'est la deuxième fonction.

## Tri fusion

def separe(L):
    p=len(L)//2
    return(L[:p],L[p:])


def fusion(L1,L2):
    compteur()
    if L1==[]:
        return L2
    elif L2==[]:
        return L1
    else:
        if L1[0]<L2[0]:
            return [L1[0]]+fusion(L1[1:],L2)
        else:
            return [L2[0]]+fusion(L1,L2[1:])

def tri_fusion(L):
    if len(L)<=1:
        return L
    else:
        L1,L2=separe(L)
        return fusion(tri_fusion(L1),tri_fusion(L2))

def compteur():
    global C
    C = C+1

import matplotlib.pyplot as plt
import random as rd
les_i = []
les_selection,les_comptage, les_fusion = [],[],[]
for i in range(1,200,10):
    les_i.append(i)
    L = [rd.randrange(0,i) for x in range(i)]

    C = 0
    tri_comptage(L.copy(),max(L)+1)
    les_comptage.append(C)

    C = 0
    tri_selection(L.copy())
    les_selection.append(C)

    C = 0
    tri_fusion(L.copy())
    les_fusion.append(C)

plt.plot(les_i,les_comptage,label='Comptage')
plt.plot(les_i,les_selection,label='Sélection')
plt.plot(les_i,les_fusion,label='Fusion')
plt.grid()
plt.legend()
plt.show()








