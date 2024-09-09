# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/APC_Key_25/SendToggleComponent.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 811 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Control import ButtonControl
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent as ControlSurfaceComponent

class SendToggleComponent(ControlSurfaceComponent):
    toggle_control = ButtonControl()

    def __init__(self, mixer, *args, **kwargs):
        (super(SendToggleComponent, self).__init__)(*args, **kwargs)
        self.mixer = mixer
        self.last_number_of_sends = self.mixer.num_sends
        self.set_toggle_button = self.toggle_control.set_control_element

    def inc_send_index(self):
        if self.mixer.num_sends:
            self.mixer.send_index = (self.mixer.send_index + 1) % self.mixer.num_sends

    @toggle_control.pressed
    def toggle_button_pressed(self, _button):
        self.inc_send_index()
