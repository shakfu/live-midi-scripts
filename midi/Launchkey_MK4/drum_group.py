# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Launchkey_MK4/drum_group.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1190 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.base import listens
from ableton.v3.control_surface import LiveObjSkinEntry
from ableton.v3.control_surface.components import DrumGroupComponent as DrumGroupComponentBase
from ableton.v3.live import liveobj_valid

class DrumGroupComponent(DrumGroupComponentBase):

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._DrumGroupComponent__on_target_track_color_changed.subject = self._target_track

    def _update_button_color(self, button):
        pad = self._pad_for_button(button)
        button.color = self._color_for_pad(pad) if pad else LiveObjSkinEntry("DrumGroup.Empty", self._target_track.target_track)

    @listens("target_track.color")
    def __on_target_track_color_changed(self):
        if not liveobj_valid(self._drum_group_device):
            self._update_led_feedback()
