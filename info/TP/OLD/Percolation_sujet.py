# === Import des modules ===
import numpy as np
import matplotlib.pyplot as plt

from numpy.random import rand
from matplotlib.colors import ListedColormap

# === Fonctions prédéfinies ===
def sauvegarder_grille(grille : list, nom_de_fichier : str) -> None:
    # Echelle Blanc : 0, Noir : 1, Blue : 2
    echelle = ListedColormap(['white','black','aqua'],2)
    plt.matshow(grille,cmap=echelle,vmin=0,vmax=2)
    plt.colorbar()
    plt.savefig(nom_de_fichier)
    return None

def afficher_grille(grille : list) -> None:
    echelle = ListedColormap(['white','black','aqua'],2)
    plt.matshow(grille,cmap=echelle,vmin=0,vmax=2)
    plt.colorbar()
    plt.show()
    return None
# ==============================
