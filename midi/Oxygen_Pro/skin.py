# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Oxygen_Pro/skin.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1087 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import Skin
from .colors import Basic, Rgb

class Colors:

    class DefaultButton:
        On = Basic.ON
        Off = Basic.OFF
        Disabled = Basic.OFF

    class Transport:
        PlayOn = Basic.ON
        PlayOff = Basic.OFF

    class Recording:
        On = Basic.ON
        Transition = Basic.ON
        Off = Basic.OFF

    class Mixer:
        ArmOn = Basic.ON
        ArmOff = Basic.OFF
        MuteOn = Basic.ON
        MuteOff = Basic.OFF
        SoloOn = Basic.ON
        SoloOff = Basic.OFF
        EmptyTrack = Basic.OFF

    class Session:
        ClipEmpty = Rgb.WHITE
        ClipTriggeredPlay = Rgb.GREEN_BLINK
        ClipTriggeredRecord = Rgb.RED_BLINK
        ClipStopped = Rgb.AMBER
        ClipStarted = Rgb.GREEN
        ClipRecording = Rgb.RED
        RecordButton = Basic.OFF
        Scene = Basic.OFF
        NoScene = Basic.OFF
        SceneTriggered = Basic.ON


skin = Skin(Colors)
