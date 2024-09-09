# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/BackgroundComponent.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 2223 bytes
from __future__ import absolute_import, print_function, unicode_literals
from future.utils import raise_
from functools import partial
from .ControlSurfaceComponent import ControlSurfaceComponent
from .SubjectSlot import SubjectSlotError

class BackgroundComponent(ControlSurfaceComponent):

    def __init__(self, *a, **k):
        (super(BackgroundComponent, self).__init__)(*a, **k)
        self._control_slots = {}
        self._control_map = {}

    def __getattr__(self, name):
        if len(name) > 4:
            if name[:4] == "set_":
                return partial(self._clear_control, name[4:])
        raise_(AttributeError, name)

    def _clear_control(self, name, control):
        slot = self._control_slots.get(name, None)
        if slot:
            del self._control_slots[name]
            self.disconnect_disconnectable(slot)
        if control:
            self._reset_control(control)
            self._control_map[name] = control
        elif name in self._control_map:
            del self._control_map[name]

    def _reset_control(self, control):
        control.reset()

    def update(self):
        super(BackgroundComponent, self).update()
        if self.is_enabled():
            for control in self._control_map.values():
                self._reset_control(control)


class ModifierBackgroundComponent(BackgroundComponent):

    def __init__(self, *a, **k):
        (super(ModifierBackgroundComponent, self).__init__)(*a, **k)

    def _reset_control(self, control):
        if len(control.resource.owners) > 1:
            control.set_light(True)
        else:
            control.reset()
