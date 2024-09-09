# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/MiniLab_3/sysex.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1329 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.elements import SysexElement as SysexElementBase
from .midi import COMMAND_ID_TO_DAW_PROGRAM_ID

class SysexElement(SysexElementBase):

    def receive_value(self, value):
        if len(value) == 2:
            if value[0] in COMMAND_ID_TO_DAW_PROGRAM_ID:
                super().receive_value(int(value[1] == COMMAND_ID_TO_DAW_PROGRAM_ID[value[0]]))
