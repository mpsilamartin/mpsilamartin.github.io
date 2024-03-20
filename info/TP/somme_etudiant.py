# -*- coding: utf-8 -*-

## importation des modules
import random as r
from piles_files import *

## déclaration des fonctions

## programme principal
r.seed(0)

p = pile()
for i in range(10):
    nb = r.randint(0, 9)
    p.empiler(nb)

# placer l'affichage de la pile après la somme
# pour vérifier que la pile est intacte
while not p.estVide():
    elt = p.depiler()
    print(elt)
