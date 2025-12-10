from os import getenv
import ipaddress
import wifi
import socketpool
import time
import microcontroller
import json
import cpwebsockets.client

# Get WiFi details, ensure these are setup in settings.toml
ssid = getenv("CIRCUITPY_WIFI_SSID")
password = getenv("CIRCUITPY_WIFI_PASSWORD")

if None in [ssid, password]:
    raise RuntimeError(
        "WiFi settings are kept in settings.toml, "
        "please add them there. The settings file must contain "
        "'CIRCUITPY_WIFI_SSID', 'CIRCUITPY_WIFI_PASSWORD', "
        "at a minimum."
    )

print()
print("Connecting to WiFi")

#  connect to your SSID
try:
    wifi.radio.connect(ssid, password)
except TypeError:
    print("Could not find WiFi info. Check your settings.toml file!")
    raise

print("Connected to WiFi")

pool = socketpool.SocketPool(wifi.radio)

#  prints MAC address to REPL
print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])

#  prints IP address to REPL
print(f"My IP address is {wifi.radio.ipv4_address}")

#  pings Google
# ipv4 = ipaddress.ip_address("8.8.4.4")
# print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4)*1000))

# Function to read onboard temperature sensor
def get_temperature():
    return microcontroller.cpu.temperature

# WebSocket setup
WS_URL = "wss://micro-api.awdokku.site/"
STREAM_NAME = "pico-temp"

print("\nConnecting to WebSocket server...")
ws = cpwebsockets.client.connect(WS_URL, wifi.radio)
ws.settimeout(0.1)  # Make recv() non-blocking with 0.1 second timeout

# Join the temperature stream
join_msg = {"type": "join", "stream": STREAM_NAME}
ws.send(json.dumps(join_msg))
print(f"Joined stream: {STREAM_NAME}")

# Main loop - send temperature every 10 seconds
print("\nStarting temperature monitoring...")
last_send = time.monotonic()
SEND_INTERVAL = 10  # seconds

while True:
    try:
        # Check for incoming messages (ping/pong handling)
        # This allows the library to respond to server pings
        try:
            msg = ws.recv()  # Non-blocking due to settimeout(0.1)
            if msg:
                print(f"Received: {msg}")
        except:
            pass  # No message available or timeout, that's OK

        # Send temperature at regular intervals
        if time.monotonic() - last_send >= SEND_INTERVAL:
            temp_c = get_temperature()
            temp_f = (temp_c * 9/5) + 32

            # Send temperature data
            data_msg = {
                "type": "data",
                "temperature_c": temp_c,
                "temperature_f": temp_f
            }
            ws.send(json.dumps(data_msg))

            print(f"Sent: {temp_c:.2f}°C / {temp_f:.2f}°F")
            last_send = time.monotonic()

        time.sleep(0.1)  # Small delay to prevent busy-waiting

    except OSError as e:
        if e.errno == 32:  # Broken pipe
            print(f"Connection lost (Error {e.errno})")
        else:
            print(f"Error: {e}")
        print("Reconnecting...")
        time.sleep(5)
        try:
            ws.close()
        except:
            pass
        ws = cpwebsockets.client.connect(WS_URL, wifi.radio)
        ws.settimeout(0.1)  # Make recv() non-blocking
        ws.send(json.dumps(join_msg))

