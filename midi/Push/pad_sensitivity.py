# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Push/pad_sensitivity.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1161 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import NamedTuple, lazy_attribute
from .sysex import to_bytes

class PadParameters(NamedTuple):
    off_threshold = 0
    on_threshold = 0
    gain = 0
    curve1 = 0
    curve2 = 0
    name = ""

    def __str__(self):
        return self.name

    @lazy_attribute
    def sysex_bytes(self):
        return to_bytes(self.off_threshold, 4) + to_bytes(self.on_threshold, 4) + to_bytes(self.gain, 8) + to_bytes(self.curve1, 8) + to_bytes(self.curve2, 8)


def pad_parameter_sender(global_control, pad_control):

    def do_send(parameters, pad=None):
        if pad != None:
            pad_control.send_value((pad,) + parameters.sysex_bytes)
        else:
            global_control.send_value(parameters.sysex_bytes)

    return do_send
