from tri import *
import time as t
import matplotlib.pyplot as plt



####Comparaison des temps de calcul
def comparer_tri(LGN,nom_de_fichier):
    temps_insertion=[]
    temps_rapide=[]
    temps_fusion=[]
    temps_sorted=[]
    liste_k=[]
    for k in range(2,len(LGN),100):
        liste_k.append(k)
        LGT1=LGN[:k+1]
        LGT2=LGN[:k+1]
        LGT3=LGN[:k+1]
        LGT4=LGN[:k+1]
        tic=t.time()
        tri_fusion(LGT1,0,len(LGT1))
        toc=t.time()
        temps_fusion.append(toc-tic)
        tic=t.time()
        tri_insertion(LGT2)
        toc=t.time()
        temps_insertion.append(toc-tic)
        tic=t.time()
        tri_rapide(LGT3,0,len(LGT3))
        toc=t.time()
        temps_rapide.append(toc-tic)
        tic=t.time()
        sorted(LGT4)
        toc=t.time()
        temps_sorted.append(toc-tic)

    plt.clf()
    #pdb.set_trace()
    plt.plot(liste_k,temps_fusion,'g-',label='fusion')
    plt.plot(liste_k,temps_rapide,'b*-',label='rapide')
    plt.plot(liste_k,temps_insertion,'r--',label='insertion')
    plt.plot(liste_k,temps_sorted,'k.-',label='sorted')
    plt.legend()
    plt.savefig(nom_de_fichier)


import random
def generer_liste(n,N):
    x = [random.randint(0, n) for p in range(0, N)]
    return(x)

N=int(1e3)
# for k in range(1,N,100):
#     L=generer_liste(N,N)

L=generer_liste(N,N)
comparer_tri(L,'complexite.png')


