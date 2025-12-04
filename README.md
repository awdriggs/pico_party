# Raspberry Pi Pico Party

A collection of Raspberry Pi Pico CircuitPython examples demonstrating various sensors, actuators, and networking capabilities.

## button_input
Demonstrates digital button input handling with two approaches: continuous polling of button state and event-based detection with debouncing. The button is connected to GP13 with a pull-down resistor and can detect both pressed and released states.

Interfaces with the Adafruit AS7341 11-channel spectral color sensor to read light wavelengths across the visible spectrum (415nm-680nm). The code includes both raw spectral data visualization and conversion to RGB values using weighted channel combinations.

## heater
Controls a heating element using a low-value resistor (~1 ohm) connected to GP9. ⚠️ WARNING: The resistor generates significant heat and can cause burns - handle with extreme caution and proper safety measures.

## lightSensor
Measures ambient light levels in lux using the BH1750 digital light sensor over I2C. The sensor is connected to GP16 (SDA) and GP17 (SCL) and provides readings every second with error handling.

## motor
Comprehensive motor control examples including DC motors with PWM speed control, servo positioning and sweeping, large stepper motors with microstepping, and small stepper motors with 4-phase sequencing. Also includes specialized paper loading/unloading scripts for printer-type applications.

## neopixel
Controls addressable RGB LED strips (WS2812/NeoPixel) connected to GP15. Includes basic color display and button-controlled toggle functionality with debouncing for interactive LED control.

## phototransistor
Reads the value of single phototransistor

## rgbled
Controls a common-cathode RGB LED with separate pins for red (GP2), green (GP3), and blue (GP4) channels. This is for discrete RGB LEDs with individual pins, not addressable NeoPixel strips.

## socket
Advanced WebSocket client that connects to a remote server to stream temperature data from the Pico W's onboard CPU sensor. Features automatic reconnection, non-blocking I/O, and sends JSON-formatted temperature readings (°C and °F) every 10 seconds. Includes a Makefile for deployment automation.

## wifi
Basic WiFi connectivity test for Pico W that connects to a network using credentials from `settings.toml`. Displays MAC address and IP address, then pings Google DNS (8.8.4.4) to verify connectivity and measure network latency.

## Getting Started

1. Install CircuitPython firmware on your Raspberry Pi Pico
2. Copy required Adafruit libraries to the `/lib` folder on your CIRCUITPY drive
3. For WiFi projects, create a `settings.toml` file with your WiFi credentials
4. Copy the desired `.py` file to your Pico as `code.py`

## Resources

- [CircuitPython Documentation](https://docs.circuitpython.org/)
- [Adafruit Learning Guides](https://learn.adafruit.com/)
- [Raspberry Pi Pico Datasheet](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf)
