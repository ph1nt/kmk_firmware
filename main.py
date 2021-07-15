from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.extensions.rgb import RGB
from kmk.keys import KC
from kmk.extensions.media_keys import MediaKeys
from kb import KMKKeyboard
# pylint: disable=import-error
import board
# pylint: enable=import-error

keyboard = KMKKeyboard()

media = MediaKeys()
layers_ext = Layers()
modtap = ModTap()
rgb_ext = RGB(pixel_pin=board.GP28, num_pixels=12, val_limit=12, hue_default=0, sat_default=100, val_default=20)


keyboard.modules = [layers_ext, modtap]
keyboard.extensions = [media, rgb_ext]

# Cleaner key names
_______ = KC.TRNS
xxxxxxx = KC.NO

LOWER = KC.MO(1)
RAISE = KC.MO(2)
Fn1 = KC.MO(1)
Fn2 = KC.MO(2)
NUM = KC.TT(3)

RC = KC.MT(KC.SLSH, KC.RCTL)
SE = KC.MT(KC.SPACE, KC.RSFT)
ES = KC.MT(KC.ESC, KC.LSFT)
RG = KC.MT(KC.BSPC, KC.RCMD)
RA = KC.MT(KC.ENTER, KC.RALT)
LG = KC.MT(KC.BSPC, KC.LCMD)
LA = KC.MT(KC.ENTER, KC.LALT)
LC = KC.MT(KC.Z, KC.LCTRL)
UNDR = KC.LSFT(KC.MINUS)
PLUS = KC.LSFT(KC.EQUAL)
LCBR = KC.LSFT(KC.LBRC)
RCBR = KC.LSFT(KC.RBRC)
PIPE = KC.LSFT(KC.BSLS)

# pylint: disable=line-too-long
# fmt: off
# ---------------------- Keymap ---------------------------------------------------------
keyboard.keymap = [
    # layer 0
    [
        KC.N1,       KC.N2,       KC.N3,       KC.N4,       KC.N5,       ES,          Fn1,         KC.N6,       KC.N7,         KC.N8,         KC.N9,         KC.N0,           Fn2,         KC.LEFT,
        KC.Q,        KC.W,        KC.E,        KC.R,        KC.T,        NUM,         LA,          KC.Y,        KC.U,          KC.I,          KC.O,          KC.P,            RA,          KC.UP,
        KC.A,        KC.S,        KC.D,        KC.F,        KC.G,        KC.TAB,      KC.RCMD,     KC.H,        KC.J,          KC.K,          KC.L,          KC.SCLN,         RG,          KC.DOWN,
        LC,          KC.X,        KC.C,        KC.V,        KC.B,        _______,     _______,     KC.N,        KC.M,          KC.COMM,       KC.DOT,        KC.SLSH,         SE,          KC.RGHT,
    ],
    # layer 1 (left) Fn1
    [
        KC.F1,       KC.F2,       KC.F3,       KC.F4,       KC.F5,      _______,      Fn1,         KC.F6,       KC.F7,         KC.F8,         KC.F9,         KC.EJCT,         Fn2,         KC.HOME,
        KC.DEL,      KC.UP,       KC.BSPC,    _______,     _______,     _______,     _______,      KC.GRV,      UNDR,          PLUS,          KC.MINUS,      KC.EQUAL,        _______,      KC.PGUP,
        KC.LEFT,     KC.DOWN,     KC.RGHT,    _______,     _______,     _______,     _______,      LCBR,        RCBR,          KC.LBRC,       KC.RBRC,       KC.QUOT,         _______,      KC.PGDN,
        _______,     _______,     _______,    _______,     _______,     _______,     _______,      KC.NUBS,     KC.TILDE,      _______,       PIPE,          KC.BSLS,         _______,      KC.END,
    ],
    # layer 2 (right) Fn2
    [
        KC.F1,       KC.F2,       KC.F3,       KC.F4,       KC.F5,      _______,      Fn1,         KC.F6,       KC.F7,         KC.F8,         KC.F9,         KC.F10,         Fn2,         _______,
        KC.F11,      KC.F12,      KC.F13,      KC.F14,      KC.F15,     _______,     _______,      KC.F16,      _______,       KC.MRWD,       KC.MFFD,       KC.MPLY,        _______,     _______,
        KC.RGB_M_K,  KC.RGB_M_B,  KC.RGB_VAI,  KC.RGB_HUI,  KC.RGB_SAI, _______,     _______,      KC.RGB_TOG,  KC.RGB_M_P,    KC.VOLD,       KC.VOLU,       KC.MUTE,        _______,     _______,
        KC.RGB_M_R,  KC.RGB_M_BR, KC.RGB_VAD,  KC.RGB_HUD,  KC.RGB_SAD, _______,     _______,      _______,     _______,       _______,       _______,       _______,        KC.CAPS,     _______,
    ],
    # layer 3 (NUM)
    [
       _______,     _______,     _______,     _______,     _______,     _______,     _______,     _______,      KC.N7,         KC.N8,         KC.N9,         KC.PSLS,        _______,     _______,
       _______,     _______,     _______,     _______,     _______,     _______,     _______,     _______,      KC.N4,         KC.N5,         KC.N6,         KC.PAST,        _______,     _______,
       _______,     _______,     _______,     _______,     _______,     _______,     _______,     _______,      KC.N1,         KC.N2,         KC.N3,         KC.PMNS,        _______,     _______,
       _______,     _______,     _______,     _______,     _______,     _______,     _______,     _______,      KC.N0,         KC.COMM,       KC.DOT,        KC.PPLS,        KC.PEQL,     _______,
    ],
]
# fmt: on
# pylint: enable=line-too-long

if __name__ == '__main__':
    keyboard.go()
