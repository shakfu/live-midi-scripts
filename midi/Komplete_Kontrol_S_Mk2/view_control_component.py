# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Komplete_Kontrol_S_Mk2/view_control_component.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 2105 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import Component
from ableton.v2.control_surface.components import BasicSceneScroller, BasicTrackScroller
from ableton.v2.control_surface.control import SendValueEncoderControl

class ViewControlComponent(Component):
    track_encoder = SendValueEncoderControl()
    scene_encoder = SendValueEncoderControl()

    def __init__(self, *a, **k):
        (super(ViewControlComponent, self).__init__)(*a, **k)
        self._track_scroller = BasicTrackScroller()
        self._scene_scroller = BasicSceneScroller()
        song = self.song
        view = song.view
        self.register_slot(song, self._update_track_encoder, "visible_tracks")
        self.register_slot(song, self._update_track_encoder, "return_tracks")
        self.register_slot(view, self._update_track_encoder, "selected_track")
        self.register_slot(song, self._update_scene_encoder, "scenes")
        self.register_slot(view, self._update_scene_encoder, "selected_scene")

    @track_encoder.value
    def track_encoder(self, value, _):
        self._do_scroll(value, self._track_scroller)

    @scene_encoder.value
    def scene_encoder(self, value, _):
        self._do_scroll(value, self._scene_scroller)

    def _do_scroll(self, value, scroller):
        if value < 0:
            scroller.scroll_up()
        else:
            scroller.scroll_down()

    def update(self):
        super(ViewControlComponent, self).update()
        self._update_track_encoder()
        self._update_scene_encoder()

    def _update_track_encoder(self):
        if self.is_enabled():
            self.track_encoder.value = int(self._track_scroller.can_scroll_up()) ^ int(self._track_scroller.can_scroll_down() << 1)

    def _update_scene_encoder(self):
        if self.is_enabled():
            self.scene_encoder.value = int(self._scene_scroller.can_scroll_up()) ^ int(self._scene_scroller.can_scroll_down() << 1)
