# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/SL_MkIII/transport.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1908 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import TransportComponent as TransportComponentBase

class TransportComponent(TransportComponentBase):

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._loop_toggle.view_transform = lambda v: "Transport.LoopOn" if v else "Transport.LoopOff"
        self._record_toggle.view_transform = lambda v: "Recording.On" if v else "Recording.Off"

    def set_seek_forward_button(self, ffwd_button):
        super().set_seek_forward_button(ffwd_button)
        self._update_seek_button(self._ffwd_button)

    def set_seek_backward_button(self, rwd_button):
        super().set_seek_backward_button(rwd_button)
        self._update_seek_button(self._rwd_button)

    def _ffwd_value(self, value):
        super()._ffwd_value(value)
        self._update_seek_button(self._ffwd_button)

    def _rwd_value(self, value):
        super()._rwd_value(value)
        self._update_seek_button(self._rwd_button)

    def _update_button_states(self):
        super()._update_button_states()
        self._update_continue_playing_button()

    def _update_continue_playing_button(self):
        self.continue_playing_button.color = "Transport.PlayOn" if self.song.is_playing else "Transport.PlayOff"

    def _update_seek_button(self, button):
        if self.is_enabled():
            if button is not None:
                button.set_light("Transport.SeekOn" if button.is_pressed() else "Transport.SeekOff")

    def _update_stop_button_color(self):
        self.stop_button.color = "Transport.StopEnabled" if self.play_button.is_toggled else "Transport.StopDisabled"
