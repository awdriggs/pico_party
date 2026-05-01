from time import sleep
import board
import busio
import displayio
import fourwire
import adafruit_st7789
from adafruit_as7341 import AS7341

# --- Display setup (SPI) ---
displayio.release_displays()
spi = busio.SPI(clock=board.GP2, MOSI=board.GP3)
display_bus = fourwire.FourWire(spi, command=board.GP5, chip_select=board.GP1, reset=board.GP20)
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
sensor = AS7341(i2c)


def get_channels():
    return {
        "F1": sensor.channel_415nm,
        "F2": sensor.channel_445nm,
        "F3": sensor.channel_480nm,
        "F4": sensor.channel_515nm,
        "F5": sensor.channel_555nm,
        "F6": sensor.channel_590nm,
        "F7": sensor.channel_630nm,
        "F8": sensor.channel_680nm,
    }


def normalize(channels):
    max_val = max(channels.values())
    return {key: value / max_val for key, value in channels.items()}


def read_rgb():
    channels = get_channels()
    normalized = normalize(channels)

    r = 0.3 * normalized["F6"] + 0.5 * normalized["F7"] + 0.7 * normalized["F8"]
    g = 0.3 * normalized["F4"] + 0.7 * normalized["F5"]
    b = 0.5 * normalized["F2"] + 0.5 * normalized["F3"]

    max_rgb = max(r, g, b)
    if max_rgb > 1.0:
        r /= max_rgb
        g /= max_rgb
        b /= max_rgb

    return int(r * 255), int(g * 255), int(b * 255)


while True:
    r, g, b = read_rgb()
    color = (r << 16) | (g << 8) | b
    color_palette[0] = color
    print("RGB: ({}, {}, {})  hex: #{:06X}".format(r, g, b, color))
    sleep(0.5)
