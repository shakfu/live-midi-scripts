# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_mk3/active_parameter.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1388 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.base import find_if, listenable_property
from ableton.v3.control_surface.components import ActiveParameterComponent as ActiveParameterComponentBase
from ableton.v3.live import liveobj_valid

class ActiveParameterComponent(ActiveParameterComponentBase):

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._is_fader_map = {}

    def set_touch_controls(self, controls):
        self.touch_controls.set_control_element(controls)
        if controls:
            self._is_fader_map = {c: int(c.name.split("_")[-1]) > 8 for c in controls}

    @listenable_property
    def is_fader(self):
        return self._is_fader_map.get(find_if((lambda elem: liveobj_valid(elem.controlled_parameter)), (elem for elem in reversed(list(self._pressed_touch_elements.values())))), False)

    def notify_parameter(self):
        super().notify_parameter()
        self.notify_is_fader()
