# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/_Komplete_Kontrol/physical_display_element.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 647 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import str
from itertools import chain
from ableton.v2.control_surface.elements import PhysicalDisplayElement as PhysicalDisplayElementBase

class PhysicalDisplayElement(PhysicalDisplayElementBase):

    def _build_display_message(self, display):
        return chain(*map((lambda x: self._translate_string(str(x).strip())), display._logical_segments))

    def _request_send_message(self):
        self._send_message()
