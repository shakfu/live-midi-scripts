# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK4/scale.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 4277 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v3.base import listens, task
from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import SendValueInputControl
FIRMWARE_SCALES = ((0, 2, 4, 5, 7, 9, 11), (0, 2, 3, 5, 7, 8, 10), (0, 2, 3, 5, 7, 9, 10),
                   (0, 2, 4, 5, 7, 9, 10), (0, 2, 4, 6, 7, 9, 11), (0, 1, 3, 5, 7, 8, 10),
                   (0, 1, 3, 5, 6, 8, 10), (0, 2, 4, 6, 8, 10), (0, 1, 3, 4, 6, 7, 9, 10),
                   (0, 2, 3, 5, 6, 8, 9, 11), (0, 3, 5, 6, 7, 10), (0, 3, 5, 7, 10),
                   (0, 2, 4, 7, 9), (0, 2, 3, 5, 7, 8, 11), (0, 2, 4, 5, 7, 8, 11),
                   (0, 2, 3, 6, 7, 9, 10), (0, 1, 4, 5, 7, 8, 10), (0, 2, 3, 5, 7, 9, 11),
                   (0, 2, 4, 6, 8, 9, 11), (0, 2, 4, 6, 7, 9, 10), (0, 1, 3, 4, 6, 8, 10),
                   (0, 1, 3, 4, 5, 6, 8, 10), (0, 1, 4, 5, 7, 8, 11), (0, 2, 3, 6, 7, 8, 11),
                   (0, 2, 3, 7, 8), (0, 1, 5, 7, 10), (0, 1, 5, 6, 10), (0, 2, 3, 7, 9),
                   (0, 1, 3, 7, 8), (0, 1, 5, 7, 8))
SCALE_NAMES = [
 None] + [{s[1]: s[0] for s in Live.Song.get_all_scales_ordered()}.get(intervals, None) for intervals in FIRMWARE_SCALES]
del FIRMWARE_SCALES

class ScaleComponent(Component):
    scale_type_control = SendValueInputControl()
    root_note_control = SendValueInputControl()

    def __init__(self, *a, **k):
        (super().__init__)(a, name="Scales", **k)

        def make_task(fn):
            t = self._tasks.add(task.sequence(task.wait(0.1), task.run(fn)))
            t.kill()
            return t

        self._update_scale_type_control_task = make_task(self._update_scale_type_control)
        self._update_root_note_control_task = make_task(self._update_root_note_control)
        self._ScaleComponent__on_scale_type_changed_in_song.subject = self.song
        self._ScaleComponent__on_root_note_changed_in_song.subject = self.song
        self._ScaleComponent__on_scale_type_changed_in_song()
        self._ScaleComponent__on_root_note_changed_in_song()

    @scale_type_control.value
    def scale_type_control(self, value, _):
        if value in range(len(SCALE_NAMES)):
            scale_name = SCALE_NAMES[value]
            if scale_name is not None:
                if self.song.scale_name != scale_name:
                    self.song.scale_name = scale_name

    @root_note_control.value
    def root_note_control(self, value, _):
        if value in range(12):
            if self.song.root_note != value:
                self.song.root_note = value

    def _update_scale_type_control(self):
        if self.song.scale_name in SCALE_NAMES:
            self.scale_type_control.value = SCALE_NAMES.index(self.song.scale_name)

    def _update_root_note_control(self):
        self.root_note_control.value = self.song.root_note

    @listens("scale_name")
    def __on_scale_type_changed_in_song(self):
        self._update_scale_type_control_task.restart()

    @listens("root_note")
    def __on_root_note_changed_in_song(self):
        self._update_root_note_control_task.restart()
