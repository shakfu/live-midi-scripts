# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/SL_MkIII/message.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 533 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import Component
from .control import TextDisplayControl
NUM_MESSAGE_SEGMENTS = 2

class MessageComponent(Component):
    display = TextDisplayControl(segments=(('', ) * NUM_MESSAGE_SEGMENTS))

    def __call__(self, *messages):
        for index, message in zip(range(NUM_MESSAGE_SEGMENTS), messages):
            self.display[index] = message if message else ""
