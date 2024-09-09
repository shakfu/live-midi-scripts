# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/MIDI_Mix/ControlElementUtils.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1154 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Framework.ButtonElement import ButtonElement as ButtonElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement as ButtonMatrixElement
from _Framework.Dependency import depends
from _Framework.EncoderElement import EncoderElement as EncoderElement
from _Framework.InputControlElement import MIDI_CC_TYPE, MIDI_NOTE_TYPE
from _Framework.SliderElement import SliderElement as SliderElement

@depends(skin=None)
def make_button(identifier, name, skin=None):
    return ButtonElement(True, MIDI_NOTE_TYPE, 0, identifier, name=name, skin=skin)


def make_slider(identifier, name):
    return SliderElement(MIDI_CC_TYPE, 0, identifier, name=name)


def make_encoder(identifier, name):
    return EncoderElement(MIDI_CC_TYPE,
      0, identifier, map_mode=(Live.MidiMap.MapMode.absolute), name=name)


def make_button_row(identifier_sequence, element_factory, name):
    return ButtonMatrixElement(rows=[[element_factory(identifier, name + "_%d" % index)] for index, identifier in enumerate(identifier_sequence)])
