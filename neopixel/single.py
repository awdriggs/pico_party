# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
NeoPixel example for Pico. Turns the NeoPixels red.

REQUIRED HARDWARE:
* RGB NeoPixel LEDs connected to pin GP0.
"""
import board
import neopixel

# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 1 
pixel = board.GP15

pixels = neopixel.NeoPixel(pixel, num_pixels)
pixels.brightness = 0.2

while True:
    pixels.fill((102, 255, 153))

