# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Launchkey_MK4/encoder_touch.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1642 bytes
from functools import partial
from ableton.v3.base import listenable_property, task
from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import ButtonControl, control_matrix
from ableton.v3.control_surface.display import Renderable

class EncoderTouchComponent(Component, Renderable):
    touch_controls = control_matrix(ButtonControl)
    last_released_index = listenable_property.managed(None)

    def __init__(self, *a, **k):
        (super().__init__)(a, name="Encoder_Touch", **k)
        self._release_tasks = [self._tasks.add(task.sequence(task.wait(0.1), task.run(partial(self._set_released, i)), task.run(partial(self._set_released, None)))) for i in range(8)]
        for release_task in self._release_tasks:
            release_task.kill()

    @touch_controls.pressed
    def touch_controls(self, control):
        self._release_tasks[control.index].kill()

    @touch_controls.released
    def touch_controls(self, control):
        self._release_tasks[control.index].restart()

    def _set_released(self, index):
        self.last_released_index = index
