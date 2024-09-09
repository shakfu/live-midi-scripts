# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ATOM/note_pad.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 590 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.controls import PlayableControl

class NotePadMixin:

    def set_matrix(self, matrix):
        super().set_matrix(matrix)
        for button in self.matrix:
            button.set_mode(PlayableControl.Mode.playable_and_listenable)
            button.pressed_color = "NotePad.Pressed"

    def _on_matrix_pressed(self, _):
        pass

    def _on_matrix_released(self, button):
        self._update_button_color(button)
