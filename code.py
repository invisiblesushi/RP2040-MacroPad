import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from custom_keycodes import CustomKeycode


# Define GPIO pins for buttons
button_pins = [
    board.GP0,   # Button 0
    board.GP1,   # Button 1
    board.GP2,   # Button 2
    board.GP3,   # Button 3
    board.GP4,   # Button 4
    board.GP6,   # Button 5
    board.GP7,   # Button 6
    board.GP26,  # Button 7
    board.GP27   # Button 8
]

# Define key combinations for each button
button_key_combinations = [
    CustomKeycode.CLOSE_BRACE,                  # Button 0  }
    CustomKeycode.LESS_THAN,                    # Button 1  <
    CustomKeycode.GREATER_THAN,                 # Button 2  >
    [Keycode.LEFT_ALT, Keycode.F5],             # Button 3  Debug
    [Keycode.F11],                              # Button 4  Step into
    [Keycode.F5],                               # Button 5  Resume program
    CustomKeycode.OPEN_BRACE,                   # Button 6  {
    [Keycode.F10],                              # Button 7  Step over
    [Keycode.LEFT_ALT, CustomKeycode.ENTER]     # Button 8  Alt + Enter
]

# Button init
buttons = [digitalio.DigitalInOut(pin) for pin in button_pins]
for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP
    
button_state = {i: False for i in range(len(button_pins))}
keyboard = Keyboard(usb_hid.devices)
keyboard.release_all()

print("MacroPad initialized")

while True:
    for i, button in enumerate(buttons):
        if not button.value:
            # Pressed
            if not button_state[i]:
                for keycode in button_key_combinations[i]:
                    keyboard.press(keycode)
                print(f"Button {i} pressed")
                button_state[i] = True
        else:
            # Released
            if button_state[i]:
                for keycode in button_key_combinations[i]:
                    keyboard.release(keycode)
                print(f"Button {i} released")
                button_state[i] = False

    time.sleep(0.05)