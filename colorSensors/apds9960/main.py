from time import sleep
import board
import busio
import displayio
import fourwire
import adafruit_st7789
from adafruit_apds9960.apds9960 import APDS9960

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
sensor = APDS9960(i2c)
sensor.enable_color = True


def read_rgb():
    r, g, b, c = sensor.color_data

    # normalize by max so the brightest channel is always 255
    max_val = max(r, g, b)
    if max_val == 0:
        return 0, 0, 0

    r = int((r / max_val) * 255)
    g = int((g / max_val) * 255)
    b = int((b / max_val) * 255)

    return r, g, b


while True:
    r, g, b = read_rgb()
    color = (r << 16) | (g << 8) | b
    color_palette[0] = color
    print("RGB: ({}, {}, {})  hex: #{:06X}".format(r, g, b, color))
    sleep(0.5)
