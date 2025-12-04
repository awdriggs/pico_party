# Small test to push power through a small resistor, like 1ohm to get it to heat up. DANGER! This will burn you.
import time
import board
import digitalio

heater = digitalio.DigitalInOut(board.GP9)  # pin for resistor 
heater.direction = digitalio.Direction.OUTPUT  # output of corse

while True:  # infinite loop here
    heater.value = True  # push power to the resistor
    print("heating");
    time.sleep(0.25)

