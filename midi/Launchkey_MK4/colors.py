# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Launchkey_MK4/colors.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1757 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.base import memoize
from ableton.v3.control_surface import STANDARD_COLOR_PALETTE, STANDARD_FALLBACK_COLOR_TABLE
from ableton.v3.control_surface.elements import ColorPart, ComplexColor, SimpleColor
from ableton.v3.live import liveobj_color_to_value_from_palette, liveobj_valid
BLINK_CHANNEL = 1
PULSE_CHANNEL = 2

@memoize
def make_simple_color(value):
    return SimpleColor(value)


def make_color_for_liveobj(obj):
    color = make_simple_color(liveobj_color_to_value_from_palette(obj,
      palette=STANDARD_COLOR_PALETTE,
      fallback_table=STANDARD_FALLBACK_COLOR_TABLE))
    if liveobj_valid(obj):
        if not color.midi_value:
            return Rgb.WHITE_HALF
        return color


def make_animated_color(value, animation_channel):
    return ComplexColor((ColorPart(0), ColorPart(value, animation_channel)))


class Mono:
    OFF = SimpleColor(0)
    DIM = SimpleColor(32)
    ON = SimpleColor(127)
    BLINK = make_animated_color(127, BLINK_CHANNEL)


class Rgb:
    OFF = SimpleColor(0)
    WHITE = SimpleColor(3)
    WHITE_HALF = SimpleColor(1)
    RED = SimpleColor(5)
    RED_HALF = SimpleColor(7)
    RED_BLINK = make_animated_color(5, BLINK_CHANNEL)
    RED_PULSE = make_animated_color(5, PULSE_CHANNEL)
    GREEN = SimpleColor(21)
    GREEN_BLINK = make_animated_color(21, BLINK_CHANNEL)
    GREEN_PULSE = make_animated_color(21, PULSE_CHANNEL)
    BLUE = SimpleColor(41)
    BLUE_HALF = SimpleColor(43)
    LIGHT_BLUE = SimpleColor(37)
    DARK_BLUE = SimpleColor(49)
    ORANGE = SimpleColor(96)
    ORANGE_HALF = SimpleColor(83)
