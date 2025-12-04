
"""
Button example for Pico. Check the state.

REQUIRED HARDWARE:
* Button switch on pin GP13.
"""
import time
import board
import digitalio

button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull=digitalio.Pull.DOWN)

previous_state = False  # Track the previous button state

while True:
    current_state = button.value  # Read current button state

    if current_state and not previous_state:
        print("Pressed")  # Button just pressed
    elif not current_state and previous_state:
        print("Released")  # Button just released

    previous_state = current_state  # Update the previous state
    time.sleep(0.05)  # Small delay to debounce the button
