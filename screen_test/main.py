import board
import busio
import displayio
import fourwire
import adafruit_st7789

displayio.release_displays()
spi = busio.SPI(clock=board.GP10, MOSI=board.GP11)
display_bus = fourwire.FourWire(spi, command=board.GP21, chip_select=board.GP17, reset=board.GP20)
display = adafruit_st7789.ST7789(display_bus, width=240, height=320, rotation=0)

splash = displayio.Group()
color_bitmap = displayio.Bitmap(240, 320, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FFFF  # Red

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)
display.root_group = splash

while True:
    pass
