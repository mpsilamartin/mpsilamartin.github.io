# -*- coding: utf-8 -*-

## importation des modules
import matplotlib.pyplot as plt
import numpy as np

## déclaration des fonctions
def reset():
    """ Initialise le stylo """
    global pos, dir, dessin, down, ax, fig
    down = True # stylo
    dir = 0
    pos = {}
    dessin = {}
    for coor in ['x', 'y']:
        pos[coor] = 0
        dessin[coor] = [[pos[coor]]]
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.axis("equal")
    ax.axis("off")

def goto(x, y):
    """ Met le stylo en position (x, y) """
    global pos, dessin, down
    pos['x'], pos['y'] = x, y
    if down:
        for coor in ['x', 'y']:
            dessin[coor][-1].append(pos[coor])

def forward(l):
    """ Avance de l """
    global pos, dessin, down
    pos['x'] += l*np.cos(dir*np.pi/180)
    pos['y'] += l*np.sin(dir*np.pi/180)
    if down:
        for coor in ['x', 'y']:
            dessin[coor][-1].append(pos[coor])

def backward(l):
    """ Recule de l """
    global pos, dessin, down
    pos['x'] -= l*np.cos(dir*np.pi/180)
    pos['y'] -= l*np.sin(dir*np.pi/180)
    if down:
        for coor in ['x', 'y']:
            dessin[coor][-1].append(pos[coor])

def left(angle):
    """ Tourne de angle (en degrés) à gauche """
    global dir
    dir += angle

def right(angle):
    """ Tourne de angle (en degrés) à droite """
    global dir
    dir -= angle

def penup():
    """ Lève le stylo """
    global down, dessin
    down = False
    for coor in ['x', 'y']:
        dessin[coor].append([])

def pendown():
    """ Baisse le stylo """
    global down, dessin
    down = True
    for coor in ['x', 'y']:
        dessin[coor][-1].append(pos[coor])

def show():
    """ Montre le dessin """
    global ax
    for i in range(len(dessin['x'])):
        ax.plot(dessin['x'][i], dessin['y'][i], 'k-')
    plt.show()

if __name__ == "__main__":
    reset()
    forward(1)
    left(60)
    forward(1)
    right(120)
    forward(1)
    left(60)
    forward(1)
    show()
    reset()
    forward(1)
    penup()
    goto(0,1)
    pendown()
    forward(1)
    penup()
    goto(0,2)
    pendown()
    forward(1)
    show()
    reset()
    right(90)
    forward(1)
    goto(2,0)
    forward(1)
    right(180)
    penup()
    backward(1)
    pendown()
    backward(3)
    left(90)
    forward(2)
    show()



