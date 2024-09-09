# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Akai_Force_MPC/session_recording.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 885 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import SessionRecordingComponent as SessionRecordingComponentBase
from ableton.v2.control_surface.control import ToggleButtonControl

class SessionRecordingComponent(SessionRecordingComponentBase):
    mpc_automation_toggle = ToggleButtonControl(toggled_color="Automation.On",
      untoggled_color="Automation.Off")

    def _on_session_automation_record_changed(self):
        super(SessionRecordingComponent, self)._on_session_automation_record_changed()
        self.mpc_automation_toggle.is_toggled = self.song.session_automation_record

    @mpc_automation_toggle.toggled
    def mpc_automation_toggle(self, is_toggled, _):
        self.song.session_automation_record = is_toggled
