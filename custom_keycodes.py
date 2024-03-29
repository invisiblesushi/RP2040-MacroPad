from adafruit_hid.keycode import Keycode

# Custom keycodes for nordic keyboard layout.
class CustomKeycode:
    A = 0x04
    B = 0x05
    C = 0x06
    D = 0x07
    E = 0x08
    F = 0x09
    G = 0x0a
    H = 0x0b
    I = 0x0c
    J = 0x0d
    K = 0x0e
    L = 0x0f
    M = 0x10
    N = 0x11
    O = 0x12
    P = 0x13
    Q = 0x14
    R = 0x15
    S = 0x16
    T = 0x17
    U = 0x18
    V = 0x19
    W = 0x1a
    X = 0x1b
    Y = 0x1c
    Z = 0x1d
    Æ = 0x34
    Ø = 0x33
    F1 = 0x3a
    F2 = 0x3b
    F3 = 0x3c
    F4 = 0x3d
    F5 = 0x3e
    F6 = 0x3f
    F7 = 0x40
    F8 = 0x41
    F9 = 0x42
    F10 = 0x43
    F11 = 0x44
    F12 = 0x45
    ONE = 0x1e
    TWO = 0x1f
    THREE = 0x20
    FOUR = 0x21
    FIVE = 0x22
    SIX = 0x23
    SEVEN = 0x24
    EIGHT = 0x25
    NINE = 0x26
    ZERO = 0x27
    TAB = 0x2b
    COMMA = 0x36
    PERIOD = 0x37
    ENTER = 0x28
    MINUS = 0x38
    OPEN_BRACE = [Keycode.RIGHT_ALT, 0x24]
    CLOSE_BRACE = [Keycode.RIGHT_ALT, 0x27]
    LESS_THAN = [0x64]
    GREATER_THAN = [Keycode.SHIFT, 0x64]
    EXCLAMATION_MARK = [Keycode.SHIFT, 0x1e]
    DOUBLE_QUOTATION_MARK = [Keycode.SHIFT, 0x1f]
    HASH = [Keycode.SHIFT, 0x20]
    PERCENT = [Keycode.SHIFT, 0x22]
    AMPERSAND = [Keycode.SHIFT, 0x23]
    FORWARD_SLASH = [Keycode.SHIFT, 0x24]
    OPEN_PARENTHESIS = [Keycode.SHIFT, 0x25]
    CLOSE_PARENTHESIS = [Keycode.SHIFT, 0x26]
    EQUAL = [Keycode.SHIFT, 0x27]
    AT_SYMBOL = [Keycode.RIGHT_ALT, 0x1f]
    POUND = [Keycode.RIGHT_ALT, 0x20]
    DOLLAR = [Keycode.RIGHT_ALT, 0x21]
