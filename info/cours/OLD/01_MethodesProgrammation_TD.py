# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 09:19:36 2022

@author: xavier.pessoles2
"""

def distance(p1:list, p2:list) -> float:
    """
    Déterminer les distances entre deux points de l'espace. 
    Entrées : 
     - p1:list : liste des coordonnées (x1,y1,z1) du point 1
     - p2:list : liste des coordonnées (x2,y2,z2) du point 2
    Sortie :
     - distance entre p1 et p2
    """
    assert len(p1)==3 and len(p2)==3
    d0 = p2[0]-p1[0]
    d1 = p2[1]-p1[1]
    d2 = p2[2]-p1[2]
    d = (d0**2+d1**2+d2**2)**(1/2)
    return d

def test_distance():
    p1 = [0,0,0]
    p2 = [0,0,0]
    assert distance(p1,p2) == 0
    p1 = [1,0,0]
    p2 = [0,0,0]
    assert distance(p1,p2) == 1



def longueur(L:list)->float:
    """
    Déterminer a longueur du chemin L
    Entrée : 
     - L:list : liste des points constitués de leurs cordonnées : [[x0,y0,z0],...[xn,yn,zn]]
    Sortie :
     - longeur du chemin
    """
    # Test à l'entrée
    for pt in L :
        assert len(pt)==3
    
    l = 0
    for i in range(len(L)-1):
        l = l+distance(L[i],L[i+1])
    return l