# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK4/internal_parameter.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1548 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface import InternalParameter
from ableton.v3.control_surface.controls import StepEncoderControl
from ableton.v3.live import liveobj_valid

def register_internal_parameter(parent, name, display_fn):
    return parent.register_disconnectable(InternalParameter(name=name, display_value_conversion=display_fn))


class InternalParameterControl(StepEncoderControl):

    class State(StepEncoderControl.State):

        def __init__(self, num_steps=64, *a, **k):
            (super().__init__)(a, num_steps=num_steps, **k)
            self._parameter = None

        @property
        def parameter(self):
            return self._parameter

        @parameter.setter
        def parameter(self, parameter):
            self._parameter = parameter

        def set_control_element(self, control_element):
            if self._control_element:
                self._control_element.release_parameter()
            super().set_control_element(control_element)
            if self._control_element:
                if liveobj_valid(self._parameter):
                    self._control_element.connect_to(self._parameter)
