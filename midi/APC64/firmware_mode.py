# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/APC64/firmware_mode.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1663 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.elements import SysexElement

class FirmwareModeElement(SysexElement):

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._suppress_next_send_value = False

    def receive_value(self, value):
        self._suppress_next_send_value = True
        super().receive_value(value)

    def send_value(self, *a, **k):
        if self._suppress_next_send_value:
            self._suppress_next_send_value = False
            return
        (super().send_value)(*a, **k)

    def clear_send_cache(self):
        self._suppress_next_send_value = True
