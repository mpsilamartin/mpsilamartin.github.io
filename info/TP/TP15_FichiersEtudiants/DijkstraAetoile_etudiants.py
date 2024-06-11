# -*- coding: utf-8 -*-

## importation des modules
import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter_ns
from collections import deque
from heapdict import heapdict

## lecture données depuis Gduree.csv

MLLi = np.loadtxt( "Gduree.csv",
                delimiter=',',
                skiprows=1,
                usecols=range(1, 51),
                encoding="UTF-8").tolist()

villes = np.loadtxt( "Gduree.csv",
                delimiter=',',
                skiprows=1,
                usecols=0,
                dtype='str',
                encoding="UTF-8").tolist()

G = {} # Graphe Gi[s1][i] -> (s2, w12)
for i in range(len(MLLi)):
    ville1 = villes[i]
    G[ville1] = []
    for j in range(len(MLLi)):
        ville2 = villes[j]
        if MLLi[i][j] != 0:
            G[ville1].append((ville2, MLLi[i][j]))

X, Y = np.loadtxt("coordonnes.csv",
                delimiter=',',
                skiprows=1,
                usecols=(1,2),
                encoding="UTF-8",
                unpack=True).tolist()

coordonnees = {}
for i, ville in enumerate(villes):
    coordonnees[ville] = (X[i], Y[i])

def representationVisite(SommetsVisites, echelle, typeAlgo):
    plt.figure(typeAlgo + ", depuis " + SommetsVisites[0][0])
    for ville, priorite in SommetsVisites:
        x, y = coordonnees[ville]
        plt.plot(x, y, 'ro', ms=echelle*priorite)
        plt.text(x, y, ville, va="center", ha="center")
    plt.show()

## déclaration des fonctions
def DureeDijkstra(G, depart, arrivee):
    fileP = heapdict()
    distance = {}
    for sommet in G:
        distance[sommet] = float("inf")
        fileP[sommet] = float("inf")
    distance[depart] = 0
    fileP[depart] = 0
    SommetsVisites = []
    while fileP:
        sommet, priorite = fileP.popitem()
        SommetsVisites.append( (sommet, priorite) )
        if sommet == arrivee:
            return distance[sommet], SommetsVisites
        for sommetAdj, poids in G[sommet]:
            if sommetAdj in fileP:
                d_alt = distance[sommet] + poids
                if d_alt < distance[sommetAdj]:
                    distance[sommetAdj] = d_alt
                    fileP[sommetAdj] = d_alt

def DureeAetoile(G, depart, arrivee, heuristique):
    fileP = heapdict()
    distance = {}
    for sommet in G:
        distance[sommet] = float("inf")
        fileP[sommet] = float("inf")
    distance[depart] = 0
    fileP[depart] = 0 + heuristique(depart, arrivee)
    SommetsVisites = []
    while fileP:
        sommet, priorite = fileP.popitem()
        SommetsVisites.append( (sommet, priorite) )
        if sommet == arrivee:
            return distance[sommet], SommetsVisites
        for sommetAdj, poids in G[sommet]:
            if sommetAdj in fileP:
                d_alt = distance[sommet] + poids
                if d_alt < distance[sommetAdj]:
                    distance[sommetAdj] = d_alt
                    fileP[sommetAdj] = d_alt + heuristique(sommetAdj, arrivee)

def heuristique(ville1, ville2):
    return 0
    # return k * VolOiseau(ville1, ville2)

## programme principal

d, L = DureeDijkstra(G, "Bordeaux", "Reims")
print(d)
representationVisite(L, 0.05, "Dijkstra")

d, L = DureeDijkstra(G, "Reims", "Bordeaux")
print(d)
representationVisite(L, 0.05, "Dijkstra")

d, L = DureeAetoile(G, "Reims", "Bordeaux", heuristique)
print(d)
representationVisite(L, 0.05, "A*")

