# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launch_Control/SpecialSessionComponent.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 567 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
from future.moves.itertools import zip_longest
from _Framework.SessionComponent import SessionComponent as SessionComponent

class SpecialSessionComponent(SessionComponent):

    def set_clip_launch_buttons(self, buttons):
        for i, button in zip_longest(range(self._num_tracks), buttons or []):
            scene = self.selected_scene()
            slot = scene.clip_slot(i)
            slot.set_launch_button(button)
