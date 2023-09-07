import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Define GPIO pins
button_pins = [
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP6,
    board.GP7,
    board.GP26,
    board.GP27
]
# Define keycodes
keycodes = [Keycode.A, Keycode.B, Keycode.C, Keycode.D, Keycode.E, Keycode.F, Keycode.G, Keycode.H]

# Button init
buttons = [digitalio.DigitalInOut(pin) for pin in button_pins]
for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP
    
button_state = {i: False for i in range(len(button_pins))}
keyboard = Keyboard(usb_hid.devices)

print("MacroPad initialized")

while True:
    for i, button in enumerate(buttons):
        if not button.value:
            # Pressed
            if not button_state[i]:
                #keyboard.press(keycodes[i])
                print(f"Button {button_pins[i]} pressed")
                button_state[i] = True
        else:
            # Released
            if button_state[i]:
                #keyboard.release(keycodes[i])
                print(f"Button {button_pins[i]} released")
                button_state[i] = False

    time.sleep(0.05)