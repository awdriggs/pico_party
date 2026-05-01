from time import sleep
import board
import busio
import displayio
import fourwire
import adafruit_st7789
from adafruit_opt4048 import OPT4048, Mode

# --- Display setup (SPI) ---
displayio.release_displays()
spi = busio.SPI(clock=board.GP18, MOSI=board.GP19)
display_bus = fourwire.FourWire(spi, command=board.GP21, chip_select=board.GP17, reset=board.GP20)
display = adafruit_st7789.ST7789(display_bus, width=240, height=320, rotation=0)

splash = displayio.Group()
color_bitmap = displayio.Bitmap(240, 320, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x000000
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)
display.root_group = splash

# --- Color sensor setup (I2C) ---
i2c = busio.I2C(scl=board.GP15, sda=board.GP14)
sensor = OPT4048(i2c)
sensor.mode = Mode.CONTINUOUS


while True:
    try:
        r, g, b, lux = sensor.rgb
        color = (r << 16) | (g << 8) | b
        color_palette[0] = color
        print("RGB: ({}, {}, {})  lux: {:.1f}  hex: #{:06X}".format(r, g, b, lux, color))
    except RuntimeError:
        pass
    sleep(0.5)
