# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_X/channel_strip.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1106 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import next
from ableton.v2.base import liveobj_valid
from novation.channel_strip import ChannelStripComponent as ChannelStripComponentBase

class ChannelStripComponent(ChannelStripComponentBase):

    def update(self):
        super(ChannelStripComponent, self).update()
        self._update_static_color_control()

    def _update_static_color_control(self):
        valid_track = liveobj_valid(self._track)
        color_value = self._static_color_value if valid_track else 0
        if valid_track and self._send_controls:
            send_index = next((i for (i, x) in enumerate(self._send_controls)), None)
            if send_index is not None:
                if send_index >= len(self._track.mixer_device.sends):
                    color_value = 0
            self.static_color_control.value = color_value
