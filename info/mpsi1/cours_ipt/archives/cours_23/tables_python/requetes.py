from bdd import *

def get_id_nom_personne(nom):
    """Renvoie une liste des id des personnes dont le nom donné"""
    L = []
    for a in personnes:
        if a[1] == nom :
            L.append(a[0])
    return L

def get_id_titre_film(titre):
    """Renvoie une liste des id des films dont le titre est donné"""
    L = []
    for a in films:
        if a[1] == titre :
            L.append(a[0])
    return L

def get_nomprenom_id_personne(i):
    """Renvoie le couple (nom,prenom) de la personne d'id i"""
    for a in personnes :
        if a[0] == i:
            return (a[1],a[2])
    return None

def get_nom_id_personnage(i):
    """Renvoie le nom du personnage d'id i"""
    for a in personnages:
        if a[0] == i:
            return a[1]
    return None

def nom_prenom_acteurs_film(titre):
    """Renvoie une liste (nom, prenom, personnage) des personnages ayant joué dans le film dont le titre est donné"""
    L = []
    films_id = get_id_titre_film(titre)
    for j in joue:
        if j[1] in films_id:
            n,m = get_nomprenom_id_personne(j[0])
            p = get_nom_id_personnage(j[2])
            L.append((n,m,p))
    return L
