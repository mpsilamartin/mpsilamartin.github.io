# -*- coding: utf-8 -*-

## importation des modules
import MyTurtle as t

## déclaration des fonctions
def ligneBase(L):
    t.forward(L)  # avancer de L
    t.left(60)    # tourner de +60°
    t.forward(L)  # avancer de L
    t.right(120)  # tourner de -120°
    t.forward(L)  # avancer de L
    t.left(60)    # tourner de +60°
    t.forward(L)  # avancer de L

## programme principal
t.reset()
ligneBase(1)
t.show()


