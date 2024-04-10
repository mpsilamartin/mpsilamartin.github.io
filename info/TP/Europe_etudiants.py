# -*- coding: utf-8 -*-

## importation des modules
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

## déclaration des sommets et arêtes
pays = [
    "AL", # Albanie
    "DE", # Allemagne
    "AD", # Andorre
    "AT", # Autriche
    "BY", # Bélarus
    "BE", # Belgique
    "BA", # Bosnie-Herzégovine
    "BG", # Bulgarie
    "CY", # Chypre
    "HR", # Croatie
    "DK", # Danemark
    "ES", # Espagne
    "EE", # Estonie
    "FI", # Finlande,
    "FR", # France
    "GR", # Grèce
    "HU", # Hongrie
    "IE", # Irlande
    "IS", # Islande
    "IT", # Italie
    "LV", # Lettonie,
    "LI", # Liechtenstein
    "LT", # Lituanie
    "LU", # Luxembourg
    "MK", # Macédoine
    "MT", # Malte,
    "MD", # Moldavie
    "MC", # Monaco
    "ME", # Monténégro
    "NO", # Norvège
    "NL", # Pays-Bas
    "PL", # Pologne
    "PT", # Portugal
    "RO", # Roumanie
    "GB", # Royaume-Uni
    "RU", # Russie
    "SM", # Saint-Marin
    "VA", # Vatican
    "RS", # Serbie
    "SK", # Slovaquie
    "SI", # Slovénie
    "SE", # Suède
    "CH", # Suisse
    "CZ", # République Tchèque
    "TR", # Turquie
    "UA"] # Ukraine

frontieres = [
    ['AL', 'GR'], ['AL', 'MK'], ['AL', 'ME'], ['AL', 'RS'], ['DE', 'DK'],
    ['DE', 'FR'], ['DE', 'LU'], ['DE', 'NL'], ['DE', 'PL'], ['AD', 'ES'],
    ['AD', 'FR'], ['AT', 'DE'], ['AT', 'HU'], ['AT', 'IT'], ['AT', 'LI'],
    ['AT', 'SK'], ['AT', 'SI'], ['AT', 'CH'], ['AT', 'CZ'], ['BY', 'LV'],
    ['BY', 'LT'], ['BY', 'PL'], ['BY', 'RU'], ['BY', 'UA'], ['BE', 'DE'],
    ['BE', 'FR'], ['BE', 'LU'], ['BE', 'NL'], ['BA', 'HR'], ['BA', 'ME'],
    ['BA', 'RS'], ['BG', 'GR'], ['BG', 'MK'], ['BG', 'RO'], ['BG', 'RS'],
    ['BG', 'TR'], ['CY', 'GB'], ['HR', 'HU'], ['HR', 'ME'], ['HR', 'RS'],
    ['HR', 'SI'], ['ES', 'FR'], ['ES', 'PT'], ['ES', 'GB'], ['EE', 'LV'],
    ['EE', 'RU'], ['FI', 'NO'], ['FI', 'RU'], ['FI', 'SE'], ['FR', 'IT'],
    ['FR', 'LU'], ['FR', 'MC'], ['GR', 'MK'], ['GR', 'TR'], ['HU', 'RO'],
    ['HU', 'RS'], ['HU', 'SK'], ['HU', 'SI'], ['HU', 'UA'], ['IT', 'SM'],
    ['IT', 'VA'], ['IT', 'SI'], ['LV', 'RU'], ['LT', 'LV'], ['LT', 'PL'],
    ['LT', 'RU'], ['MK', 'RS'], ['MD', 'RO'], ['MD', 'UA'], ['ME', 'RS'],
    ['NO', 'RU'], ['NO', 'SE'], ['PL', 'RU'], ['PL', 'SK'], ['PL', 'UA'],
    ['RO', 'RS'], ['RO', 'UA'], ['GB', 'IE'], ['RU', 'UA'], ['SK', 'UA'],
    ['CH', 'DE'], ['CH', 'FR'], ['CH', 'IT'], ['CH', 'LI'], ['CZ', 'DE'],
    ['CZ', 'PL'], ['CZ', 'SK']]

## déclaration des fonctions
def dessinerGraphe(G):
    plt.figure()
    nx.draw(G, with_labels=True, pos=nx.shell_layout(G))
    plt.show()

## déclaration des variables
G = nx.Graph()
G.add_nodes_from(pays)
G.add_edges_from(frontieres)
dessinerGraphe(G)


