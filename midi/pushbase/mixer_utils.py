# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/pushbase/mixer_utils.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 431 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v2.base import old_hasattr

def is_set_to_split_stereo(mixer):
    modes = Live.MixerDevice.MixerDevice.panning_modes
    return modes.stereo_split == getattr(mixer, "panning_mode", modes.stereo)


def has_pan_mode(mixer):
    return old_hasattr(mixer, "panning_mode")
