# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Push/drum_group_component.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 508 bytes
from __future__ import absolute_import, print_function, unicode_literals
from pushbase.drum_group_component import DrumGroupComponent as DrumGroupComponentBase

class DrumGroupComponent(DrumGroupComponentBase):

    def __init__(self, selector=None, *a, **k):
        (super(DrumGroupComponent, self).__init__)(*a, **k)
        self._selector = selector

    def select_drum_pad(self, drum_pad):
        self._selector.on_select_drum_pad(drum_pad)
