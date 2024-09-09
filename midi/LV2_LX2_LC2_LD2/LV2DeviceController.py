# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/LV2_LX2_LC2_LD2/LV2DeviceController.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 404 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from .FaderfoxDeviceController import FaderfoxDeviceController

class LV2DeviceController(FaderfoxDeviceController):
    __module__ = __name__

    def __init__(self, parent):
        LV2DeviceController.realinit(self, parent)

    def realinit(self, parent):
        FaderfoxDeviceController.realinit(self, parent)
