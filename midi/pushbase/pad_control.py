# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/pushbase/pad_control.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1146 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.control import PlayableControl

class PadControl(PlayableControl):

    class State(PlayableControl.State):

        def __init__(self, sensitivity_profile=None, *a, **k):
            (super(PadControl.State, self).__init__)(*a, **k)
            self._sensitivity_profile = sensitivity_profile

        def _get_sensitivity_profile(self):
            return self._sensitivity_profile

        def _set_sensitivity_profile(self, value):
            self._sensitivity_profile = value
            self._update_sensitivity()

        sensitivity_profile = property(_get_sensitivity_profile, _set_sensitivity_profile)

        def set_control_element(self, control_element):
            super(PadControl.State, self).set_control_element(control_element)
            self._update_sensitivity()

        def _update_sensitivity(self):
            if self._control_element:
                if self._sensitivity_profile:
                    self._control_element.sensitivity_profile = self._sensitivity_profile
