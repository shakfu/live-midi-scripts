# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/ableton/v3/control_surface/elements/discrete_values.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 2385 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ...base import is_iterable, nop
from .. import MIDI_CC_TYPE, InputControlElement, NotifyingControlElement

class ValueElement(NotifyingControlElement):

    def __init__(self, *a, **k):
        (super().__init__)(a, is_private=True, **k)
        self.send_value = nop
        self.set_light = nop
        self.is_momentary = lambda: False

    def reset(self):
        pass


class DiscreteValuesElement(InputControlElement):

    def __init__(self, identifier, channel=0, msg_type=MIDI_CC_TYPE, values=None, *a, **k):
        (super().__init__)(a, **, **k)
        self._sub_elements = {v: ValueElement() for v in values}

    def script_wants_forwarding(self):
        return True

    def message_map_mode(self):
        raise AssertionError("DiscreteValuesElement doesn't support mapping.")

    def receive_value(self, value):
        super().receive_value(value)
        if value in self._sub_elements:
            self._sub_elements[value].notify_value(127)

    def __iter__(self):
        for element in self._sub_elements.values():
            yield element

    def __getitem__(self, value):
        return self._sub_elements[value]

    def __len__(self):
        return len(self._sub_elements)
