# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/ATOMSQ/midi.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 621 bytes
from __future__ import absolute_import, print_function, unicode_literals
NATIVE_MODE_ON_MESSAGE = (143, 0, 1)
NATIVE_MODE_OFF_MESSAGE = (143, 0, 0)
RED_MIDI_CHANNEL = 1
GREEN_MIDI_CHANNEL = 2
BLUE_MIDI_CHANNEL = 3
USER_MODE_START_CHANNEL = 10
SYSEX_START_BYTE = 240
SYSEX_END_BYTE = 247
PRODUCT_ID_BYTES = (0, 1, 6, 34)
SYSEX_HEADER = (
 SYSEX_START_BYTE,) + PRODUCT_ID_BYTES
DISPLAY_HEADER = SYSEX_HEADER + (18, )
LOWER_FIRMWARE_TOGGLE_HEADER = SYSEX_HEADER + (19, )
UPPER_FIRMWARE_TOGGLE_HEADER = SYSEX_HEADER + (20, )
