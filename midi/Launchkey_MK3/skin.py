# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK3/skin.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 873 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import Skin, merge_skins
from novation.colors import Mono, Rgb
from novation.skin import skin as base_skin

class Colors:

    class DefaultButton:
        On = Mono.ON

    class TrackNavigation:
        On = Mono.HALF
        Pressed = Mono.ON

    class Device:
        Navigation = Rgb.PURPLE_HALF
        NavigationPressed = Rgb.PURPLE

    class DrumGroup:
        PadSelected = Rgb.WHITE
        PadSelectedNotSoloed = Rgb.WHITE
        PadMutedSelected = Rgb.WHITE
        PadSoloedSelected = Rgb.WHITE

    class Mode:

        class Device:

            class Bank:
                Selected = Rgb.PURPLE
                Available = Rgb.PURPLE_HALF


skin = merge_skins(base_skin, Skin(Colors)*())
