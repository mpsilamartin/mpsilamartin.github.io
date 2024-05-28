# -*- coding: utf-8 -*-

## importation des modules
import numpy as np
from time import perf_counter_ns
from collections import deque

## lecture données depuis Gduree.csv

MLLi = np.loadtxt( "Gduree.csv",
                delimiter=',',
                skiprows=1,
                usecols=range(1, 51),
                encoding="UTF-8").tolist()

Villes = np.loadtxt( "Gduree.csv",
                delimiter=',',
                skiprows=1,
                usecols=0,
                dtype='str',
                encoding="UTF-8").tolist()

M = {} # Graphe Mi[s1][s2] -> w12
for i in range(len(MLLi)):
    ville1 = Villes[i]
    Mi[ville1] = {}
    for j in range(len(MLLi)):
        ville2 = Villes[j]
        Mi[ville1][ville2] = MLLi[i][j]

G = {} # Graphe Gi[s1][i] -> (s2, w12)
for i in range(len(MLLi)):
    ville1 = Villes[i]
    Gi[ville1] = []
    for j in range(len(MLLi)):
        ville2 = Villes[j]
        if MLLi[i][j] != 0:
            Gi[ville1].append((ville2, MLLi[i][j]))

## déclaration des fonctions avec un dictionnaire comme file de priorité

def popPrioritaire(fileP):
    mini = float("inf")
    for sommet, priorite in fileP.items():
        if ... :
            mini = ...
            sommetMini = ...
    del fileP[sommetMini]
    return sommetMini, mini

def DureeDijkstraG(G, depart, arrivee):
    fileP = {}
    for sommet in G:
        fileP[sommet] = float("inf")
    fileP[depart] = 0
    while fileP:
        sommet, dureeDepartSommet = popPrioritaire(fileP)
        if sommet == arrivee:
            return dureeDepartSommet
        for sommetAdj, poids in G[sommet]:
            if sommetAdj in fileP:
                d_alt = dureeDepartSommet + poids
                if d_alt < fileP[sommetAdj]:
                    fileP[sommetAdj] = d_alt

def DureeDijkstraM(M, depart, arrivee):
    fileP = {}
    for sommet in M:
        fileP[sommet] = float("inf")
    fileP[depart] = 0
    while fileP:
        sommet, dureeDepartSommet = popPrioritaire(fileP)
        if sommet == arrivee:
            return dureeDepartSommet
        for sommetAdj in M[sommet]:
            if M[sommet][sommetAdj] != 0 and sommetAdj in fileP:
                poids = M[sommet][sommetAdj]
                d_alt = dureeDepartSommet + poids
                if d_alt < fileP[sommetAdj]:
                    fileP[sommetAdj] = d_alt


## programme principal

# tic = perf_counter_ns()
# ...
# toc = perf_counter_ns()
# print((toc-tic)/1e9)

