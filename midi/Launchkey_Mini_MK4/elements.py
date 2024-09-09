# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Launchkey_Mini_MK4/elements.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 609 bytes
from __future__ import absolute_import, print_function, unicode_literals
from Launchkey_MK4.elements import LaunchkeyCommonElements

class Elements(LaunchkeyCommonElements):

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self.add_mono_button(102, "Track_Left_Button")
        self.add_mono_button(103, "Track_Right_Button")
        self.add_shifted_control(self.record_button)
