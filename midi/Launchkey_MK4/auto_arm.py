# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK4/auto_arm.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1504 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.base import depends, listens
from ableton.v3.control_surface.components import AutoArmComponent as AutoArmComponentBase

class AutoArmComponent(AutoArmComponentBase):

    @depends(session_ring=None)
    def __init__(self, session_ring=None, *a, **k):
        (super().__init__)(*a, **k)
        self._last_track_offset = -1
        self._AutoArmComponent__on_offset_changed.subject = session_ring

    @listens("offset")
    def __on_offset_changed(self, track_offset, _):
        if track_offset != self._last_track_offset:
            self._set_auto_arm_state(False)
        self._last_track_offset = track_offset
