############################################
#   Librairie pour utilisation du robot    #
#        Maqueen dans Mu editor            #
#  		  par Philippe LECLERC			   #
#			DRANE NORMANDIE                #
#            janvier 2020                  #
############################################
from microbit import *
from machine import time_pulse_us
from music import play, pitch, stop
from time import sleep_ms
import neopixel

LRGB = neopixel.NeoPixel(pin15, 4)

# Renvoie la distance en cm
def mesure_distance():
    pin1.write_digital(0)
    sleep_ms(2)
    pin1.write_digital(1)
    sleep_ms(10)
    pin1.write_digital(0)
    pin2.read_digital()
    dt = time_pulse_us(pin2, 1)
    return dt * 0.034328 / 2
# ###

# Renvoie l'etat logique du capteur de ligne droit
def capteurD():
    return  pin14.read_digital()
# ###

# Renvoie l'etat logique du capteur de ligne gauche
def capteurG():
    return pin13.read_digital()
# ###

# Allume la led rouge indiquee
# Parametre : D ou G
def allume_led(coT):
    if coT == 'D':
        pin12.write_digital(1)
    elif coT == 'G':
        pin8.write_digital(1)
# ###

# Eteint la led rouge indiquee
# Parametre : D ou G
def eteint_led(coT):
    if coT == 'D':
        pin12.write_digital(0)
    elif coT == 'G':
        pin8.write_digital(0)
# ###

# Fait tourner le moteur droit
# Parametre : vitesse (-255 <-> 255)
# Sens Avant si vitesse > 0, Arriere si vitesse < 0
def moteurD(vitesse):
    v= max(-255, min(vitesse,255))
    if v >= 0:
        i2c.write(0x10, bytearray([0x02, 0x0, v]))
    else:
        i2c.write(0x10, bytearray([0x02, 0x1, -v]))
# ###

# Fait tourner le moteur gauche
# Parametre : vitesse (-255 <-> 255)
# Sens Avant si vitesse > 0, Arriere si vitesse < 0
def moteurG(vitesse):
    v= max(-255, min(vitesse,255))
    if v >= 0:
        i2c.write(0x10, bytearray([0x00, 0x0, v]))
    else:
        i2c.write(0x10, bytearray([0x00, 0x1, -v]))
# ###

# Positionne le servomoteur S1
# Parametre : position (0 <-> 180)
def servo1(angle):
    ang = max(0, min(angle,180))
    i2c.write(0x10, bytearray([0x14, ang]))
# ###

# Positionne le servomoteur S2
# Parametre : position (0 <-> 180)
def servo2(angle):
    ang = max(0, min(angle,180))
    i2c.write(0x10, bytearray([0x15, ang]))
# ###

# Allume une led RGB
# Parametre :
#   num = numero de la led (0 <-> 4)
#   si num = 4 on allume les 4 leds RGB
#   couleur au format Rouge Vert Bleu
def ledRGB(num, R, V, B):
    laquelle = max(0, min(num,4))
    rouge = max(0, min(R,255))
    vert = max(0, min(V,255))
    bleu = max(0, min(B,255))
    if laquelle < 4:
        LRGB[laquelle] = (rouge, vert, bleu)
    else:
        for i in range(4):
           LRGB[i] = (rouge, vert, bleu)
    LRGB.show()
# ###

# Eteint une led RGB
# Parametre :
#   num = numero de la led (0 <-> 4)
#   si num = 4 on eteint les 4 leds RGB
def eteintLedRGB(num):
    laquelle = max(0, min(num,4))
    if laquelle < 4:
        LRGB[laquelle] = (0, 0, 0)
    else:
        for i in range(4):
            LRGB[i] = (0, 0, 0)
    LRGB.show()
# ###

# Joue une melodie de type sirene de police
def sirene():
    for i in range(2):
        for freq in range(880, 1760, 8):
            pitch(freq,-1,pin0,False)
            sleep(6)
        for freq in range(1760, 880, -8):
            pitch(freq, -1,pin0,False)
            sleep(6)
    stop(pin0)
# ###

# Joue un son
# Parametres :
#   frequence en hz
#   duree en millisecondes
def son(f, t):
    pitch(f,t)
# ###

# Indique si le robot est sous tension
# au cas ou la micobit est alimentee separement
def power_is_on():
    return (16 in i2c.scan())

