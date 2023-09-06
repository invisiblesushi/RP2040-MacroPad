import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Create a list of keycodes (empty in this example)
key_layout = []

# Create a keyboard object
keyboard = Keyboard(usb_hid.devices)
# Define the LED pinaaaaaaa
led_pin = board.LED

button_pin = board.GP5
button = digitalio.DigitalInOut(button_pin)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

print("Hello world")

while True:
    if not button.value:
        print("Button pressed!")
        keyboard.press(Keycode.A)
        keyboard.release_all()
    
    # Add a small delay to avoid rapid button presses
    time.sleep(0.1)