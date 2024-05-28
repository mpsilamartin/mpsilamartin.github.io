# -*- coding: utf-8 -*-

## importation des modules
import numpy as np

## lecture données depuis Mduree.csv

Mstr = np.loadtxt( "Mduree.csv",
                delimiter=',',
                skiprows=1,
                usecols=range(1, 51),
                dtype='str',
                encoding="UTF-8").tolist()

Villes = np.loadtxt( "Mduree.csv",
                delimiter=',',
                skiprows=1,
                usecols=0,
                dtype='str',
                encoding="UTF-8").tolist()

## déclaration des fonctions


## programme principal

