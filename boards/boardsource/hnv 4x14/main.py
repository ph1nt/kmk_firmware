from kb import KMKKeyboard
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

media = MediaKeys()
layers_ext = Layers()

keyboard.modules = [layers_ext]
keyboard.extensions = [media]

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

LOWER = KC.MO(1)
RAISE = KC.MO(2)
Fn1 = KC.MO(1)
Fn2 = KC.MO(2)
NUM = KC.TT(3)
RC = KC.MT(KC.SLSH, KC.RCTRL)
SE = KC.MT(KC.SPACE, KC.RSFT)
ES = KC.MT(KC.ESC, KC.LSFT)
RG = KC.MT(KC.BSPC, KC.RCMD)
RA = KC.MT(KC.ENTER, KC.RALT)
LG = KC.MT(KC.BSPC, KC.LCMD)
LA = KC.MT(KC.ENTER, KC.LALT)
LC = KC.MT(KC.Z, KC.LCTRL)

# fmt: off
# ---------------------- Keymap ---------------------------------------------------------
keyboard.keymap = [
    # layer 0
    [
        KC.N1,       KC.N2,       KC.N3,       KC.N4,       KC.N5,       ES,          Fn1,         KC.N6,       KC.N7,         KC.N8,         KC.N9,         KC.N0,           Fn2,         KC.LEFT,
        KC.Q,        KC.W,        KC.E,        KC.R,        KC.T,        NUM,         LA,          KC.Y,        KC.U,          KC.I,          KC.O,          KC.P,            RA,          KC.UP,
        KC.A,        KC.S,        KC.D,        KC.F,        KC.G,        KC.TAB,      KC.RCMD,     KC.H,        KC.J,          KC.K,          KC.L,          KC.SCLN,         RG,          KC.DOWN,         
        LC,          KC.X,        KC.C,        KC.V,        KC.B,        ______,      ______,      KC.N,        KC.M,          KC.COMM,       KC.DOT,        KC.SLSH,         SE,          KC.RGHT,
    ],
    # layer 1 (left) Fn1
    [
        KC.F1,       KC.F2,       KC.F3,       KC.F4,       KC.F5,       ______,      Fn1,         KC.F6,       KC.F7,         KC.F8,         KC.F9,         KC.EJCT,         Fn2,         KC.HOME,
        KC.DEL,      KC.UP,       KC.BSPC,     ______,      ______,      ______,      ______,      KC.GRV,      KC.UNDS,       KC.PLUS,       KC.MINUS,      KC.EQUAL,        ______,      KC.PGUP,
        KC.LEFT,     KC.DOWN,     KC.RGHT,     ______,      ______,      ______,      ______,      KC.LCBR,     KC.RCBR,       KC.LBRC,       KC.RBRC,       KC.QUOT,         ______,      KC.PGDN,
        ______,      ______,      ______,      ______,      ______,      ______,      ______,      KC.NUBS,     KC.TILDE,      ______,        KC.PIPE,       KC.BSLS,         ______,      KC.END,
    ],
    # layer 2 (right) Fn2
    [
        KC.F1,       KC.F2,       KC.F3,       KC.F4,       KC.F5,       ______,      Fn1,         KC.F6,       KC.F7,         KC.F8,         KC.F9,         KC.F10,          Fn2,         ______,
        KC.F11,      KC.F12,      KC.F13,      KC.F14,      KC.F15,      ______,      ______,      KC.F16,      ______,        KC.MRWD,       KC.MFFD,       KC.MPLY,         ______,      ______,
        KC.RGB_M_K,  KC.RGB_M_B,  KC.RGB_VAI,  KC.RGB_HUI,  KC.RGB_SAI,  ______,      ______,      KC.RGB_TOG,  KC.RGB_M_P,    KC.VOLD,       KC.VOLU,       KC.MUTE,         ______,      ______,
        KC.RGB_M_R,  KC.RGB_M_BR, KC.RGB_VAD,  KC.RGB_HUD,  KC.RGB_SAD,  ______,      ______,      LS,          ______,        ______,        ______,        ______,          KC.CAPS,     ______,
    ],
    # layer 3 (NUM)
    [
        ______,      ______,      ______,      ______,      ______,      ______,      ______,      ______,      KC.N7,         KC.N8,         KC.N9,         KC.PSLS,         ______,      ______,
        KC.PWR,      ______,      ______,      ______,      ______,      ______,      ______,      ______,      KC.N4,         KC.N5,         KC.N6,         KC.PAST,         ______,      ______,
        ______,      ______,      ______,      ______,      ______,      ______,      ______,      ______,      KC.N1,         KC.N2,         KC.N3,         KC.PMNS,         ______,      ______,
        ______,      ______,      ______,      ______,      ______,      ______,      ______,      ______,      KC.N0,         KC.COMM,       KC.DOT,        KC.PPLS,         KC.PEQL,     ______,
    ],
]
# fmt: on

if __name__ == '__main__':
    keyboard.go()
