# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Push2/beatrepeat.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 818 bytes
from __future__ import absolute_import, print_function, unicode_literals
from enum import IntEnum
from ableton.v2.base import EventObject, liveobj_valid
from ableton.v2.control_surface import LiveObjectDecorator

class BeatRepeatDeviceDecorator(LiveObjectDecorator, EventObject):

    def __init__(self, *a, **k):
        (super(BeatRepeatDeviceDecorator, self).__init__)(*a, **k)
        self._add_switch_option(name="Mix Type",
          pname="Mix Type",
          labels=["Mix", "Ins", "Gate"])
        self._add_on_off_option(name="Repeat", pname="Repeat")
        self._add_on_off_option(name="Filter", pname="Filter On")
        self._add_on_off_option(name="Triplets", pname="Block Triplets")
        self.register_disconnectables(self.options)
