# Makefile for CircuitPython Development with Raspberry Pi Pico RP2040

# Configuration
DEVICE_PATH = /Volumes/CIRCUITPY
SERIAL_PORT = /dev/tty.usbmodem1101
BAUD_RATE = 115200
SOURCE_FILE = main.py

# Targets
.PHONY: help upload monitor clean reset watch

help:
	@echo "CircuitPython Makefile Commands:"
	@echo "  make upload    - Copy $(SOURCE_FILE) to $(DEVICE_PATH)/code.py"
	@echo "  make monitor   - Monitor serial output (Ctrl-A then K to exit)"
	@echo "  make run       - Upload and then monitor"
	@echo "  make watch     - Auto-upload on file changes (requires watchexec)"
	@echo "  make clean     - Remove code.py from device"
	@echo "  make reset     - Touch code.py to trigger reload"
	@echo "  make check     - Check if device is mounted"

check:
	@if [ ! -d "$(DEVICE_PATH)" ]; then \
		echo "Error: Device not found at $(DEVICE_PATH)"; \
		echo "Available volumes:"; \
		ls -1 /Volumes; \
		exit 1; \
	fi
	@echo "Device found at $(DEVICE_PATH)"

upload: check
	@if [ ! -f "$(SOURCE_FILE)" ]; then \
		echo "Error: Source file $(SOURCE_FILE) not found"; \
		echo "Available Python files:"; \
		find . -name "*.py" -type f; \
		exit 1; \
	fi
	@echo "Copying $(SOURCE_FILE) to $(DEVICE_PATH)/code.py..."
	@cp $(SOURCE_FILE) $(DEVICE_PATH)/code.py
	@echo "Upload complete!"
	@sleep 1
	@echo "CircuitPython will auto-reload..."

monitor:
	@echo "Connecting to $(SERIAL_PORT) at $(BAUD_RATE) baud..."
	@echo "Press Ctrl-A then K to exit, or Ctrl-A then D to detach"
	@screen $(SERIAL_PORT) $(BAUD_RATE)

run: upload
	@sleep 2
	@$(MAKE) monitor

clean: check
	@echo "Removing code.py from device..."
	@rm -f $(DEVICE_PATH)/code.py
	@echo "Cleaned!"

reset: check
	@echo "Triggering device reload..."
	@touch $(DEVICE_PATH)/code.py
	@echo "Device should reload now"

# List CircuitPython files on device
ls: check
	@echo "Files on device:"
	@ls -lh $(DEVICE_PATH)

# Watch for changes and auto-upload
watch:
	@echo "Watching $(SOURCE_FILE) for changes..."
	@echo "Press Ctrl-C to stop"
	@watchexec -w $(SOURCE_FILE) make upload
