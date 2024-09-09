# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/consts.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 771 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import DEFAULT_PRIORITY
LOW_PRIORITY = DEFAULT_PRIORITY - 1
HIGH_PRIORITY = DEFAULT_PRIORITY + 1
M4L_PRIORITY = HIGH_PRIORITY + 1
MOMENTARY_DELAY = 0.3
ACTIVE_PARAMETER_TIMEOUT = 0.75
