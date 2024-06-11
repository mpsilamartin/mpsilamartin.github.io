# -*- coding: utf-8 -*-

## importation des modules
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
from heapdict import heapdict

## déclaration des fonctions
def Aetoile(G, depart, arrivee, heuristique):
    fileP = heapdict()
    distance = {}
    predecesseur = {}
    for sommet in G:
        distance[sommet] = float("inf")
        fileP[sommet] = float("inf")
    distance[depart] = 0
    fileP[depart] = 0 + heuristique(depart, arrivee)
    predecesseur[depart] = None
    SommetsVisites = []
    while fileP:
        sommet, priorite = fileP.popitem()
        SommetsVisites.append( (sommet, priorite) )
        if sommet == arrivee:
            chemin = deque()
            sommet = arrivee
            while sommet != None:
                chemin.appendleft(sommet)
                sommet = predecesseur[sommet]
            return list(chemin), SommetsVisites, priorite
        for sommetAdj, poids in G[sommet]:
            if sommetAdj in fileP:
                d_alt = distance[sommet] + poids
                if d_alt < distance[sommetAdj]:
                    distance[sommetAdj] = d_alt
                    fileP[sommetAdj] = d_alt + heuristique(sommetAdj, arrivee)
                    predecesseur[sommetAdj] = sommet

def distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

## programme principal

# Début question 2
# obstacle = {"x":[], "y":[]}
# terrain = {"x":[], "y":[]}
#
# for i in range(100):
#     for j in range(100):
#         if estDansDisque( (i,j), (50, 70), 20):
#             obstacle["x"].append(i)
#             obstacle["y"].append(j)
#         else:
#             terrain["x"].append(i)
#             terrain["y"].append(j)
# plt.plot(obstacle["x"], obstacle["y"], 'k.', ms=1)
# plt.plot(terrain["x"], terrain["y"], 'b.', ms=1)
# plt.axis("equal")
# plt.show()

# Début question 6
# chemin, visite, dureeParcours = Aetoile(G,
#     (15, 20), (80, 90),
#     lambda s1, s2: 1*distance(s1, s2)) # heuristique
# print(dureeParcours, len(visite))
