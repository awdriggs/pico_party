import board
import busio
from adafruit_ht16k33.segments import Seg7x4

i2c = busio.I2C(board.GP5, board.GP4)
display = Seg7x4(i2c)

display.brightness = 1.0

# display.blink_rate = 3

# display.print(1234)

display.set_digit_raw(1, 0b1111111)
