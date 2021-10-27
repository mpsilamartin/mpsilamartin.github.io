# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 16:03:15 2021

@author: jphbe
"""

## Q1

def generate_pair_01(nb:int):
    res=[]
    for i in range(1,nb//2):
        res.append(2*i)
    return(res)

# print(generate_pair_01(0),generate_pair_01(9),generate_pair_01(10))

## Q2 à Q5

def generate_pair_02(nb:int):
    res=[]
    i=1
    while i<nb//2:
        res.append(2*i)
        i=i+1
    return(res)

def recherche_nb_01(nb:int,L:list):
    test=False
    for x in L:
        if nb==x:
            test=True
    return(test)

def recherche_nb_02(nb:int,L:list):
    n=len(L)
    i=0
    while i<=n-1 and nb!=L[i]:
        i=i+1
    return(i<n)

def recherche_nb_03(nb:int, L:list):
    return(nb in L)


## Q6 à Q10

def recherche_first_index_nb_01(nb:int, L:list):
    n=len(L)
    index=-1
    for i in range(n):
        if nb==L[i] and index==-1:
            index=i
    return(index)
        
def recherche_first_index_nb_02(nb:int, L:list):
    n=len(L)
    i=0
    while i<=n-1 and nb!=L[i]:
        i=i+1
    if i<n:
        index=i
    else:
        index=-1
    return(index)

def recherche_last_index_nb_01(nb:int, L:list):
    n=len(L)
    index=-1
    for i in range(n):
        if nb==L[i]:
            index=i
    return(index)

def recherche_last_index_nb_02(nb:int, L:list):
    n=len(L)
    i=n-1   # On part de la fin de la liste
    while i>=0 and nb!=L[i]:
        i=i-1
    if i>0:
        index=i
    else:
        index=-1
    return(index)


def recherche_index_nb_01(nb:int, L:list):
    res=[]
    n=len(L)
    for i in range(n):
        if L[i]==nb:
            res.append(i)
    return(res)


## Q11 et Q12

def is_char_in_str_01(lettre:str,mot:str):
    n=len(mot)
    i=0
    while i<=n-1 and lettre!=mot[i]:
        i=i+1
    return(i<n)


def is_char_in_str_02(lettre:str,mot:str):
    return(lettre in mot)

## Q13

def compte_lettre_01(lettre:str, mot:str):
    nb=0
    for x in mot:
        if x==lettre:
            nb=nb+1
    return(nb)

#######

alphabet='abcdefghijklmnopqrstuvwxyz'
def load_fichier(file):
    f=open(file,'r')
    mots=f.readlines()
    f.close()
    dico=[]
    for mot in mots:
        dico.append(mot.strip())
    return dico

dictionnaire=load_fichier('liste_francais.txt')

## Q14

def compte_lettre_02(lettre:str, mots:str):
    nb=0
    for mot in mots:
        if lettre in mot:
            nb=nb+1
    return(nb)

## Q15

def nb_consonnes(mots):
    consonnes='bcdfghjklmnpqrstvwxz'
    L=[compte_lettre_02(lettre,mots) for lettre in consonnes]
    m,M=L[0],L[0]   # Min et Max des occurrences
    lettre_min=consonnes[0]
    lettre_max=consonnes[0]
    n=len(L)
    for i in range(n):
        if L[i]<m:
            lettre_min=consonnes[i]
            m=L[i]
        if L[i]>M:
            lettre_max=consonnes[i]
            M=L[i]
    occ_consonnes_min=[compte_lettre_02(lettre_min,mot) for mot in mots]
    occ_consonnes_max=[compte_lettre_02(lettre_max,mot) for mot in mots]
    return('consonne_max: '+ lettre_max +' '+ str(M)+ ' fois; '+ 'consonne_min: '+ lettre_min+' '+ str(m)+ ' fois.')
    
## Q 16

def mots_plus_long(mots:list):
    M=0
    for mot in mots:
        if len(mot)>M:
            max=mot
            M=len(mot)
    return(max)

## Q17

def cherche_mot_in_chaine_01(mot:str,chaine=str):
    p,n=len(mot), len(chaine)
    j=0
    test=False
    while j<=n-p and test==False:
        i=0
        while i<=p-1 and mot[i]==chaine[i+j]:
            i=i+1
        test=(i==p)
        j=j+1
    return(test)
        
## Q18

def cherche_mot_in_chaine_02(mot:str,chaine=str):
    return(mot in chaine)

## Q19

def cherche_mot_in_dico(nb:int,dico:list):
    # on isole les mots de nb lettres dans liste
    liste=[]
    for mot in dico:
        if len(mot)==nb:
            liste.append(mot)
    M=0
    mot_nb=liste[0]
    for l in liste:   # On compte les occurrences et on prend le max
        n=0
        for mot in dico:
            if cherche_mot_in_chaine_01(l,mot):
                n=n+1
        if n>M:
            M=n
            mot_nb=l
    return(mot_nb)
    

        