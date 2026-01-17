import board
import analogio
import time
import usb_midi
import adafruit_midi
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff

# === CONFIGURATION ===
LOW_THRESHOLD = 1000    # Trigger when light drops below this
HIGH_THRESHOLD = 3000   # Reset when light goes above this
MIDI_NOTE = 60          # Middle C (change to desired note)
MIDI_VELOCITY = 127     # Note velocity (0-127)
NOTE_DURATION_MS = 100  # How long the note stays on

# === SETUP ===
photo = analogio.AnalogIn(board.A0)
midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

# State tracking
armed = True  # Ready to trigger
note_off_time = 0

print("Light-to-MIDI")
print(f"Low threshold: {LOW_THRESHOLD} (trigger)")
print(f"High threshold: {HIGH_THRESHOLD} (reset)")
print(f"MIDI Note: {MIDI_NOTE}")
print()

while True:
    now = time.monotonic_ns() // 1_000_000  # Current time in ms
    light_value = photo.value

    # Check if we need to send note off
    if note_off_time > 0 and now >= note_off_time:
        midi.send(NoteOff(MIDI_NOTE, 0))
        note_off_time = 0
        print("  note off")

    # Trigger when armed and light drops below low threshold
    if armed and light_value < LOW_THRESHOLD:
        midi.send(NoteOn(MIDI_NOTE, MIDI_VELOCITY))
        note_off_time = now + NOTE_DURATION_MS
        armed = False
        print(f"TRIGGER! Light: {light_value}")

    # Re-arm when light goes above high threshold
    if not armed and light_value > HIGH_THRESHOLD:
        armed = True
        print(f"ARMED. Light: {light_value}")

    time.sleep(0.01)  # 10ms loop for responsive detection
