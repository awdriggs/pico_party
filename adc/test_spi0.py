import board
import busio
import digitalio
import time
from adafruit_mcp3xxx.mcp3008 import MCP3008
from adafruit_mcp3xxx.analog_in import AnalogIn

print("Testing SPI0 ONLY")
print("-" * 40)

try:
    # Create ONLY SPI0 bus
    spi0 = busio.SPI(clock=board.GP18, MISO=board.GP16, MOSI=board.GP19)
    print("✓ SPI0 bus created successfully")

    # Create chip select
    cs0 = digitalio.DigitalInOut(board.GP17)
    print("✓ CS0 pin configured")

    # Create MCP3008 object
    mcp0 = MCP3008(spi0, cs0)
    print("✓ MCP3008 initialized")

    # Create analog input for channel 0
    chan0 = AnalogIn(mcp0, 0)
    print("✓ Channel 0 created")
    print()

    # Try to read
    print("Attempting to read channel 0...")
    for i in range(5):
        value = chan0.value
        voltage = chan0.voltage
        print(f"  Read {i+1}: Raw={value:5d}, Voltage={voltage:.3f}V")
        time.sleep(0.5)

except Exception as e:
    print(f"✗ ERROR: {e}")
    import traceback
    traceback.print_exc()
