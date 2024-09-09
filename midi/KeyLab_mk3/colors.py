# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_mk3/colors.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 2162 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface import BasicColors
from ableton.v3.control_surface.elements import FallbackColor, create_rgb_color
from ableton.v3.live import liveobj_color_to_midi_rgb_values

def create_color(r, g, b):
    return create_rgb_color((r, g, b, 0))


class Rgb:
    OFF = FallbackColor(create_color(0, 0, 0), BasicColors.OFF)
    WHITE_HALF = create_color(32, 32, 32)
    WHITE = FallbackColor(create_color(127, 127, 127), BasicColors.ON)
    RED = create_color(127, 0, 0)
    RED_HALF = create_color(32, 0, 0)
    RED_LOW = create_color(16, 0, 0)
    GREEN = create_color(0, 127, 0)
    GREEN_HALF = create_color(0, 32, 0)
    YELLOW = create_color(127, 72, 0)
    YELLOW_HALF = create_color(32, 24, 0)


class Skin:

    class DefaultButton:
        On = Rgb.WHITE
        Off = Rgb.OFF
        Disabled = Rgb.OFF

    class Transport:
        PlayOn = Rgb.GREEN
        PlayOff = Rgb.GREEN_HALF
        StopOn = Rgb.WHITE
        StopOff = Rgb.WHITE_HALF
        LoopOn = Rgb.YELLOW
        LoopOff = Rgb.YELLOW_HALF
        MetronomeOn = Rgb.WHITE
        MetronomeOff = Rgb.WHITE_HALF
        TapTempoPressed = Rgb.WHITE
        TapTempo = Rgb.WHITE_HALF
        SeekPressed = Rgb.WHITE
        Seek = Rgb.WHITE_HALF
        CanCaptureMidi = Rgb.WHITE

    class Recording:
        ArrangementRecordOn = Rgb.RED
        ArrangementRecordOff = Rgb.RED_HALF
        SessionRecordOn = Rgb.RED
        SessionRecordOff = Rgb.RED_HALF

    class UndoRedo:
        UndoPressed = Rgb.WHITE
        Undo = Rgb.WHITE_HALF
        RedoPressed = Rgb.WHITE
        Redo = Rgb.WHITE_HALF

    class ClipActions:
        Quantize = Rgb.WHITE_HALF
        QuantizePressed = Rgb.WHITE

    class Session:
        Slot = Rgb.OFF
        SlotRecordButton = Rgb.RED_LOW
        NoSlot = Rgb.OFF
        ClipStopped = lambda x: create_color(*liveobj_color_to_midi_rgb_values(x))
        ClipTriggeredPlay = Rgb.GREEN_HALF
        ClipPlaying = Rgb.GREEN
        ClipTriggeredRecord = Rgb.RED_HALF
        ClipRecording = Rgb.RED
