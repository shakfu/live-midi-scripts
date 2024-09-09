# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/MaxForLive/MaxForLive.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 2246 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import SimpleControlSurface
from ableton.v2.control_surface.input_control_element import MIDI_CC_TYPE, MIDI_NOTE_TYPE, MIDI_PB_TYPE, InputControlElement
STATUS_TO_TYPE = {144:MIDI_NOTE_TYPE, 
 176:MIDI_CC_TYPE,  224:MIDI_PB_TYPE}

class MaxForLive(SimpleControlSurface):

    def __init__(self, *a, **k):
        (super(MaxForLive, self).__init__)(*a, **k)
        self._registered_control_names = []
        self._registered_messages = []

    def register_midi_controlParse error at or near `LOAD_GLOBAL' instruction at offset 62