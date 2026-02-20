import time
import math
import busio
import board
import digitalio
import adafruit_ov5640
import adafruit_st7789
import displayio
import fourwire

# --- Display setup ---
displayio.release_displays()
spi = busio.SPI(clock=board.GP18, MOSI=board.GP19)
display_bus = fourwire.FourWire(spi, command=board.GP21, chip_select=board.GP17, reset=board.GP20)
display = adafruit_st7789.ST7789(display_bus, width=240, height=135, rotation=270, colstart=53, rowstart=40)

# --- Camera setup ---
print("construct bus")
i2c = busio.I2C(board.GP5, board.GP4)
print("construct camera")
reset = digitalio.DigitalInOut(board.GP14)
cam = adafruit_ov5640.OV5640(
    i2c,
    data_pins=(
        board.GP6, board.GP7, board.GP8, board.GP9,
        board.GP10, board.GP11, board.GP12, board.GP13,
    ),
    clock=board.GP3,
    vsync=board.GP0,
    href=board.GP2,
    mclk=None,
    shutdown=None,
    reset=reset,
    size=adafruit_ov5640.OV5640_SIZE_240X240,
)
print("chip id:", cam.chip_id)

cam.colorspace = adafruit_ov5640.OV5640_COLOR_RGB
cam.flip_y = False
cam.flip_x = False
cam.test_pattern = False

# --- Bitmap setup ---
width = display.width
height = display.height

try:
    bitmap = displayio.Bitmap(cam.width, cam.height, 65535)
except MemoryError:
    print("240x240 too big, trying QCIF...")
    cam.size = adafruit_ov5640.OV5640_SIZE_QCIF
    bitmap = displayio.Bitmap(cam.width, cam.height, 65535)

print(width, height, cam.width, cam.height)

g = displayio.Group(scale=1, x=(width - cam.width) // 2, y=(height - cam.height) // 2)
tg = displayio.TileGrid(
    bitmap,
    pixel_shader=displayio.ColorConverter(input_colorspace=displayio.Colorspace.RGB565_SWAPPED),
)
g.append(tg)
display.root_group = g
display.auto_refresh = False

TWO_PI = 6.2831853


SAMPLE_STEP = 2
TARGET_MS = 5000


def compute_average_color(bmp, w, h, step):
    """Compute average color using HSV circular hue averaging."""
    sin_sum = 0.0
    cos_sum = 0.0
    s_sum = 0.0
    v_sum = 0.0
    count = 0

    for y in range(0, h, step):
        for x in range(0, w, step):
            val = bmp[x, y]
            # Decode RGB565_SWAPPED to float RGB
            swapped = ((val & 0xFF) << 8) | ((val >> 8) & 0xFF) # reverse order, so we get to RRRRRGGGGGGBBBBB, green is 6 bits
            r = ((swapped >> 11) & 0x1F) / 31.0 # get thef red values, mask any grabage, normalize
            gr = ((swapped >> 5) & 0x3F) / 63.0 # get the green values, mask out red values, normalize
            b = (swapped & 0x1F) / 31.0 # get the vlue values, mask out the left hand bits, normalize

            # RGB to HSV
            mx = max(r, gr, b) # max channel
            mn = min(r, gr, b) # min channel
            d = mx - mn # difference between the two

            # determine which part of the color wheel we are in 
            if d < 0.001:
                hue = 0.0
            elif mx == r:
                hue = ((gr - b) / d) % 6.0
            elif mx == gr:
                hue = ((b - r) / d) + 2.0
            else:
                hue = ((r - gr) / d) + 4.0
            hue /= 6.0

            # Circular hue averaging via unit vectors
            angle = hue * TWO_PI
            sin_sum += math.sin(angle)
            cos_sum += math.cos(angle)

            # saturation averaging
            s_sum += (d / mx) if mx > 0.001 else 0.0
            v_sum += mx #value averaging
            count += 1

    # Compute averages
    avg_hue = math.atan2(sin_sum / count, cos_sum / count) / TWO_PI
    avg_hue = avg_hue % 1.0
    avg_sat = s_sum / count
    avg_val = v_sum / count

    # HSV to RGB
    i = int(avg_hue * 6) % 6 # which section fo the color wheel is the average in?
    f = (avg_hue * 6) - i
    p = avg_val * (1 - avg_sat)
    q = avg_val * (1 - f * avg_sat)
    t = avg_val * (1 - (1 - f) * avg_sat)

    if i == 0:
        r, gr, b = avg_val, t, p # truple packing
    elif i == 1:
        r, gr, b = q, avg_val, p
    elif i == 2:
        r, gr, b = p, avg_val, t
    elif i == 3:
        r, gr, b = p, q, avg_val
    elif i == 4:
        r, gr, b = t, p, avg_val
    else:
        r, gr, b = avg_val, p, q

    return int(r * 255), int(gr * 255), int(b * 255)


def rgb_to_565_swapped(r, g, b):
    """Convert RGB (0-255) to RGB565_SWAPPED."""
    r5 = (r >> 3) & 0x1F
    g6 = (g >> 2) & 0x3F
    b5 = (b >> 3) & 0x1F
    rgb565 = (r5 << 11) | (g6 << 5) | b5
    return ((rgb565 & 0xFF) << 8) | ((rgb565 >> 8) & 0xFF)


# --- Main loop ---
while True:
    cam.capture(bitmap)

    t0 = time.monotonic_ns()
    r, g, b = compute_average_color(bitmap, cam.width, cam.height, SAMPLE_STEP)
    t1 = time.monotonic_ns()
    elapsed_ms = (t1 - t0) // 1_000_000
    print("avg color: R={} G={} B={} ({}ms)".format(r, g, b, elapsed_ms))

    # Fill display with solid average color
    fill_val = rgb_to_565_swapped(r, g, b)
    bitmap.fill(fill_val)
    bitmap.dirty()
    display.refresh(minimum_frames_per_second=0)

    # Pad to 5 second interval if compute was faster
    if elapsed_ms < TARGET_MS:
        time.sleep((TARGET_MS - elapsed_ms) / 1000)
