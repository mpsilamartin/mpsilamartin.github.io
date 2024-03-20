# -*- coding: utf-8 -*-

## importation des modules
import random as r
from piles_files import *

## déclaration des fonctions
def affichageFile(f):
    f.enfiler(None)
    x = f.defiler()
    while x != None:
        print(x)
        f.enfiler(x)
        x = f.defiler()

## programme principal
r.seed(0)

f = file()
for i in range(10):
    nb = r.randint(0, 99)
    f.enfiler(nb)

# placer l'affichage de la file après le
# maximum pour vérifier l'état de la file
affichageFile(f)
