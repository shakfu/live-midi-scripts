# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/MiniLab_3/transport.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1598 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v3.base import sign
from ableton.v3.control_surface.components import TransportComponent as TransportComponentBase
from ableton.v3.control_surface.controls import ButtonControl, EncoderControl, ToggleButtonControl
from ableton.v3.live import move_current_song_time

class TransportComponent(TransportComponentBase):
    __events__ = ('transport_event', )
    arrangement_position_encoder = EncoderControl()
    tap_tempo_button = ButtonControl(color="Transport.TapTempo",
      pressed_color="Transport.TapTempoPressed")
    loop_button = ToggleButtonControl(color="Transport.LoopOff",
      on_color="Transport.LoopOn")

    @arrangement_position_encoder.value
    def arrangement_position_encoder(self, value, _):
        move_current_song_time(self.song, sign(value))
        self.notify_transport_event("", str(self.song.get_current_smpte_song_time(Live.Song.TimeFormat.smpte_25)))

    @tap_tempo_button.pressed
    def tap_tempo_button(self, _):
        self._trigger_tap_tempo()

    @tap_tempo_button.released
    def tap_tempo_button(self, _):
        self.notify_transport_event("Tap Tempo", "{} BPM".format(int(self.song.tempo)))

    @loop_button.released
    def loop_button(self, *_):
        self.notify_transport_event("Loop Mode", "ON" if self.song.loop else "OFF")
