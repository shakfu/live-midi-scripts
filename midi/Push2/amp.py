# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Push2/amp.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 551 bytes
from __future__ import absolute_import, print_function, unicode_literals
from enum import IntEnum
from ableton.v2.base import EventObject, liveobj_valid
from ableton.v2.control_surface import LiveObjectDecorator

class AmpDeviceDecorator(LiveObjectDecorator, EventObject):

    def __init__(self, *a, **k):
        (super(AmpDeviceDecorator, self).__init__)(*a, **k)
        self._add_on_off_option(name="Dual Mono", pname="Dual Mono")
        self.register_disconnectables(self.options)
