# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Launchkey_MK3/transport.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 465 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.control import ButtonControl
from novation.transport import TransportComponent as TransportComponentBase

class TransportComponent(TransportComponentBase):
    alt_stop_button = ButtonControl()

    @alt_stop_button.pressed
    def alt_stop_button(self, _):
        self.song.is_playing = False
