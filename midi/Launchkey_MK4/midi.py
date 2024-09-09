# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK4/midi.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1791 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.midi import SYSEX_END, SYSEX_START
MAIN_PAD_IDS = [
 range(96, 104), range(112, 120)]
SMALL_MODEL_ID_BYTES = (67, 68)
SET_RELATIVE_ENCODER_MODE = (182, 69, 127)
LAUNCHKEY_COMMON_SYSEX_HEADER = (
 SYSEX_START, 0, 32, 41)
MK4_SYSEX_HEADER = LAUNCHKEY_COMMON_SYSEX_HEADER + (2, 20)
MINI_MK4_SYSEX_HEADER = LAUNCHKEY_COMMON_SYSEX_HEADER + (2, 19)

def make_connection_message(sysex_header, connect=True):
    return sysex_header + (2, 127 if connect else 0, SYSEX_END)


def make_disable_daw_label_popup(sysex_header):
    return sysex_header + (4, 34, 1, SYSEX_END)


def make_enable_touch_output_message():
    return (182, 71, 127)


def make_enable_keyboard_message(enable=True):
    return (
     182, 76, 127 if enable else 0)


def make_enable_drum_pads_message(enable=True):
    return (
     182, 84, 127 if enable else 0)
