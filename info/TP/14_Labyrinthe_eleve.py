# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 14:14:15 2023
@author: xavier.pessoles2
"""
from collections import deque
import matplotlib.pyplot as plt
import random

## Question 1 ##
def creer_graphe(p:int, n:int) -> dict:
    # n : lignes
    # p : colonnes
    G = {}
    sommets = []
    for i in range(n):
        for j in range(p):
            sommets.append((j,i))
    
    for sommet in sommets : 
        (i,j) = sommet
        voisins = [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]
        # On vérifie que les voisins sont dans les sommets
        vv = []
        for v in voisins : 
            if v in sommets : 
                vv.append(v)
        G[sommet]=vv
    return G

## Question 2 ##
def get_sommets(G:{}) -> ([],[]):
    # On trace les sommets
    les_x,les_y = [],[]
    for sommet in G.keys() : 
        les_x.append(sommet[0])
        les_y.append(sommet[1])
    return les_x,les_y
                
## Question 3 ##
def trace_sommets(G:{}) :
    # On trace les sommets
    les_x,les_y = [],[]
    for sommet in G.keys() : 
        les_x.append(sommet[0])
        les_y.append(sommet[1])
    plt.plot(les_x,les_y,".",color="royalblue")
    
    plt.grid()
    plt.axis("equal")
    plt.show()
                

## Question 4 ##
def get_aretes(G):
    edges = []
    for sommet,voisins in G.items():
        for v in voisins : 
            edge = (sommet,v)
            if (sommet,v) not in edges : 
                if (v,sommet) not in edges : 
                    edges.append(edge)
    return edges

## Question 5 ##
def tracer_aretes(G) :
    # On trace les arrêtes    
    edges = get_aretes(G)
    for edge in edges : 
        x = [edge[0][0],edge[1][0]]
        y = [edge[0][1],edge[1][1]]
        plt.plot(x,y,'lightcoral')
    
    plt.grid()
    plt.axis("equal")
    plt.show()

## Question 6 ##
def tracer_graphe(G) :
    # On trace les arrêtes    
    edges = get_aretes(G)
    for edge in edges : 
        x = [edge[0][0],edge[1][0]]
        y = [edge[0][1],edge[1][1]]
        plt.plot(x,y,'lightcoral')
    
    # On trace les sommets
    les_x,les_y = [],[]
    for sommet in G.keys() : 
        les_x.append(sommet[0])
        les_y.append(sommet[1])
    plt.plot(les_x,les_y,".",color="royalblue")
    
    plt.grid()
    plt.axis("equal")
    plt.show()

## TEST ##
G = creer_graphe(10,8)
tracer_graphe(G)


### PARCOURS ###
def parcours_largeur(G,depart) :
    visited = {}    
    for sommet in G.keys():
        visited[sommet] = False
    file = deque([depart])
    while len(file) > 0:
        s = file.pop()
        if visited[s] == False:
            visited[s] = True
            voisins = G[s]
            for v in voisins:
                file.appendleft(v)


def parcours_profondeur(G,depart) :
    visited = {}    
    for sommet in G.keys():
        visited[sommet] = False
    pile = deque([depart])
    
    while len(pile) > 0:
        s = pile.pop()
        if visited[s] == False:
            visited[s] = True
            voisins = G[s]
            for v in voisins:
                pile.append(v)
