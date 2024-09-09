# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Push2/velocity.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 611 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import EventObject, liveobj_valid
from ableton.v2.control_surface import LiveObjectDecorator, get_parameter_by_name

class VelocityDeviceDecorator(LiveObjectDecorator, EventObject):

    def __init__(self, *a, **k):
        (super(VelocityDeviceDecorator, self).__init__)(*a, **k)
        self._add_switch_option(name="Operation",
          pname="Operation",
          labels=["Vel", "Rel", "Both"])
        self.register_disconnectables(self.options)
