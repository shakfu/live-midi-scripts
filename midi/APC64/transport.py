# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/APC64/transport.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 2046 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.base import task
from ableton.v3.control_surface.components import TransportComponent as TransportComponentBase
from ableton.v3.control_surface.controls import ButtonControl

class TransportComponent(TransportComponentBase):
    tap_tempo_button = ButtonControl()
    shift_button = ButtonControl()

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._can_trigger_tap_tempo = False
        self._disable_tap_tempo_task = self._tasks.add(task.sequence(task.wait(1), task.run(self._disable_tap_tempo)))
        self._disable_tap_tempo_task.kill()

    @tap_tempo_button.pressed
    def tap_tempo_button(self, _):
        if self._can_trigger_tap_tempo:
            self._trigger_tap_tempo()

    @tap_tempo_button.released_immediately
    def tap_tempo_button(self, _):
        self._can_trigger_tap_tempo = True
        self._disable_tap_tempo_task.restart()

    @tap_tempo_button.released_delayed
    def tap_tempo_button(self, _):
        self._disable_tap_tempo()

    def _disable_tap_tempo(self):
        self._can_trigger_tap_tempo = False

    def _toggle_record_quantize(self):
        if self.shift_button.is_pressed:
            super()._toggle_record_quantize()
