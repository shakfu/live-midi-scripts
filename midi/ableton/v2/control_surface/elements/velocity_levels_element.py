# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/ableton/v2/control_surface/elements/velocity_levels_element.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 857 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ...base import EventObject, listenable_property
from .proxy_element import ProxyElement

class NullVelocityLevels(EventObject):
    enabled = False
    target_note = -1
    target_channel = -1
    source_channel = -1
    notes = []

    @property
    def levels(self):
        return []

    @listenable_property
    def last_played_level(self):
        return -1.0


class VelocityLevelsElement(ProxyElement):

    def __init__(self, velocity_levels=None, *a, **k):
        super(VelocityLevelsElement, self).__init__(proxied_object=velocity_levels,
          proxied_interface=(NullVelocityLevels()))

    def reset(self):
        self.notes = []
        self.source_channel = -1
