# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_mk3/mixer.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 2541 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.base import find_if, listenable_property, nop
from ableton.v3.control_surface.components import MixerComponent as MixerComponentBase
from ableton.v3.control_surface.components import SessionNavigationComponent as SessionNavigationComponentBase
from ableton.v3.control_surface.components import SessionRingComponent
from ableton.v3.live import liveobj_valid, simple_track_name

class SessionNavigationComponent(SessionNavigationComponentBase):

    def set_horizontal_page_encoder(self, encoder):
        self._horizontal_paging.set_scroll_encoder(encoder)


class MixerSessionRingComponent(SessionRingComponent):

    def __init__(self, *a, **k):
        (super().__init__)(a, **, **k)

    @listenable_property
    def controlled_range(self):
        tracks = self.tracks
        last_track = find_if(liveobj_valid, reversed(tracks))
        return "Tracks {} to {}".format(simple_track_name(tracks[0]), simple_track_name(last_track))

    def move(self, tracks, scenes):
        super().move(tracks, scenes)
        self.notify_controlled_range()
        self.notify(self.notifications.controlled_range, "", self.controlled_range)


class MixerComponent(MixerComponentBase):

    def __init__(self, *a, **k):
        self._session_ring = MixerSessionRingComponent()
        (super().__init__)(a, session_ring=self._session_ring, **k)
        self._session_navigation = SessionNavigationComponent(session_ring=(self._session_ring),
          snap_track_offset=True,
          parent=self)
        self.add_children(self._session_ring)

    def set_track_bank_encoder(self, encoder):
        self._session_navigation.set_horizontal_page_encoder(encoder)
