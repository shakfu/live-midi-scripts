# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/OpenLabs/SpecialDeviceComponent.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1055 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Framework.DeviceComponent import DeviceComponent as DeviceComponent

class SpecialDeviceComponent(DeviceComponent):

    def __init__(self):
        DeviceComponent.__init__(self)

    def _device_parameters_to_map(self):
        return self._device.parameters[1:]
