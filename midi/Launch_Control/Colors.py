# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Launch_Control/Colors.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 451 bytes
from __future__ import absolute_import, print_function, unicode_literals
LED_OFF = 4
LED_ON = 15
RED_FULL = 7
RED_HALF = 6
RED_THIRD = 5
RED_BLINK = 11
GREEN_FULL = 52
GREEN_HALF = 36
GREEN_THIRD = 20
GREEN_BLINK = 56
YELLOW_FULL = 62
AMBER_FULL = RED_FULL + GREEN_FULL - 4
AMBER_HALF = RED_HALF + GREEN_HALF - 4
AMBER_THIRD = RED_THIRD + GREEN_THIRD - 4
AMBER_BLINK = AMBER_FULL - 4 + 8
