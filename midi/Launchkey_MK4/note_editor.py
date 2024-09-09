# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Launchkey_MK4/note_editor.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1695 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.base import listens
from ableton.v3.control_surface import LiveObjSkinEntry
from ableton.v3.control_surface.components.bar_based_sequence import NoteEditorComponent as NoteEditorComponentBase

class NoteEditorComponent(NoteEditorComponentBase):

    def set_clip(self, clip):
        super().set_clip(clip)
        self._NoteEditorComponent__on_clip_color_changed.subject = clip

    def get_duration_fine_range_string(self):
        result = self._get_property_range_string("duration",
          (lambda value_range: (v / self.step_length for v in value_range)),
          str_fmt=("{:.1f}".format))
        return "{}{}".format(result, " steps" if result != "No Notes" else "")

    def _update_editor_matrix(self):
        if self.is_enabled():
            visible_steps = self._visible_steps()
            for (index, button) in enumerate(self.matrix):
                button.color = LiveObjSkinEntry(self._get_color_for_step(index, visible_steps), self._clip)

    @listens("color")
    def __on_clip_color_changed(self):
        self._update_editor_matrix()
