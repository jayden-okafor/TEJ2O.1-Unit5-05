"""
Created by: Jayden Okafor
Created on: Mar 2026
This program measures the distance using the sonar.
"""

from microbit import *

# variables
sonar = None
distance = None

# Show Happy Face
display.show(Image.HAPPY)


# library
class HCSR04:
    # this class abstracts out the functionality of the HC-SR04 and
    #   returns distance in mm
    # Trig: pin 1
    # Echo: pin 2
    def __init__(self, tpin=pin1, epin=pin2, spin=pin13):
        self.trigger_pin = tpin
        self.echo_pin = epin
        self.sclk_pin = spin

    def distance_mm(self):
        spi.init(
            baudrate=125000,
            sclk=self.sclk_pin,
            mosi=self.trigger_pin,
            miso=self.echo_pin,
        )
        pre = 0
        post = 0
        k = -1
        length = 500
        resp = bytearray(length)
        resp[0] = 0xFF
        spi.write_readinto(resp, resp)
        # find first non zero value
        try:
            i, value = next((ind, v) for ind, v in enumerate(resp) if v)
        except StopIteration:
            i = -1
        if i > 0:
            pre = bin(value).count("1")
            # find first non full high value afterwards
            try:
                k, value = next(
                    (ind, v)
                    for ind, v in enumerate(resp[i : length - 2])
                    if resp[i + ind + 1] == 0
                )
                post = bin(value).count("1") if k else 0
                k = k + i
            except StopIteration:
                i = -1
        dist = -1 if i < 0 else round(((pre + (k - i) * 8.0 + post) * 8 * 0.172) / 2)
        return dist


# assign the class library to the sonar variable
sonar = HCSR04()

while True:
    if button_a.was_pressed():
        display.clear()

        # convert distance to cm
        distance = (str(sonar.distance_mm() / 10)) + " cm"

        # show distance to user
        display.scroll(str(distance))
        display.show(Image.HAPPY)
        sleep(500)
