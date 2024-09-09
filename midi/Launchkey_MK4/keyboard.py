# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK4/keyboard.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1364 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.base import task
from ableton.v3.control_surface.components import PitchProvider, PlayableComponent

class KeyboardComponent(PlayableComponent, PitchProvider):
    is_polyphonic = True

    def __init__(self, *a, **k):
        (super().__init__)(a, matrix_always_listenable=True, **k)
        self._note_editor = None
        self.pitches = [36]
        self._chord_detection_task = self._tasks.add(task.wait(0.3))
        self._chord_detection_task.kill()

    def set_note_editor(self, note_editor):
        self._note_editor = note_editor

    def _on_matrix_pressed(self, button):
        pitch = button.index
        if self._note_editor and self._note_editor.active_steps:
            self._note_editor.toggle_pitch_for_all_active_steps(pitch)
        elif self._chord_detection_task.is_running:
            self.pitches.append(pitch)
        else:
            self.pitches = [
             pitch]
            self._chord_detection_task.restart()

    def _update_led_feedback(self):
        pass
