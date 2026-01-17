import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP6)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    print("ON")
    time.sleep(3)
    led.value = False
    print("OFF")
    time.sleep(3)
