# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_mk3/mode_buttons.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 624 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import ButtonControl
from ableton.v3.control_surface.display import Renderable

class ModeButtonsComponent(Component, Renderable):
    device_button = ButtonControl()
    mixer_button = ButtonControl()

    def __init__(self, *a, **k):
        (super().__init__)(a, name="Mode_Buttons", **k)
