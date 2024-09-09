# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Launchkey_MK4/transport.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 2745 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.base import round_to_multiple, sign
from ableton.v3.control_surface.components import TransportComponent as TransportComponentBase
from ableton.v3.live import get_bar_length, move_current_song_time
from .internal_parameter import InternalParameterControl, register_internal_parameter

def format_beat_time(beat_time):
    return "{}.{}.{}".format(beat_time.bars, beat_time.beats, beat_time.sub_division)


class TransportComponent(TransportComponentBase):
    tempo_coarse_encoder = InternalParameterControl()
    arrangement_position_encoder = InternalParameterControl()
    loop_start_encoder = InternalParameterControl()
    loop_length_encoder = InternalParameterControl()

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self.tempo_coarse_encoder.parameter = register_internal_parameter(self, "Tempo", (lambda _: "{} BPM".format(int(self.song.tempo))))
        self.arrangement_position_encoder.parameter = register_internal_parameter(self, "Playback Position", self._position_display_fn)
        self.loop_start_encoder.parameter = register_internal_parameter(self, "Loop Start", self._loop_start_display_fn)
        self.loop_length_encoder.parameter = register_internal_parameter(self, "Loop End", self._loop_length_display_fn)
        self.set_position_encoders_use_bar_increments(True)

    @arrangement_position_encoder.value
    def arrangement_position_encoder(self, value, _):
        move_current_song_time(self.song, self._get_quantized_delta(value))

    def _get_quantized_delta(self, value):
        bar_length = get_bar_length()
        if not self.song.is_playing:
            distance_from_bar = round_to_multiple(self.song.current_song_time, bar_length) - self.song.current_song_time
            if distance_from_bar:
                if value < 0:
                    return distance_from_bar
                return bar_length + distance_from_bar
            return sign(value) * bar_length

    def _position_display_fn(self, _):
        return format_beat_time(self.song.get_current_beats_song_time())

    def _loop_start_display_fn(self, _):
        return format_beat_time(self.song.get_beats_loop_start())

    def _loop_length_display_fn(self, _):
        return format_beat_time(self.song.get_beats_loop_length())
