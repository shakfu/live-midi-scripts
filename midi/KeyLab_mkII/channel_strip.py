# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/KeyLab_mkII/channel_strip.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 893 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import liveobj_valid
from ableton.v2.control_surface.control import TextDisplayControl
from KeyLab_Essential.channel_strip import ChannelStripComponent as ChannelStripComponentBase

class ChannelStripComponent(ChannelStripComponentBase):
    track_name_display = TextDisplayControl(" ")

    def set_track_name_display(self, display):
        self.track_name_display.set_control_element(display)
        self._update_track_name_display()

    def set_track(self, track):
        super(ChannelStripComponent, self).set_track(track)
        self._update_track_name_display()

    def _update_track_name_display(self):
        track = self._track
        self.track_name_display[0] = track.name if liveobj_valid(track) else ""
