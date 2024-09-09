# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_Essential/arrangement.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 843 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import move_current_song_time
from ableton.v2.control_surface import Component
from ableton.v2.control_surface.control import ButtonControl, EncoderControl

class ArrangementComponent(Component):
    set_or_delete_cue_button = ButtonControl()
    jump_encoder = EncoderControl()

    @set_or_delete_cue_button.pressed
    def set_or_delete_cue_button(self, _):
        if self.application.view.focused_document_view == "Arranger":
            self.song.set_or_delete_cue()

    @jump_encoder.value
    def jump_encoder(self, value, _):
        step = -1.0 if value < 0 else 1.0
        if self.song.is_playing:
            step *= 4.0
        move_current_song_time(self.song, step)
