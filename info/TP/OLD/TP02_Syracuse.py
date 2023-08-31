# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 14:47:54 2021

@author: jphbe
"""

## Q1

def tempsdevol(c:int):
    u=c
    n=0
    while u!=1:
        if u%2==0:
            u=u//2
        else:
            u=3*u+1
        n=n+1
    return(n)

## Q2

def altitude(c:int):
    u=c
    M=c
    n=0
    while u!=1:
        if u%2==0:
            u=u//2
        else:
            u=3*u+1
        n=n+1
        if u>M:
            M=u
    return(M)

## Q3

def tempsdarret(c:int):
    if c==1:
        n=0
    else:
        u=c
        n=0
        while u>=c:
            if u%2==0:
                u=u//2
            else:
                u=3*u+1
            n=n+1
    return(n)

## Q4

import time as t

def verification(m:int):
    tps=t.time()
    for c in range(2,m+1):
        tempsdarret(c)
    return(t.time()-tps)
    

## Q5

# Si c est pair, le temps d'arrêt vaut 1
# Si c=4n+1, u1=12n+4, u2=6n+2, u3=3n+1: le temps d'arret est donc 3
# Il ne reste que les nombres impairs congrus à 3 modulo 4 ie de la forme 3n+4



def verification2(m:int):
    tps=t.time()
    k=0
    while 4*k+3<=m:
        tempsdarret(4*k+3)
        k=k+1
    return(t.time()-tps)

## Q6

def max_altitude():
    M=0
    for c in range(1,1000001):
        alt=altitude(c)
        if alt>M:
            M=alt
            cmin=c
    return(M,cmin)

## Q7

def max_tempsdarret():   # On se limite à c=4n+3
    M=0
    n=0
    while 4*n+3<=1000000:
        t=tempsdarret(4*n+3)
        if t>M:
            M=t
            cmin=4*n+3
        n=n+1
    return(M,cmin)

## Q8

def record():
    liste=[]
    for c in range(1,1000000):
        t=tempsdarret(c)
        i=1
        while i<=c-1 and tempsdarret(i)<=t:
            i=i+1
        if i==c:
            liste.append(c)
    return(liste)

## Q9 Affichage de vol

import matplotlib.pyplot as plt

def graphique(c:int):
    t=tempsdarret(c)
    les_x=[i for i in range(t)]
    les_y=[c]
    u=c
    for i in range(1,t):
        if u%2==0:
            u=u//2
        else:
            u=3*u+1
            
        les_y.append(u)
    plt.plot(les_x,les_y)
    plt.xlabel("n")
    plt.ylabel("u(n)")
    plt.show()
    