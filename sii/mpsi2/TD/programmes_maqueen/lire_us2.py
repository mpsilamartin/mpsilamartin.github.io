from microbit import *
import utime
import machine


def distance():
    """Calcule la distance à l'obstacle en m
    pin1 : Trig
    pin2 : Echo"""
    pin1.write_digital(0)
    utime.sleep_us(2)
    pin1.write_digital(1)
    utime.sleep_us(10)
    pin1.write_digital(0)
    pin2.read_digital()
    t2 = machine.time_pulse_us(pin2, 1)  # t_echo in microseconds
    return 340 * t2 / 2 / 1000000  # sound speed, round-trip/2, get in cm

while True:
    d = distance()
    if d:
        print("Distance:", (int(d),), "cm")
    else:
        print((int(0),))
    sleep(500)
