from gpiozero import LED
from time import sleep

light = LED(17)  # Change to your GPIO pin

while True:
    light.on()
    print("ON")
    sleep(3)
    light.off()
    print("OFF")
    sleep(3)
