# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/SL_MkIII/device_parameters.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1965 bytes
from __future__ import absolute_import, print_function, unicode_literals
from future.moves.itertools import zip_longest
from ableton.v2.control_surface import InternalParameterBase
from ableton.v2.control_surface.components import DisplayingDeviceParameterComponent
from ableton.v2.control_surface.control import ColorSysexControl, control_list
from .util import convert_parameter_value_to_midi_value

def is_internal_parameter(parameter):
    return isinstance(parameter, InternalParameterBase)


WIDTH = 8

class DeviceParameterComponent(DisplayingDeviceParameterComponent):
    parameter_color_fields = control_list(ColorSysexControl, WIDTH)
    encoder_color_fields = control_list(ColorSysexControl, WIDTH)

    def __init__(self, *a, **k):
        self._parameter_controls = None
        (super().__init__)(*a, **k)

    def set_parameter_controls(self, encoders):
        super().set_parameter_controls(encoders)
        self._parameter_controls = encoders

    def _update_parameter_values(self):
        super()._update_parameter_values()
        for (parameter, control) in zip_longest(self.parameters, self._parameter_controls or []):
            if is_internal_parameter(parameter):
                if control:
                    control.send_value(convert_parameter_value_to_midi_value(parameter))

    def _update_parameters(self):
        super()._update_parameters()
        self._update_color_fields()

    def _update_color_fields(self):
        for (color_field_index, parameter_info) in zip_longest(range(WIDTH), self._parameter_provider.parameters[:WIDTH]):
            parameter = parameter_info.parameter if parameter_info else None
            color = "Device.On" if parameter else "DefaultButton.Disabled"
            self.parameter_color_fields[color_field_index].color = color
            self.encoder_color_fields[color_field_index].color = color
