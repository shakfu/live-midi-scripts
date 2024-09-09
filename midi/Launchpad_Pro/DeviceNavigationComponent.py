# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Pro/DeviceNavigationComponent.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1218 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Framework.Control import ButtonControl
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent as ControlSurfaceComponent
NavDirection = Live.Application.Application.View.NavDirection

class DeviceNavigationComponent(ControlSurfaceComponent):
    device_nav_left_button = ButtonControl(color="Device.Off", pressed_color="Device.On")
    device_nav_right_button = ButtonControl(color="Device.Off", pressed_color="Device.On")

    @device_nav_left_button.pressed
    def device_nav_left_button(self, value):
        self._scroll_device_chain(NavDirection.left)

    @device_nav_right_button.pressed
    def device_nav_right_button(self, value):
        self._scroll_device_chain(NavDirection.right)

    def _scroll_device_chain(self, direction):
        view = self.application().view
        if not (view.is_view_visible("Detail") and view.is_view_visible("Detail/DeviceChain")):
            view.show_view("Detail")
            view.show_view("Detail/DeviceChain")
        else:
            view.scroll_view(direction, "Detail/DeviceChain", False)
