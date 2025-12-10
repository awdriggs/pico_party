import board
import digitalio
import time

# Define the GPIO pins for each segment (A-G plus DP for decimal point)
segment_pins = [board.GP0, board.GP1, board.GP2, board.GP3,
                board.GP4, board.GP5, board.GP6, board.GP7]

# Configure all segments as outputs using a loop
segments = []
for pin in segment_pins:
    segment = digitalio.DigitalInOut(pin)
    segment.direction = digitalio.Direction.OUTPUT
    segments.append(segment)

# Flash all segments on and off together
while True:
    # Turn all segments ON
    for segment in segments:
        segment.value = True
    print("All segments: ON")
    time.sleep(1)

    # Turn all segments OFF
    for segment in segments:
        segment.value = False
    print("All segments: OFF")
    time.sleep(1)

