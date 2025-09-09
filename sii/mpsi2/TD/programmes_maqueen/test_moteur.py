from microbit import *

def moteurDroit(sens, vitesse):
    i2c.write(0x10, bytearray([2, sens, vitesse]))

def moteurGauche(sens, vitesse):
    i2c.write(0x10, bytearray([0, sens, vitesse]))

moteurDroit(0, 255)
moteurGauche(1, 255)

