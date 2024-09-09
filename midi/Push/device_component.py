# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Push/device_component.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1736 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import liveobj_valid
from ableton.v2.control_surface import ParameterInfo
from ableton.v2.control_surface.components import DeviceComponent as DeviceComponentBase
from ableton.v2.control_surface.control import ButtonControl
from .parameter_mapping_sensitivities import fine_grain_parameter_mapping_sensitivity, parameter_mapping_sensitivity

def is_wavetable(device):
    return liveobj_valid(device) and device.class_name == "InstrumentVector"


class DeviceComponent(DeviceComponentBase):
    shift_button = ButtonControl()

    @shift_button.pressed
    def shift_button(self, button):
        decorated_device = self.device()
        if is_wavetable(decorated_device):
            decorated_device.osc_1_pitch.adjust_finegrain = True
            decorated_device.osc_2_pitch.adjust_finegrain = True

    @shift_button.released
    def shift_button(self, button):
        decorated_device = self.device()
        if is_wavetable(decorated_device):
            decorated_device.osc_1_pitch.adjust_finegrain = False
            decorated_device.osc_2_pitch.adjust_finegrain = False

    def _create_parameter_info(self, parameter, name):
        device_class_name = self.device().class_name
        return ParameterInfo(parameter=parameter,
          name=name,
          default_encoder_sensitivity=(parameter_mapping_sensitivity(parameter, device_class_name)),
          fine_grain_encoder_sensitivity=(fine_grain_parameter_mapping_sensitivity(parameter, device_class_name)))
