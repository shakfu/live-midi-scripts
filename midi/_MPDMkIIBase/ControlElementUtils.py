# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_MPDMkIIBase/ControlElementUtils.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 763 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Framework.ButtonElement import ButtonElement as ButtonElement
from _Framework.EncoderElement import EncoderElement as EncoderElement
from _Framework.InputControlElement import MIDI_CC_TYPE
from _Framework.SliderElement import SliderElement as SliderElement

def make_encoder(identifier, channel, name):
    return EncoderElement(MIDI_CC_TYPE,
      channel, identifier, (Live.MidiMap.MapMode.absolute), name=name)


def make_slider(identifier, channel, name):
    return SliderElement(MIDI_CC_TYPE, channel, identifier, name=name)


def make_button(identifier, channel, name):
    return ButtonElement(True, MIDI_CC_TYPE, channel, identifier, name=name)
