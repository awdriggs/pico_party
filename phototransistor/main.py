import board
import analogio
import time

# Phototransistor on analog pin A0
# Circuit: 3.3V → 10kΩ resistor → phototransistor collector
#          phototransistor emitter → Ground
#          A0 measures voltage between resistor and phototransistor
photo = analogio.AnalogIn(board.A0)

print("Phototransistor Reader")
print("Connect phototransistor to A0 (GP26)")
print("Press Ctrl-C to stop")
print()

while True:
    # Read raw value (0-65535, 16-bit ADC)
    light_value = photo.value

    # Convert to voltage (0-3.3V)
    voltage = (light_value / 65535) * 3.3

    # Calculate percentage (brighter = higher value)
    percentage = (light_value / 65535) * 100

    print(f"Raw: {light_value:5d} | Voltage: {voltage:.3f}V | Light: {percentage:.1f}%")
    time.sleep(0.1)
