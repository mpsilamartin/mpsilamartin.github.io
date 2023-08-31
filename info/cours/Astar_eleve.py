''' 11 - Bases des graphes'''
from Affichage import *
import pdb
import os
## 11-3 - A star

## Création de l'image

# Initialisation

Nl,Nc = 5,9
Image = 255*np.ones((Nl,Nc,3),dtype='uint8')

# Obstacles

Noir = [0,0,0]

for l in range(1,4):
    Image[l,4] = Noir

for c in range(4,6):
    Image[1,c] = Noir

# Depart - Arrivee

'''ATTENTION: partir d'un point blanc'''
lDep,cDep = 3,7
lA,cA = 0,1
Rouge = [255,0,0]
Image[lDep,cDep] = Rouge
Bleu = [0,0,255]
Vert = [0,180,0]
Image[lA,cA] = Bleu

Depart = (lDep,cDep)
Arrivee = (lA,cA)

# Affichage

Affiche(1,Image,True)




###Heuristique


from math import sqrt



def distance_man(l,c,la,ca):
    return None



def f_heuristique(l,c,la,ca):
    return 10



Affiche_distance(1,Image,True,f_heuristique,Arrivee)


# Fonction de comparaison de pixels

def Test_Pix(P1,P2):
    Res = True
    for i in range(3):
        Test = P1[i]==P2[i]
        Res = Res & Test
    return Res

# Initialisation de Dico_Voisins

Noir = [0,0,0]
Dico_Voisins = {}
for l in range(Nl):
    for c in range(Nc):
        Pix = Image[l,c]
        Case = (l,c)
        if Test_Pix(Pix,Noir)==False:
            Dico_Voisins[Case] = []


# Fonction de traitement des voisins d'une case

from math import sqrt

def Couples_Voisins(l,c):
    Case = (l,c)
    for li in range(l-1,l+2):
        for ci in range(c-1,c+2):
            Case_i = (li,ci)
            # Ne pas traiter la case actuelle
            test_case = (Case_i != Case)
            # Etre dans l'image
            test_image = (0 <= li < Nl and 0 <= ci < Nc)
            if test_case and test_image:
                Pixi = Image[li,ci]
                if Test_Pix(Pixi,Noir)==False:
                    Di = int(sqrt((li-l)**2+(ci-c)**2)*10)
                    Couple = [Case_i,Di]
                    Dico_Voisins[Case].append(Couple)

# Remplissage de Dico_Voisins

for Case in Dico_Voisins.keys():
    l,c = Case
    Pix = Image[l,c]
    Couples_Voisins(l,c)





#Initialisation ds distances

Distances = np.inf*np.ones([Nl,Nc])
Distances[lDep,cDep] = 0
# Provenances = {}
Reste = Dico_Voisins.copy()
S = (lDep,cDep)
del Reste[S]
Image_Anim=Image.copy()






