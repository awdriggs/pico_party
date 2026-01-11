import board
import analogio
import time

# Phototransistor on analog pin A0
# Circuit: 3.3V → 10kΩ resistor → phototransistor collector
#          phototransistor emitter → Ground
#          A0 measures voltage between resistor and phototransistor
photo1 = analogio.AnalogIn(board.A0)
photo2 = analogio.AnalogIn(board.A1)

print("Phototransistor Reader")
print("Connect phototransistor to A0 (GP26)")
print("Press Ctrl-C to stop")
print()

while True:
    # Read raw value (0-65535, 16-bit ADC)
    light_value1 = photo1.value
    light_value2 = photo2.value


    print(f"one: {light_value1:5d}")
    print(f"two: {light_value2:5d}")
    time.sleep(0.5)
