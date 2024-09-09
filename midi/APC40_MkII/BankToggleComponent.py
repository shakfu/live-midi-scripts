# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/APC40_MkII/BankToggleComponent.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 914 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ComboElement import ToggleElement
from _Framework.Control import ToggleButtonControl
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent as ControlSurfaceComponent

class BankToggleComponent(ControlSurfaceComponent):
    bank_toggle_button = ToggleButtonControl()

    def __init__(self, *a, **k):
        (super(BankToggleComponent, self).__init__)(*a, **k)
        self._toggle_elements = []

    @bank_toggle_button.toggled
    def bank_toggle_button(self, toggled, button):
        for e in self._toggle_elements:
            e.set_toggled(toggled)

    def create_toggle_element(self, *a, **k):
        element = ToggleElement(*a, **k)
        element.toggled = self.bank_toggle_button.is_toggled
        self._toggle_elements.append(element)
        return element
