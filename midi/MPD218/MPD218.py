# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/MPD218/MPD218.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 417 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _MPDMkIIBase.MPDMkIIBase import MPDMkIIBase as MPDMkIIBase
PAD_CHANNEL = 9
PAD_IDS = [
 [
  48, 49, 50, 51], [44, 45, 46, 47], [40, 41, 42, 43], [36, 37, 38, 39]]

class MPD218(MPDMkIIBase):

    def __init__(self, *a, **k):
        (super(MPD218, self).__init__)(PAD_IDS, PAD_CHANNEL, *a, **k)
