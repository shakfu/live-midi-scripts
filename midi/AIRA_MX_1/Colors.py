# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/AIRA_MX_1/Colors.py
# Compiled at: 2024-08-28 00:57:02
# Size of source mod 2**32: 589 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ButtonElement import Color
BLINK_LED_CHANNEL = 14

class Blink(Color):

    def draw(self, interface):
        interface.send_value(self.midi_value)
        interface.send_value(0, channel=BLINK_LED_CHANNEL)


class Rgb:
    BLACK = Color(0)
    RED = Color(5)
    RED_BLINK = Blink(5)
    GREEN_HALF = Color(20)
    GREEN = Color(21)
    GREEN_BLINK = Blink(21)
    BLUE_HALF = Color(44)
    BLUE = Color(45)
    BLUE_BLINK = Blink(45)
