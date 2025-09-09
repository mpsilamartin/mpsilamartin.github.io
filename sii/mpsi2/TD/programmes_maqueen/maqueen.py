# The MIT License (MIT)
# Copyright (c) 2016 British Broadcasting Corporation.
# This software is provided by Lancaster University by arrangement with the BBC.
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

# Olivier Lecluse
# Avril 2019

import microbit
import time
import machine
import music

class Maqueen():
    def __init__(self,addr=0x10):
        """Initiaisation robot
        addr : adresse i2c. 0x10 par defaut"""
        self.addr=addr
        self._vitesse=0 # vitesse entre 0 et 100

    def getVitesse(self):
        return self._vitesse

    def setVitesse(self, v):
        self._vitesse=v

    def moteurDroit(self, v=None):
        if v==None:
            v=self._vitesse
        sens=0 if v>=0 else 1 # sens moteur
        vit=abs(v)*255//100   # vitesse moteur 0..255
        microbit.i2c.write(self.addr,bytearray([2,sens, vit]))

    def moteurGauche(self, v=None):
        if v==None:
            v=self._vitesse
        sens=0 if v>=0 else 1 # sens moteur
        vit=abs(v)*255//100   # vitesse moteur 0..255
        microbit.i2c.write(self.addr,bytearray([0,sens, vit]))

    def avance(self,v=None):
        if v != None:
            self._vitesse=v
        self.moteurDroit()
        self.moteurGauche()

    def recule(self):
        self.moteurDroit(-self._vitesse)
        self.moteurGauche(-self._vitesse)

    def stop(self):
        microbit.i2c.write(self.addr,bytearray([0,0,0]))
        microbit.sleep(1)
        microbit.i2c.write(self.addr,bytearray([2,0,0]))

    def distance(self):
        """Calcule la distance à l'obstacle en cm
        pin1 : Trig
        pin2 : Echo"""
        microbit.pin1.write_digital(1)
        time.sleep_ms(10)
        microbit.pin1.write_digital(0)

        microbit.pin2.read_digital()
        t2 = machine.time_pulse_us(microbit.pin2, 1)

        d = 340 * t2 / 20000
        return d

    def son_r2d2(self):
        tune=["A7:0", "G7:0", "E7:0","C7:0","D7:0","B7:0","F7:0","C8:0","A7:0","G7:0","E7:0","C7:0","D7:0","B7:0","F7:0","C8:0"]
        music.play(tune)

    def son_bip(self):
        for i in range(2):
            freq=2000
            while freq>1000:
                music.pitch(int(freq),10)
                freq*=0.95
            freq=1000
            while freq<3000:
                music.pitch(int(freq),10)
                freq*=1.05
