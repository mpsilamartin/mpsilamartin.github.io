from microbit import *

# import neopixel
# from lib_maqueen import *

while True:
    # dist=mesure_distance()
    acc = accelerometer.get_values()
    print(acc)
    sleep(50)
