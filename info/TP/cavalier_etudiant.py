# -*- coding: utf-8 -*-

## importation des modules
from collections import deque

## déclaration des fonctions

def parcoursProfondeur(G):
    def explorationProfondeur(s):
        parcouru[s] = True
        for ss in G[s]: # G[s] liste des successeurs de s dans G
            if not parcouru[ss]:
                explorationProfondeur(ss) # appel récursif
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False # initialisation du marquage
    for r in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        if not parcouru[r]:
            explorationProfondeur(r)

def parcoursLargeur(G):
    def explorationLargeur(r):
        f = deque() # initialisation d'une deque vide
        f.append(r)
        parcouru[r] = True
        while f:    # Vrai tant que f est non-vide
            s = f.popleft()
            for ss in G[s]: # G[s] liste des successeurs de s dans G
                if not parcouru[ss]:
                    f.append(ss)
                    parcouru[ss] = True
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False # initialisation du marquage
    for r in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        if not parcouru[r]:
            explorationLargeur(r)


## programme principal
