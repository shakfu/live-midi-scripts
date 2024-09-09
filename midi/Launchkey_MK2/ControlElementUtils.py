# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Launchkey_MK2/ControlElementUtils.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1372 bytes
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial
import Live
from _Framework.ButtonElement import ButtonElement as ButtonElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement as ButtonMatrixElement
from _Framework.ComboElement import ComboElement as ComboElement
from _Framework.Dependency import depends
from _Framework.EncoderElement import EncoderElement as EncoderElement
from _Framework.InputControlElement import MIDI_CC_TYPE, MIDI_NOTE_TYPE
from _Framework.Resource import PrioritizedResource
from _Framework.SliderElement import SliderElement as SliderElement
from .consts import STANDARD_CHANNEL

@depends(skin=None)
def make_button(identifier, msg_type=MIDI_NOTE_TYPE, is_momentary=True, skin=None, is_modifier=False, name=""):
    return ButtonElement(is_momentary,
      msg_type,
      STANDARD_CHANNEL,
      identifier,
      skin=skin,
      name=name,
      resource_type=(PrioritizedResource if is_modifier else None))


def make_encoder(identifier, name=''):
    return EncoderElement(MIDI_CC_TYPE,
      STANDARD_CHANNEL,
      identifier,
      (Live.MidiMap.MapMode.absolute),
      name=name)


def make_slider(identifier, name="", channel=STANDARD_CHANNEL):
    return SliderElement(MIDI_CC_TYPE, channel, identifier, name=name)
