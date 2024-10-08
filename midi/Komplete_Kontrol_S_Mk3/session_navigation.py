# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Komplete_Kontrol_S_Mk3/session_navigation.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1744 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.base import listens
from ableton.v3.control_surface.components import SessionNavigationComponent as SessionNavigationComponentBase
from .view_control import add_scroll_encoder, update_scroll_encoder

class SessionNavigationComponent(SessionNavigationComponentBase):

    def __init__(self, *a, **k):
        (super().__init__)(a, snap_track_offset=True, **k)
        add_scroll_encoder(self._horizontal_paging)
        self._session_ring = self._SessionNavigationComponent__on_offset_changed.subject
        self._SessionNavigationComponent__on_selected_track_changed.subject = self.song.view
        self._SessionNavigationComponent__on_selected_track_changed()

    def set_track_bank_encoder(self, encoder):
        self._horizontal_paging.encoder.set_control_element(encoder)
        self._update_horizontal()

    def _update_horizontal(self):
        super()._update_horizontal()
        update_scroll_encoder(self._horizontal_paging)

    @listens("selected_track")
    def __on_selected_track_changed(self):
        selected_track = self.song.view.selected_track
        if selected_track not in self._session_ring.tracks:
            all_tracks = list(self._session_ring.tracks_to_use())
            self._session_ring.track_offset = all_tracks.index(selected_track)
