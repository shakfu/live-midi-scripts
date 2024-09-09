# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Launchpad_MK2/ComponentUtils.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 399 bytes
from __future__ import absolute_import, print_function, unicode_literals

def skin_scroll_component(component):
    for button in (component.scroll_up_button, component.scroll_down_button):
        button.color = "Scrolling.Enabled"
        button.pressed_color = "Scrolling.Pressed"
        button.disabled_color = "Scrolling.Disabled"
