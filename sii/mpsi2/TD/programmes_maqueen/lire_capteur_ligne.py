from microbit import *

# Capteurs de ligne : gauche = P13, droit = P14
left_sensor = pin13
right_sensor = pin14

while True:
    left_value = left_sensor.read_digital()
    right_value = right_sensor.read_digital()

    # Affiche les valeurs dans la console
    print("Gauche:", left_value, "  Droite:", right_value)

    # Affichage rapide sur les LEDs :
    # Pixel (0,2) = gauche, Pixel (4,2) = droite
    display.clear()
    if left_value == 0:  # Ligne détectée
        display.set_pixel(0, 2, 9)
    if right_value == 0:  # Ligne détectée
        display.set_pixel(4, 2, 9)

    sleep(500)
