# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/novation/clip_slot.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 949 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import const, depends
from ableton.v2.control_surface.components import ClipSlotComponent as ClipSlotComponentBase

class FixedLengthClipSlotComponent(ClipSlotComponentBase):

    @depends(fixed_length_recording=(const(None)))
    def __init__(self, fixed_length_recording, *a, **k):
        (super(FixedLengthClipSlotComponent, self).__init__)(*a, **k)
        self._fixed_length_recording = fixed_length_recording

    def _do_launch_clip(self, fire_state):
        slot = self._clip_slot
        if self._fixed_length_recording.should_start_recording_in_slot(slot):
            self._fixed_length_recording.start_recording_in_slot(slot)
        else:
            super(FixedLengthClipSlotComponent, self)._do_launch_clip(fire_state)
