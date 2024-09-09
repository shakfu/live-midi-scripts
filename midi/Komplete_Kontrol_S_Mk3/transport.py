# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Komplete_Kontrol_S_Mk3/transport.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 419 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.components import TransportComponent as TransportComponentBase

class TransportComponent(TransportComponentBase):

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self.set_position_encoders_use_bar_increments(True)
