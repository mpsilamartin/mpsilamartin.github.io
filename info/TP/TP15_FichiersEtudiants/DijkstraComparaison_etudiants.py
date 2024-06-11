# -*- coding: utf-8 -*-

## importation des modules
import numpy as np
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

## déclaration des fonctions

def DureeDijkstraD(G, depart): # dictionnaire comme file
    def popMin(fileP):
        mini = float("inf")
        for sommet, priorite in fileP.items():
            if priorite < mini :
                mini = priorite
                sommetMini = sommet
        del fileP[sommetMini]
        return sommetMini, mini
    fileP = dict()
    for sommet in G:
        fileP[sommet] = float("inf")
    fileP[depart] = 0
    distance = {}
    while fileP:
        sommet, dureeDepartSommet = popMin(fileP)
        distance[sommet] = dureeDepartSommet
        for sommetAdj, poids in G[sommet]:
            if sommetAdj in fileP:
                d_alt = dureeDepartSommet + poids
                if d_alt < fileP[sommetAdj]:
                    fileP[sommetAdj] = d_alt
    return distance

def DureeDijkstraHd(G, depart):
    fileP = heapdict()
    for sommet in G:
        fileP[sommet] = float("inf")
    fileP[depart] = 0
    distance = {}
    while fileP:
        sommet, dureeDepartSommet = fileP.popitem()
        distance[sommet] = dureeDepartSommet
        for sommetAdj, poids in G[sommet]:
            if sommetAdj in fileP:
                d_alt = dureeDepartSommet + poids
                if d_alt < fileP[sommetAdj]:
                    fileP[sommetAdj] = d_alt
    return distance


## programme principal

tic = perf_counter_ns()
# code dont il faut vérifier la performance
toc = perf_counter_ns()
print("Temps de calcul entre tic et toc : ", (toc - tic)*1e-9, "s")

