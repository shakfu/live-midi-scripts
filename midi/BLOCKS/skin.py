# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/BLOCKS/skin.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1316 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object
from ableton.v2.control_surface import Skin
from ableton.v2.control_surface.elements import Color
from .colors import Rgb

class Colors(object):

    class DefaultButton(object):
        On = Rgb.WHITE
        Off = Rgb.BLACK
        Disabled = Rgb.BLACK

    class Session(object):
        RecordButton = Rgb.RED
        ClipTriggeredPlay = Rgb.GREEN_BLINK
        ClipTriggeredRecord = Rgb.RED_BLINK
        ClipStarted = Rgb.GREEN_PULSE
        ClipRecording = Rgb.RED_PULSE
        ClipStopped = Rgb.AMBER
        Scene = Rgb.GREEN
        SceneTriggered = Rgb.GREEN_BLINK
        NoScene = Rgb.BLACK
        StopClipTriggered = Rgb.RED_PULSE
        StopClip = Rgb.RED
        StopClipDisabled = Rgb.BLACK
        ClipEmpty = Rgb.BLACK

    class DrumGroup(object):
        PadEmpty = Rgb.BLACK
        PadFilled = Rgb.YELLOW
        PadSelected = Rgb.LIGHT_BLUE
        PadSelectedNotSoloed = Rgb.LIGHT_BLUE
        PadMuted = Rgb.DARK_ORANGE
        PadMutedSelected = Rgb.LIGHT_BLUE
        PadSoloed = Rgb.DARK_BLUE
        PadSoloedSelected = Rgb.LIGHT_BLUE
        PadInvisible = Rgb.BLACK
        PadAction = Rgb.RED


skin = Skin(Colors)
