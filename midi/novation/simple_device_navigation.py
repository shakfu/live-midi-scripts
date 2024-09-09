# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/novation/simple_device_navigation.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1342 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v2.control_surface import Component
from ableton.v2.control_surface.control import ButtonControl
NavDirection = Live.Application.Application.View.NavDirection

class SimpleDeviceNavigationComponent(Component):
    next_button = ButtonControl(color="Device.Navigation",
      pressed_color="Device.NavigationPressed")
    prev_button = ButtonControl(color="Device.Navigation",
      pressed_color="Device.NavigationPressed")

    @next_button.pressed
    def next_button(self, value):
        self._scroll_device_chain(NavDirection.right)

    @prev_button.pressed
    def prev_button(self, value):
        self._scroll_device_chain(NavDirection.left)

    def _scroll_device_chain(self, direction):
        view = self.application.view
        if not (view.is_view_visible("Detail") and view.is_view_visible("Detail/DeviceChain")):
            view.show_view("Detail")
            view.show_view("Detail/DeviceChain")
        else:
            view.scroll_view(direction, "Detail/DeviceChain", False)
