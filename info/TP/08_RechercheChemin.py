# -*- coding: utf-8 -*-

# ==== NE PAS MODIFIER =====
import numpy as np
dim = 100
n=10
# ==== FIN A NE PAS MODIFIER =====




# Question 1
############
def distance(p1:list, p2:list) -> float:
    # A compléter    
    return 0.

def Q1_test():
    """ Fonction de test pour la question 1."""
    A, p1, p2 = [0,0], [2,4], [6,5]
    return (distance(A,p1) > 4.472135) and (distance(p1,p2) < 4.472136)
 
    
# Question 2
############
def distances(pts, dep):
    # A compléter    
    return []

def Q2_test():
    """ Fonction de test pour la question 2."""
    A, p1, p2, p3 = [0,0], [2,4], [6,5], [5,1]
    pts = [p1,p2,p3]
    dist = distances(pts, A)
    tab_dist = [[0, 4.123105625617661, 4.242640687119285, 4.47213595499958], [4.123105625617661, 0, 4.123105625617661, 7.810249675906654], [4.242640687119285, 4.123105625617661, 0, 5.0990195135927845], [4.47213595499958, 7.810249675906654, 5.0990195135927845, 0]]
    return np.allclose(np.array(tab_dist),np.array(dist))

# Question 3
############
ques_3 = 0  # Modifier le 0 par votre réponse (en fonction de n)

# Question 4
############
def longueur(chemin, dist):
    # A compléter    
    return 0.

def Q4_test():
    """ Fonction de test pour la question 7."""
    chemin = [3,2,1,0]
    tab_dist = [[0, 4.123105625617661, 4.242640687119285, 4.47213595499958], [4.123105625617661, 0, 4.123105625617661, 7.810249675906654], [4.242640687119285, 4.123105625617661, 0, 5.0990195135927845], [4.47213595499958, 7.810249675906654, 5.0990195135927845, 0]]
    d = longueur(chemin, tab_dist)
    return (d > 13.34523076) and (d < 13.34523077)
    

# Question 5
############
def longueur_rec(chemin, dist):
    # A compléter    
    return 0.

# Question 6
############
ques_6_pts  = 0 # A compléter
ques_6_pts_parc  = 0 # A compléter
ques_6_pts_parc_liste = "" # Chaine de caractères sous la forme "a,p1,p2,p3"


# Question 7
#############
ques_7  = "" # A compléter


# Question 8
#############
def indice(position, dist, dispo):
    # A compléter    
    return 0

def Q8_test():
    """ Fonction de test pour la question 8."""
    dispo = [False, True, True, False]
    tab_dist = [[0, 4.123105625617661, 4.242640687119285, 4.47213595499958], [4.123105625617661, 0, 4.123105625617661, 7.810249675906654], [4.242640687119285, 4.123105625617661, 0, 5.0990195135927845], [4.47213595499958, 7.810249675906654, 5.0990195135927845, 0]]
    return 1 == indice(0, tab_dist, dispo)
    
# Question 9
#############
def plus_court(dist):
    # A compléter    
    return []

def Q9_test():
    """ Fonction de test pour la question 9."""
    tab_dist = [[0, 4.123105625617661, 4.242640687119285, 4.47213595499958], [4.123105625617661, 0, 4.123105625617661, 7.810249675906654], [4.242640687119285, 4.123105625617661, 0, 5.0990195135927845], [4.47213595499958, 7.810249675906654, 5.0990195135927845, 0]]
    return  plus_court(tab_dist) == [0, 1, 2]



# Question 10
#############

def plot_chemin():
    from random import randint
    nbpoints, dim = 20, 20
    def points(n, c):
        liste = []
        while len(liste) < n:
            x = randint(-c, c)
            y = randint(-c, c)
            if [x, y] not in liste:
                liste.append([x, y])
        return liste
    
    depart = (randint(-dim, dim), randint(-dim, dim))
    import matplotlib.pyplot as plt
    pts = points(nbpoints, dim)
    x = [u[0] for u in pts]
    y = [u[1] for u in pts]
    plt.plot(x, y, "x")
    plt.plot(depart[0], depart[1], "+")
    plt.show()
    
    tableau = distances(pts, depart)
    ch = plus_court(tableau)

    xliste = [depart[0]] + [pts[k][0] for k in ch]
    yliste = [depart[1]] + [pts[k][1] for k in ch]
    plt.plot(x, y, "bo") # affichage des points
    plt.plot(depart[0], depart[1], "rs")
    plt.plot(xliste, yliste,"b") # affichage du chemin
    plt.grid()
    plt.xlim(-dim,dim)
    plt.ylim(-dim,dim)
    plt.axis("equal")
    plt.show()
