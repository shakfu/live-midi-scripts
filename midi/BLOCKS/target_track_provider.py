# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/BLOCKS/target_track_provider.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 2567 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import listens, listens_group
from ableton.v2.control_surface import Component

class TargetTrackProvider(Component):
    __events__ = ('target_track', 'armed_tracks')

    def __init__(self, *a, **k):
        (super(TargetTrackProvider, self).__init__)(*a, **k)
        self._target_track = None
        self._armed_tracks = []
        self._TargetTrackProvider__on_selected_track_changed.subject = self.song.view
        self._TargetTrackProvider__on_tracks_changed.subject = self.song
        self._TargetTrackProvider__on_tracks_changed()

    @property
    def target_track(self):
        return self._target_track

    @listens("selected_track")
    def __on_selected_track_changed(self):
        if not self._armed_tracks:
            self._update_target_track()

    @listens("tracks")
    def __on_tracks_changed(self):
        tracks = [t for t in self.song.tracks if t.can_be_armed if t.has_midi_input if t.can_be_armed if t.has_midi_input]
        self._TargetTrackProvider__on_arm_changed.replace_subjects(tracks)
        self._TargetTrackProvider__on_frozen_state_changed.replace_subjects(tracks)
        self._update_tracks(tracks)

    @listens_group("arm")
    def __on_arm_changed(self, track):
        if track in self._armed_tracks:
            self._armed_tracks.remove(track)
        if track.arm:
            self._armed_tracks.append(track)
            self._set_target_track(track)
        else:
            self._update_target_track()
        self.notify_armed_tracks()

    @listens_group("is_frozen")
    def __on_frozen_state_changed(self, track):
        if track in self._armed_tracks:
            self._armed_tracks.remove(track)
        self._update_target_track()

    def _update_tracks(self, all_tracks):
        for track in self._armed_tracks:
            if track not in all_tracks:
                self._armed_tracks.remove(track)

        for track in all_tracks:
            if track.arm:
                if track not in self._armed_tracks:
                    self._armed_tracks.append(track)

        self._update_target_track()

    def _update_target_track(self):
        target_track = None
        selected_track = self.song.view.selected_track
        if self._armed_tracks:
            target_track = self._armed_tracks[-1]
        elif not selected_track.is_frozen:
            target_track = selected_track
        self._set_target_track(target_track)

    def _set_target_track(self, track):
        if self._target_track != track:
            self._target_track = track
            self.notify_target_track()
