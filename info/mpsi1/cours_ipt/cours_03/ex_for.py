prenoms = ["Jeffrey",
           "Fatime Zhoura",
           "Bénédicte",
           "Samuel",
           "Abdourahmane",
           "Anjdy",
           "Camille",
           "Anna",
           "Théotime",
           "Yann",
           "Amélie",
           "Gaëtan",
           "Gaëtan",
           "Lenaïg",
           "Robin",
           "Marina",
           "Timothée",
           "Sarah",
           "Alix",
           "Sylvio",
           "Mohamad-Mehdi",
           "Nicolas",
           "Ryad",
           "Clément",
           "Romain",
           "David",
           "Yassine",
           "Bastien",
           "Louise",
           "Tetautahi",
           "Nicolas",
           "Van Sang Denny",
           "Lise",
           "David",
           "Ianis",
           "Valentin",
           "Thibault",
           "Arthur",
           "Clara",
           "Emma",
           "Simon",
           "Mathieu",
           "Chloé",
           "Alexandre",
           "Thomas",
           "Laureen",
           "Julien"
]

def affiche1(prenoms) : 
    """Souhaite le bonjour à tous les étudiants"""
    for petitcoeur in prenoms:
        print("Bonjour " + petitcoeur)
    return None


def affiche2(prenoms) : 
    """Souhaite le bonjour à tous les étudiants"""
    n = len(prenoms)
    for i in range(n):
        print("Bonjour " + prenoms[i])
    return None

def ex_range(a,b):
    for i in range(a,b):
        print(i)
    return None

