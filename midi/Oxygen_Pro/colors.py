# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Oxygen_Pro/colors.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 395 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.elements import Color

class Basic:
    ON = Color(127)
    OFF = Color(0)


class Rgb:
    GREEN = Color(12)
    GREEN_BLINK = Color(76)
    RED = Color(3)
    RED_BLINK = Color(67)
    AMBER = Color(11)
    WHITE = Color(63)
