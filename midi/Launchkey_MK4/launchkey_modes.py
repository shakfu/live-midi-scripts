# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK4/launchkey_modes.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 619 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.mode import ModesComponent

class LaunchkeyModesComponent(ModesComponent):

    def _handle_mode_selection_control_value(self, value):
        if self.is_enabled():
            if value < len(self.modes):
                self.previous_mode = self.selected_mode
                mode = self.modes[value]
                self._get_mode_behaviour(mode).press_immediate(self, mode)
