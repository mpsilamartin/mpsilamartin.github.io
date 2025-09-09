from microbit import *
import utime

def distance():
    #  Programme de lecture du capteur ultra son
    # Envoi impulsion TRIG sur P1
    pin1.write_digital(0)
    utime.sleep_us(2)
    pin1.write_digital(1)
    utime.sleep_us(10)
    pin1.write_digital(0)

    # Attente du front montant sur ECHO (P2)
    timeout = utime.ticks_add(utime.ticks_us(), 30000)  # 30 ms timeout
    while pin2.read_digital() == 0:
        if utime.ticks_diff(timeout, utime.ticks_us()) <= 0:
            return None
    start = utime.ticks_us()

    # Attente du front descendant
    timeout = utime.ticks_add(utime.ticks_us(), 30000)
    while pin2.read_digital() == 1:
        if utime.ticks_diff(timeout, utime.ticks_us()) <= 0:
            return None
    end = utime.ticks_us()

    # Durée de l’écho
    duration = utime.ticks_diff(end, start)

    # Conversion en cm
    dist_cm = (duration / 2) / 29.1
    return dist_cm

while True:
    d = distance()
    if d:
        #  affichage des mesures de disance en cm
        print((int(d),))
    else:
        #  on affiche 0 si pas d'echo
        print((0,))
    sleep(50)
