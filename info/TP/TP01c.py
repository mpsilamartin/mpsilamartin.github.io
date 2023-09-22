## TP 01


## 1

def som_impair():
    S=0
    for i in range(5,14):
        S=S+i**3
    return S

## 2

def som_riz():  # Sur la case i, il y a 2**(i-1) grains de riz
    som=0
    for i in range(1,35):
        som=som+2**(i-1)
    return som

def som_riz2():   # On no double que le nombre de la dernière case visitée
    som=1
    nb=1
    for i in range(2,65):
        som=som+2*nb
        nb=2*nb
    return som


## 3

from math import *

def moyenne():
    u,v=3,175
    for i in range(7):
        u,v=sqrt(u*v),(u+v)/2
    return u,v

## 4

def fact(n):
    P=1
    for i in range(1,n+1):
        P=P*i
    return P

print(fact(1), fact(6))

def p_parmi_n(n,p):
    Num=1
    for i in range(p):
        Num=Num*(n-i)
    return(Num//fact(p))

def somme(n):
    S=0
    for p in range(n+1):
        S=S+p_parmi_n(n,p)
    return S

## 5

def rang(eps):
    u=2
    n=1
    while (abs(u-1)>eps):
        u=(1+u)/(2*u)
        n+=1
    return n

print(rang(10**(-5)))

## 6

# Nombre de grain de riz usiné

Nb=45*10**7/0.04


def case_riz():   # On no double que le nombre de la dernière case visitée
    som=1
    nb=1
    case=1
    while som<Nb:
        case+=1
        som=som+2*nb
        nb=2*nb
    return case

## 7

def syracuse(u):
    n=0
    while u!=1:
        if u%2==0:
            u=u//2
        else:
            u=3*u+1
        n+=1
    return n

## 8

from random import random

# Pile= 0 = partie entière du 2*random
# Face= 1 = partie entière de 2*random

def nb_lancers():
    x,y,z=floor(2*random()),floor(2*random()),floor(2*random())
    rang=3
    S=[x,y,z]
    while (x,y,z) != (0,0,0):
        x,y,z=y,z,floor(2*random())
        rang=rang+1
        S=S+[z]
    return S,rang


