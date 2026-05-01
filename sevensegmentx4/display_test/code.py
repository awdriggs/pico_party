import board
import digitalio
import time

# Define the GPIO pins for each segment (A-G plus DP for decimal point)
segment_pins = [board.GP5, board.GP4, board.GP27, board.GP15, board.GP14, board.GP7, board.GP8, board.GP28]

# Configure all segments as outputs using a loop
segments = []
for pin in segment_pins:
    segment = digitalio.DigitalInOut(pin)
    segment.direction = digitalio.Direction.OUTPUT
    segments.append(segment)

# Initialize all segments OFF (HIGH for common anode)
for segment in segments:
    segment.value = True

# Cycle through each segment pin
while True:
    for i, segment in enumerate(segments):
        # Turn current segment ON (LOW for common anode)
        segment.value = False
        print(f"Segment {i}: ON")
        time.sleep(0.5)

        # Turn current segment OFF (HIGH for common anode)
        segment.value = True

