# -*- coding: utf-8 -*-

class pile:

    def __init__(self):
        self.valeurs = []

    def empiler(self, valeur):
        self.valeurs.append(valeur)

    def depiler(self):
        assert self.valeurs, 'fonction depiler appliquée à une pile vide !'
        return self.valeurs.pop()

    def estVide(self):
        return self.valeurs == []

class file:

    def __init__(self):
        self.valeurs = []

    def enfiler(self, valeur):
        self.valeurs.append(valeur)

    def defiler(self):
        assert self.valeurs, 'fonction defiler appliquée à une file vide !'
        return self.valeurs.pop(0)

    def estVide(self):
        return self.valeurs == []