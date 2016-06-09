def lit_valeurs(nom_de_fichier):
    """Lit le contenu du fichier image f et retourne la liste des
      valeurs lues (séparées par des blancs) sous forme d'une liste
      de chaines de caractères. La première valeur est normalement
      'P2'."""
    with open(nom_de_fichier, 'r') as f:
        c = f.read()
    return c.split()
