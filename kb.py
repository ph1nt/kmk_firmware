from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation
import board


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP18,
        board.GP19,
        board.GP20,
        board.GP21,
        board.GP22,
        board.GP16,
        board.GP17,
        board.GP6,
        board.GP7,
        board.GP8,
        board.GP9,
        board.GP10,
        board.GP11,
        board.GP12,
    )
    row_pins = (board.GP5, board.GP4, board.GP3, board.GP2)
    rgb_pixel_pin = board.GP28
    rgb_num_pixels = 12
    diode_orientation = DiodeOrientation.ROWS
