# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Button example for Pico. Prints button pressed state to serial console.

REQUIRED HARDWARE:
* Button switch on pin GP12 (one side to GP12, other side to GND).
"""
import board
import digitalio
from adafruit_debouncer import Debouncer

pin = digitalio.DigitalInOut(board.GP12)
pin.switch_to_input(pull=digitalio.Pull.UP)
button = Debouncer(pin)

while True:
    button.update()

    if button.fell:  # Button was just pressed (went from HIGH to LOW)
        print("Button pressed!")
    if button.rose:  # Button was just released
        print("Button released!")
