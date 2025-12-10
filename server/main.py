import wifi
import socketpool
import os
import board
import digitalio
import time

def load_html():
    """Load HTML content from file"""
    try:
        with open('index.html', 'r') as f:
            return f.read()
    except:
        return "<html><body><h1>Pico Party Server</h1><p>Error loading page</p></body></html>"

def start_server():
    """Start the web server"""
    # Wi-Fi credentials are read from settings.toml automatically
    ssid = os.getenv('CIRCUITPY_WIFI_SSID')
    password = os.getenv('CIRCUITPY_WIFI_PASSWORD')

    if not ssid or not password:
        print("ERROR: Wi-Fi credentials not found in settings.toml")
        return

    print("Connecting to Wi-Fi...")
    print(f"SSID: {ssid}")

    try:
        wifi.radio.connect(ssid, password, timeout=10)
    except Exception as e:
        print(f"Wi-Fi connection failed: {e}")
        print("Check your settings.toml credentials")
        return

    print("Connected!")
    print(f"IP Address: {wifi.radio.ipv4_address}")

    # Load HTML
    html = load_html()

    # Create socket pool and server
    try:
        pool = socketpool.SocketPool(wifi.radio)
        server_socket = pool.socket(pool.AF_INET, pool.SOCK_STREAM)
        server_socket.setsockopt(pool.SOL_SOCKET, pool.SO_REUSEADDR, 1)
        server_socket.bind(('0.0.0.0', 80))
        server_socket.listen(5)
        print("Socket created and listening")
    except Exception as e:
        print(f"Failed to create server socket: {e}")
        return

    print(f"\nServer running at http://{wifi.radio.ipv4_address}")
    print("Waiting for connections...\n")

    # Setup LED
    try:
        led = digitalio.DigitalInOut(board.LED)
        led.direction = digitalio.Direction.OUTPUT
        has_led = True
    except:
        has_led = False
        print("No LED available")

    last_blink = time.monotonic()
    led_state = False

    while True:
        client = None
        try:
            # Blink LED every 2 seconds if Wi-Fi is connected
            if has_led and wifi.radio.connected:
                now = time.monotonic()
                if now - last_blink > 2:
                    led_state = not led_state
                    led.value = led_state
                    last_blink = now

            server_socket.settimeout(0.5)  # Short timeout so LED can blink
            client, addr = server_socket.accept()
            server_socket.settimeout(None)  # Reset timeout after accepting
            print(f"Client connected: {addr}")

            # Read request using recv_into
            buffer = bytearray(1024)
            num_bytes = client.recv_into(buffer)
            if num_bytes:
                request_str = buffer[:num_bytes].decode('utf-8')
                print(f"Request: {request_str.split()[0:2] if request_str else 'empty'}")

            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type: text/html\r\n"
            response += "Connection: close\r\n\r\n"
            response += html

            client.send(response.encode('utf-8'))
            print("Response sent")
            client.close()
            print("Connection closed\n")

        except OSError as e:
            # Timeout is expected, just continue to blink LED
            if e.errno == 116:  # ETIMEDOUT
                pass
            else:
                print(f"Socket error: {e}")
        except Exception as e:
            print(f"Error handling request: {e}")
            import traceback
            traceback.print_exception(e)
        finally:
            if client:
                try:
                    client.close()
                except:
                    pass

# Start server
print("Pico Party Web Server")
print("=" * 30)
start_server()
