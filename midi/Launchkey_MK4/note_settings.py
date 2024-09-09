# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK4/note_settings.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1936 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import control_list
from .internal_parameter import InternalParameterControl, register_internal_parameter

class NoteSettingsComponent(Component):
    encoders = control_list(InternalParameterControl, 8, num_steps=10)

    def __init__(self, note_editor, *a, **k):
        (super().__init__)(a, name="Note_Settings", **k)
        self._note_editor = note_editor
        self.encoders[0].parameter = register_internal_parameter(self, "Velocity", (lambda _: self._note_editor.get_velocity_range_string()))
        self.encoders[1].parameter = register_internal_parameter(self, "Length", (lambda _: self._note_editor.get_duration_range_string()))
        self.encoders[2].parameter = register_internal_parameter(self, "Fine", (lambda _: self._note_editor.get_duration_fine_range_string()))
        self.encoders[3].parameter = register_internal_parameter(self, "Nudge", (lambda _: self._note_editor.get_nudge_offset_range_string()))
        self.encoders[0].num_steps = 64

    @encoders.value
    def encoders(self, value, encoder):
        index = encoder.index
        if index == 0:
            self._note_editor.set_velocity_offset(value)
        elif index == 1:
            self._note_editor.set_duration_offset(self._note_editor.step_length * value)
        elif index == 2:
            self._note_editor.set_duration_offset(self._note_editor.step_length * 0.1 * value)
        elif index == 3:
            self._note_editor.set_nudge_offset(self._note_editor.step_length * 0.1 * value)
