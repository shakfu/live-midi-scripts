# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Keystage/mappings.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 824 bytes
from __future__ import absolute_import, print_function, unicode_literals

def create_mappings(_):
    mappings = {}
    mappings["Transport"] = dict(play_button="play_button",
      stop_button="stop_button",
      loop_button="loop_button",
      tap_tempo_button="tempo_button",
      metronome_button="metronome_button",
      rewind_button="rewind_button",
      fastforward_button="fastforward_button")
    mappings["View_Based_Recording"] = dict(record_button="record_button")
    mappings["Undo_Redo"] = dict(undo_button="undo_button")
    mappings["View_Control"] = dict(prev_track_button="up_button",
      next_track_button="down_button")
    mappings["Device"] = dict(parameter_controls="knobs")
    return mappings
