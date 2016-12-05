def affiche(nom_de_fichier):
    """Affiche nom_de_fichier, ligne par ligne"""
    with open(nom_de_fichier,'r') as f :
        # f == open(nom_de_fichier,'r')
        L = f.readlines()
    # Ici, f est fermé
    for x in L :
        print(x.strip('\n'))
    return None

def affiche_bis(nom_de_fichier):
    """Affiche nom_de_fichier, ligne par ligne"""
    with open(nom_de_fichier,'r') as f :
        # f == open(nom_de_fichier,'r')
        s = f.read()
    # Ici, f est fermé
    print(s)
    return None
