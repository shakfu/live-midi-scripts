# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/ableton/v2/base/live_api_utils.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1636 bytes
from __future__ import absolute_import, print_function, unicode_literals

def liveobj_changed(obj, other):
    return obj != other or type(obj) != type(other)


def liveobj_valid(obj):
    return obj != None


def is_parameter_bipolar(param):
    return param.min == -1 * param.max


def duplicate_clip_loop(clip):
    if liveobj_valid(clip) and clip.is_midi_clip:
        try:
            clip.duplicate_loop()
        except RuntimeError:
            pass


def move_current_song_time(song, delta, truncate_to_beat=True):
    new_time = max(0, song.current_song_time + delta)
    if truncate_to_beat:
        new_time = int(new_time)
    song.current_song_time = new_time
    if not song.is_playing:
        song.start_time = new_time
