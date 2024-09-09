# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Komplete_Kontrol_S_Mk2/meter_display_element.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1543 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
from ableton.v2.base import task
from ableton.v2.control_surface import ControlElement, midi
METERS_PER_SEGMENT = 2
CLEAR_VALUE = 0

class MeterDisplayElement(ControlElement):

    def __init__(self, header, num_segments, *a, **k):
        (super(MeterDisplayElement, self).__init__)(*a, **k)
        self._header = header
        self._clear_values = [CLEAR_VALUE for _ in range(num_segments * METERS_PER_SEGMENT)]
        self._meter_values = list(self._clear_values)
        self._last_sent_message = None
        self._send_message_task = self._tasks.add(task.run(self._send_message))
        self._send_message_task.kill()

    def update_meter_display(self, display_offset, values):
        self._meter_values[display_offset] = values[0]
        self._meter_values[display_offset + 1] = values[1]
        self._request_send_message()

    def reset(self):
        self._meter_values = list(self._clear_values)
        self._request_send_message()

    def send_midi(self, midi_bytes):
        if midi_bytes != self._last_sent_message:
            super(MeterDisplayElement, self).send_midi(midi_bytes)
            self._last_sent_message = midi_bytes

    def _request_send_message(self):
        self._send_message_task.restart()

    def _send_message(self, *a):
        self.send_midi(self._header + tuple(self._meter_values) + (midi.SYSEX_END,))
