# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Akai_Force_MPC/physical_display.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 714 bytes
from __future__ import absolute_import, print_function, unicode_literals
from itertools import chain, starmap
from ableton.v2.base import clamp, group
from ableton.v2.control_surface.elements import PhysicalDisplayElement as PhysicalDisplayElementBase

def message_length(message):
    length = len(message)
    return (
     clamp(length // 128, 0, 127), length % 128)


class PhysicalDisplayElement(PhysicalDisplayElementBase):

    def _build_display_message(self, display):
        message_string = display.display_string.strip()
        return chain(message_length(message_string), self._translate_string(message_string))
