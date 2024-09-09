# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_Mini_MK4/mappings.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 648 bytes
from __future__ import absolute_import, print_function, unicode_literals
from Launchkey_MK4.mappings import create_launchkey_common_mappings

def create_mappings(control_surface):
    mappings = create_launchkey_common_mappings(control_surface)
    mappings["Transport"] = dict(play_toggle_button="play_button",
      play_pause_button="play_button_with_shift",
      capture_midi_button="record_button_with_shift")
    mappings["View_Control"] = dict(prev_track_button="track_left_button",
      next_track_button="track_right_button")
    return mappings
