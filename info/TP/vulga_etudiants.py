# -*- coding: utf-8 -*-

## importation des modules
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

## déclaration des fonctions
def dessinerGraphe(G):
    plt.figure()
    nx.draw(G, with_labels=True, pos=nx.shell_layout(G))
    plt.show()

## déclaration des sommets et arcs
sommets = ['Dr Nozman', 'Doc Seven', 'FabienOlicard', 'DirtyBiology',
    'ScienceEtonnante', 'e-penser 2.0', 'Nota Bene', "C'est pas sorcier",
    'Max Bird', 'Axolot', 'Mickaël Launay', "C'est une autre histoire",
    'Jamy - Epicurieux', 'Balade Mentale', 'Les Revues du Monde', 'AstronoGeek',
    'Tu mourras moins bête - ARTE', 'Poisson Fécond', 'Scilabus',
    'Dans Ton Corps', 'Allo Docteurs', "Secrets d'Histoire Officiel ",
    'Cyrus North', "L'Antiseche"]

arcs = [
    ['Nota Bene', 'Axolot'], ['Nota Bene', "C'est une autre histoire"],
    ["C'est pas sorcier", 'Max Bird'], ["C'est pas sorcier", 'Jamy - Epicurieux'],
    ["C'est pas sorcier", 'Allo Docteurs'],
    ["C'est pas sorcier", "Secrets d'Histoire Officiel "],
    ['Axolot', 'DirtyBiology'], ['Axolot', 'Nota Bene'],
    ['Axolot', 'Mickaël Launay'], ['Axolot', 'Cyrus North'],
    ['Mickaël Launay', 'DirtyBiology'], ['Mickaël Launay', 'Axolot'],
    ['Mickaël Launay', 'Scilabus'], ['Jamy - Epicurieux', "C'est pas sorcier"],
    ['Balade Mentale', "C'est une autre histoire"],
    ['Balade Mentale', 'AstronoGeek'],
    ["Secrets d'Histoire Officiel ", "C'est pas sorcier"],
    ['Cyrus North', "L'Antiseche"], ["L'Antiseche", 'Cyrus North']]


## programme principal
G = nx.DiGraph()
G.add_nodes_from(sommets)
G.add_edges_from(arcs)
dessinerGraphe(G)
