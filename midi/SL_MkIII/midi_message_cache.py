# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/SL_MkIII/midi_message_cache.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 725 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .sysex import NUM_SET_PROPERTY_HEADER_BYTES

class MidiMessageCache:

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._messages = []

    def __call__(self, message):
        self._messages = list(filter((lambda m: m[:NUM_SET_PROPERTY_HEADER_BYTES] != message[:NUM_SET_PROPERTY_HEADER_BYTES]), self._messages))
        self._messages.append(message)

    @property
    def messages(self):
        return self._messages

    def clear(self):
        self._messages = []
