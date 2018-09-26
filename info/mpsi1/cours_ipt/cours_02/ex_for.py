prenoms = ["Hind",
           "Louis",
           "Nicolas", 
           "Florian",
           "Tom",
           "Émeric",
           "Aloïs",
           "Ambélina", 
           "Pierre",
           "Frédéric",
           "Quentin",
           "Clémence",
           "Alice",
           "Alexane",
           "Anaëlle",
           "Léo",
           "Thaïs",
           "Alice",
           "Nathan",
           "Alexandre",
           "Marius",
           "Théo",
           "Emmanuel",
           "Clara",
           "Nathan",
           "Ayman",
           "Clément",
           "Julia",
           "Melvin",
           "David Ndombele",
           "Anthony",
           "Joël",
           "Pierre",
           "Jade",
           "Lalou",
           "Louis",
           "Colette",
           "Loïc",
           "Zacharie",
           "Aymen",
           "Mathis",
           "Louis",
           "Benjamin",
           "Julien",
           "Florian"
]

def affiche1(prenoms) : 
    """Souhaite le bonjour à tous les étudiants"""
    for petitcoeur in prenoms:
        print("Bonjour " + petitcoeur)
    return None

def ex_range(a,b):
    for i in range(a,b):
        print(i)

def affiche2(prenoms) : 
    """Souhaite le bonjour à tous les étudiants"""
    n = len(prenoms)
    for i in range(n):
        print("Bonjour " + prenoms[i])
    return None


