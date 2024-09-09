# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/KeyLab_mkII/mixer.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 599 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import liveobj_valid
from novation.mixer import MixerComponent as MixerComponentBase

class MixerComponent(MixerComponentBase):

    def set_selected_track_name_display(self, display):
        self._selected_strip.set_track_name_display(display)

    def _update_selected_strip(self):
        selected_strip = self._selected_strip
        if liveobj_valid(selected_strip):
            selected_strip.set_track(self.song.view.selected_track)
