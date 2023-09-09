from adafruit_hid.keycode import Keycode

# Custom keycodes for nordic keyboard layout.
class CustomKeycode:
    OPEN_BRACE = [Keycode.RIGHT_ALT, 36]    # Right Alt + 36
    CLOSE_BRACE = [Keycode.RIGHT_ALT, 39]   # Right Alt + 39
    LESS_THAN = [100]                        # 100
    GREATER_THAN = [Keycode.SHIFT, 100]     # Shift + 100
    EXCLAMATION_MARK = [Keycode.SHIFT, 30] # Shift + 30