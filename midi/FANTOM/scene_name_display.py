# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/FANTOM/scene_name_display.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 705 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .simple_display import SimpleDisplayElement, adjust_string, as_ascii
from .sysex import NAME_LENGTH, NAME_TERMINATOR

class SceneNameDisplayElement(SimpleDisplayElement):

    def display_data(self, data):
        data_to_send = [
         len(data)]
        for scene in data:
            data_to_send.extend(as_ascii(adjust_string(scene.name, NAME_LENGTH).strip()))
            data_to_send.append(NAME_TERMINATOR)

        self._message_to_send = self._message_header + tuple(data_to_send) + self._message_tail
        self._request_send_message()
