from microbit import *

while True:
    #  Lire des données de l'accelerometer
    acc = accelerometer.get_values()
    #  Affichage des donnees
    print(acc)
    sleep(50)  # Pause entre chaque mesure
