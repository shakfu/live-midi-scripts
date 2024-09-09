# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/AIRA_MX_1/ControlElementUtils.py
# Compiled at: 2024-08-28 00:57:02
# Size of source mod 2**32: 1170 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Framework.Resource import PrioritizedResource
from _Framework.Dependency import depends
from _Framework.InputControlElement import MIDI_NOTE_TYPE, MIDI_CC_TYPE
from _Framework.ComboElement import ComboElement as ComboElement
from _Framework.ButtonElement import ButtonElement as ButtonElement
from _Framework.EncoderElement import EncoderElement as EncoderElement

@depends(skin=None)
def make_button(name, identifier, channel=0, msg_type=MIDI_NOTE_TYPE, is_momentary=True, is_modifier=False, skin=None):
    return ButtonElement(is_momentary,
      msg_type,
      channel,
      identifier,
      name=name,
      resource_type=(PrioritizedResource if is_modifier else None),
      skin=skin)


def make_encoder(name, identifier, channel=0):
    return EncoderElement(MIDI_CC_TYPE,
      channel, identifier, (Live.MidiMap.MapMode.absolute), name=name)


def with_modifier(control, modifier):
    return ComboElement(control,
      modifiers=[modifier], name=(control.name + "_With_Modifier"))
