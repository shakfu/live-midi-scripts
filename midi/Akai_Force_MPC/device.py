# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Akai_Force_MPC/device.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 2651 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import clamp, listens, liveobj_valid
from ableton.v2.control_surface import ParameterInfo
from ableton.v2.control_surface.components import DeviceComponent as DeviceComponentBase
from ableton.v2.control_surface.control import ButtonControl, TextDisplayControl, ToggleButtonControl

class DeviceComponent(DeviceComponentBase):
    prev_bank_button = ButtonControl(color="Action.Off", pressed_color="Action.On")
    next_bank_button = ButtonControl(color="Action.Off", pressed_color="Action.On")
    bank_name_display = TextDisplayControl()
    device_lock_button = ToggleButtonControl()

    def __init__(self, toggle_lock=None, *a, **k):
        (super(DeviceComponent, self).__init__)(*a, **k)
        self._toggle_lock = toggle_lock
        self._DeviceComponent__on_is_locked_to_device_changed.subject = self._device_provider
        self._DeviceComponent__on_is_locked_to_device_changed()

    @prev_bank_button.pressed
    def prev_bank_button(self, _):
        self._scroll_bank(-1)

    @next_bank_button.pressed
    def next_bank_button(self, _):
        self._scroll_bank(1)

    @device_lock_button.toggled
    def device_lock_button(self, toggled, _):
        self._toggle_lock()
        self._update_device_lock_button()

    def _create_parameter_info(self, parameter, name):
        return ParameterInfo(parameter=parameter,
          name=name,
          default_encoder_sensitivity=1.0)

    def _set_bank_index(self, index):
        super(DeviceComponent, self)._set_bank_index(index)
        self._update_bank_name_display()

    def _scroll_bank(self, offset):
        bank = self._bank
        if bank:
            new_index = clamp(bank.index + offset, 0, bank.bank_count() - 1)
            self._device_bank_registry.set_device_bank(self.device(), new_index)

    def _update_bank_name_display(self):
        bank_name = ""
        device = self.device()
        if liveobj_valid(device):
            device_bank_names = self._banking_info.device_bank_names(device)
            if device_bank_names:
                bank_name = device_bank_names[self._device_bank_registry.get_device_bank(device)]
        self.bank_name_display[0] = bank_name

    def _update_device_lock_button(self):
        self.device_lock_button.is_toggled = self._device_provider.is_locked_to_device

    @listens("is_locked_to_device")
    def __on_is_locked_to_device_changed(self):
        self._update_device_lock_button()
