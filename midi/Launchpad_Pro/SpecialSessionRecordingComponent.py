# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Launchpad_Pro/SpecialSessionRecordingComponent.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 2641 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Framework.ClipCreator import ClipCreator as ClipCreator
from _Framework.SessionRecordingComponent import SessionRecordingComponent, subject_slot, track_is_recording, track_playing_slot

class SpecialSessionRecordingComponent(SessionRecordingComponent):

    def __init__(self, target_track_component, *a, **k):
        self._target_track_component = target_track_component
        self._modes_component = None
        self._note_mode_name = None
        (super(SpecialSessionRecordingComponent, self).__init__)(
 ClipCreator(), True, *a, **k)

    def set_modes_component(self, modes_component):
        self._modes_component = modes_component

    def set_note_mode_name(self, name):
        self._note_mode_name = name

    @subject_slot("value")
    def _on_record_button_value(self, value):
        if self.is_enabled() and value:
            if self._modes_component.selected_mode == self._note_mode_name:
                self._handle_note_mode_record_behavior()
            elif not self._stop_recording():
                self._start_recording()

    def _handle_note_mode_record_behavior(self):
        track = self._target_track_component.target_track
        if self._track_can_record(track):
            playing_slot = track_playing_slot(track)
            should_overdub = not track_is_recording(track) and playing_slot != None
            if should_overdub:
                self.song().overdub = not self.song().overdub
                self.song().is_playing = self.song().is_playing or True
            elif not self._stop_recording():
                self._prepare_new_slot(track)
                self._start_recording()
        elif not self._stop_recording():
            self._start_recording()

    def _prepare_new_slot(self, track):
        song = self.song()
        song.overdub = False
        view = song.view
        try:
            slot_index = list(song.scenes).index(view.selected_scene)
            track.stop_all_clips(False)
            self._jump_to_next_slot(track, slot_index)
        except Live.Base.LimitationError:
            self._handle_limitation_error_on_scene_creation()

    def _track_can_record(self, track):
        return track in self.song().tracks and track.can_be_armed
