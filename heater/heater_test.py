import board
import digitalio
import time

# Configure GP0 as output for segment E
segment_e = digitalio.DigitalInOut(board.GP0)
segment_e.direction = digitalio.Direction.OUTPUT

# Blink segment E on and off
while True:
    segment_e.value = True   # Turn segment E on
    print("Segment E: ON")
    time.sleep(1)

    segment_e.value = False  # Turn segment E off
    print("Segment E: OFF")
    time.sleep(1)

