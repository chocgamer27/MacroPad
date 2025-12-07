import board
import supervisor

# KMK imports
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap
from kmk.modules.rgb import RGB

keyboard = KMKKeyboard()

# --------------------------
#  RGB LEDs (SK6812 MINI-E)
# --------------------------

rgb = RGB(
    pixel_pin=board.D0,      # your LED DIN pin
    num_pixels=2,            # 2 strips × 2 LEDs each
    hue_default=0,           # red
    sat_default=255,
    val_default=40,          # brightness
    animation_mode=1,        # breathing
)

keyboard.modules.append(rgb)

# --------------------------
#  MACRO ENGINE
# --------------------------

macros = Macros()
keyboard.modules.append(macros)

# --------------------------
#  SWITCH INPUT PINS
#  Based on your schematic, example:
#  GP1–GP9  → board.D1 .. board.D9
# --------------------------

PINS = [
    board.D1,
    board.D2,
    board.D3,
    board.D4,
    board.D5,
    board.D6,
    board.D7,
    board.D8,
    board.D9,
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,  # switches pull to GND
)

# --------------------------
#  KEYMAP (9 keys)
#  You can replace these with anything
#  https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# --------------------------

keyboard.keymap = [
    [
        KC.A,             # key 1
        KC.B,             # key 2
        KC.C,             # key 3
        KC.D,             # key 4
        KC.E,             # key 5
        KC.F,             # key 6
        KC.G,             # key 7
        KC.H,             # key 8

        # key 9 = macro example
        KC.MACRO(
            Press(KC.LCTRL),
            Tap(KC.S),
            Release(KC.LCTRL)
        ),
    ]
]

# --------------------------
#  START KMK
# --------------------------

if __name__ == '__main__':
    keyboard.go()
