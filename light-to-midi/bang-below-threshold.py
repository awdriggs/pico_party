import board
import analogio
import time
import usb_midi
import adafruit_midi
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff

# === CONFIGURATION ===
THRESHOLD = 1000       # Trigger when light drops below this (0-65535)
MIDI_NOTE = 60          # Middle C (change to desired note)
MIDI_VELOCITY = 127     # Note velocity (0-127)
DEBOUNCE_MS = 200       # Minimum time between triggers
NOTE_DURATION_MS = 100  # How long the note stays on

# === SETUP ===
photo = analogio.AnalogIn(board.A0)
midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

# State tracking
triggered = False
last_trigger_time = 0
note_off_time = 0

print("Light-to-MIDI")
print(f"Threshold: {THRESHOLD}")
print(f"MIDI Note: {MIDI_NOTE}")
print(f"Debounce: {DEBOUNCE_MS}ms")
print()

while True:
    now = time.monotonic_ns() // 1_000_000  # Current time in ms
    light_value = photo.value

    # Check if we need to send note off
    if note_off_time > 0 and now >= note_off_time:
        midi.send(NoteOff(MIDI_NOTE, 0))
        note_off_time = 0
        print("  note off")

    # Check for trigger condition
    below_threshold = light_value < THRESHOLD
    time_since_trigger = now - last_trigger_time

    if below_threshold and not triggered and time_since_trigger >= DEBOUNCE_MS:
        # Trigger!
        midi.send(NoteOn(MIDI_NOTE, MIDI_VELOCITY))
        note_off_time = now + NOTE_DURATION_MS
        last_trigger_time = now
        triggered = True
        print(f"TRIGGER! Light: {light_value}")

    # Reset triggered state when light returns above threshold
    if not below_threshold:
        triggered = False

    time.sleep(0.01)  # 10ms loop for responsive detection
