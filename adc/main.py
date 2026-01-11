import board
import busio
import digitalio
import time
from adafruit_mcp3xxx.mcp3008 import MCP3008
from adafruit_mcp3xxx.analog_in import AnalogIn

# MCP3008 SPI Setup
# Wiring:
#   MCP3008 CLK  -> GP18 (SPI0 SCK)
#   MCP3008 DOUT -> GP16 (SPI0 MISO)
#   MCP3008 DIN  -> GP19 (SPI0 MOSI)
#   MCP3008 CS   -> GP17
#   MCP3008 VDD  -> 3.3V
#   MCP3008 VREF -> 3.3V
#   MCP3008 AGND -> GND
#   MCP3008 DGND -> GND

# Create SPI bus
spi0 = busio.SPI(clock=board.GP2, MISO=board.GP0, MOSI=board.GP3)
spi1 = busio.SPI(clock=board.GP14, MISO=board.GP12, MOSI=board.GP15)

# Create chip select
cs0 = digitalio.DigitalInOut(board.GP1)
cs1 = digitalio.DigitalInOut(board.GP13)

# Create MCP3008 object
mcp0 = MCP3008(spi0, cs0)
mcp1 = MCP3008(spi1, cs1)

# Create analog inputs for all 8 channels
channels0 = [AnalogIn(mcp0, i) for i in range(8)]
channels1 = [AnalogIn(mcp1, i) for i in range(8)]

print("MCP3008 Phototransistor Test")
print("Reading all 8 channels")
print("16-bit resolution (0-65535)")
print("Press Ctrl-C to stop")
print()

while True:
    print("-" * 80)
    print("spi0")
    for i, chan in enumerate(channels0):
        # Read raw value (0-65535, 16-bit)
        raw_value = chan.value

        print(f"CH{i} - Raw: {raw_value:5d}")

    print("spi1")
    for i, chan in enumerate(channels1):
        # Read raw value (0-65535, 16-bit)
        raw_value = chan.value

        print(f"CH{i} - Raw: {raw_value:5d}")

    time.sleep(5)
