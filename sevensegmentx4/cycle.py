import board
import digitalio
import time

# Define the GPIO pins for each segment (A-G)
segment_pins = [board.GP5, board.GP4, board.GP27, board.GP15, board.GP14, board.GP7, board.GP8]

# Configure all segments as outputs using a loop
segments = []
for pin in segment_pins:
    segment = digitalio.DigitalInOut(pin)
    segment.direction = digitalio.Direction.OUTPUT
    segments.append(segment)

# Initialize all segments OFF (HIGH for common anode)
for segment in segments:
    segment.value = True

# Display delay in seconds
DISPLAY_DELAY = 0.5 

# Combinations that look like numbers 0-9 (do not display these)
# Bit mapping: 0=A, 1=B, 2=C, 3=D, 4=E, 5=F, 6=G
DO_NOT_DISPLAY = [
    63,   # 0: A,B,C,D,E,F
    6,    # 1: B,C
    91,   # 2: A,B,D,E,G
    79,   # 3: A,B,C,D,G
    102,  # 4: B,C,F,G
    109,  # 5: A,C,D,F,G
    125,  # 6: A,C,D,E,F,G
    7,    # 7: A,B,C
    127,  # 8: A,B,C,D,E,F,G
    111,  # 9: A,B,C,D,F,G
    39,   # looks like 7
    103
]

# Cycle through all 128 possible combinations (2^7 = 128)
while True:
    for combination in range(128):
        # Skip combinations that look like numbers
        if combination in DO_NOT_DISPLAY:
            continue

        # Set each segment based on the binary representation of the combination
        for bit_position in range(7):
            # Check if this bit is set in the combination
            bit_value = (combination >> bit_position) & 1
            # For common anode: bit_value=1 means ON, so set to False (LOW)
            # bit_value=0 means OFF, so set to True (HIGH)
            segments[bit_position].value = not bool(bit_value)

        # Print the current combination info
        active_segments = []
        segment_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        for i in range(7):
            if (combination >> i) & 1:
                active_segments.append(segment_names[i])

        print(f"Combination {combination:3d} (0b{combination:07b}): {','.join(active_segments) if active_segments else 'none'}")

        time.sleep(DISPLAY_DELAY)
