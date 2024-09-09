# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Launchkey_MK4/cue_point.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 4690 bytes
from __future__ import absolute_import, print_function, unicode_literals
from bisect import bisect_left, bisect_right
from operator import attrgetter
from ableton.v3.base import listens, listens_group
from ableton.v3.control_surface import Component
from .internal_parameter import InternalParameterControl, register_internal_parameter

class CuePointComponent(Component):
    encoder = InternalParameterControl(num_steps=5)

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._cue_points = []
        self._cue_point_times = []
        self._last_cue_point_name = "-"
        self._last_song_time = -1
        self._next_cue_point_time = None
        self.encoder.parameter = register_internal_parameter(self, "Marker Select", (lambda _: self._last_cue_point_name))
        self.register_slot(self.song, self._refresh_cue_points, "cue_points")
        self._refresh_cue_points()

    def set_encoder(self, encoder):
        self.encoder.set_control_element(encoder)
        self._update_song_time_listener()

    @encoder.value
    def encoder(self, value, _):
        self._jump_to_cue_point(self._find_cue_point(find_next=(value > 0)))

    def _jump_to_cue_point(self, cue_point):
        if cue_point is not None:
            self.song.current_song_time = cue_point.time
            if not self.song.is_playing:
                self.song.start_time = cue_point.time

    def _find_cue_point(self, find_next=True, can_offset_song_time=True):
        song_time = self.song.current_song_time
        if find_next:
            index = bisect_right(self._cue_point_times, song_time)
        elif self.song.is_playing:
            if can_offset_song_time:
                song_time -= 1.0
            index = bisect_left(self._cue_point_times, song_time) - 1
        return self._get_cue_point_by_index(index)

    def _get_cue_point_by_index(self, index):
        if index in range(len(self._cue_points)):
            return self._cue_points[index]

    def _refresh_cue_points(self):
        self._cue_points = sorted((self.song.cue_points), key=(attrgetter("time")))
        self._cue_point_times = [cp.time for cp in self._cue_points]
        self._CuePointComponent__on_cue_point_time_changed.replace_subjects(self.song.cue_points)
        self.encoder.enabled = bool(self._cue_points)
        self._update_song_time_listener()

    def _refresh_cue_point_name_and_next_target(self):
        self._last_cue_point_name = "No Markers"
        self._next_cue_point_time = None
        if self._cue_points:
            next_cue_point = self._find_cue_point()
            self._next_cue_point_time = next_cue_point.time if next_cue_point else None
            song_time = self.song.current_song_time
            if self.song.is_cue_point_selected() and song_time in self._cue_point_times:
                last_cue_point = self._get_cue_point_by_index(self._cue_point_times.index(song_time))
            else:
                last_cue_point = self._find_cue_point(find_next=False,
                  can_offset_song_time=False)
            self._last_cue_point_name = last_cue_point.name if last_cue_point else "-"

    def _update_song_time_listener(self):
        self._last_song_time = -1
        self._CuePointComponent__on_song_time_changed.subject = self.song if (self.encoder.control_element) and (bool(self._cue_points)) else None
        self._refresh_cue_point_name_and_next_target()

    @listens_group("time")
    def __on_cue_point_time_changed(self, _):
        self._refresh_cue_points()

    @listens("current_song_time")
    def __on_song_time_changed(self):
        song_time = self.song.current_song_time
        if song_time < self._last_song_time or self._next_cue_point_time is not None and song_time >= self._next_cue_point_time:
            self._refresh_cue_point_name_and_next_target()
        self._last_song_time = self.song.current_song_time
