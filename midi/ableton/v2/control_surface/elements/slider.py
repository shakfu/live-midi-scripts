# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/elements/slider.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 531 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ..input_control_element import MIDI_NOTE_TYPE
from .encoder import EncoderElement

class SliderElement(EncoderElement):

    def __init__(self, msg_type, channel, identifier, *a, **k):
        (super(SliderElement, self).__init__)(
 msg_type, channel, identifier, *a, map_mode=Live.MidiMap.MapMode.absolute, **k)
