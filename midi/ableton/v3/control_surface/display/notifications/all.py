# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/ableton/v3/control_surface/display/notifications/all.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 9524 bytes
from __future__ import absolute_import, annotations, print_function, unicode_literals
from typing import NewType
from Live.ClipSlot import ClipSlot as ClipSlot
from ....base import pitch_index_to_string
from ....live import display_name, major_version
from .type_decl import Fn, Notification, _DefaultText, _TransformDefaultText
from .util import toggle_text_generator
SceneName = NewType("SceneName", str)
TrackName = NewType("TrackName", str)
ClipName = NewType("ClipName", str)
DeviceName = NewType("DeviceName", str)
DeviceBank = NewType("DeviceBank", str)
PadName = NewType("PadName", str)
ComponentName = NewType("ComponentName", str)
ModeName = NewType("ModeName", str)
Subdivision = NewType("Subdivision", str)
Resolution = NewType("Resolution", str)
Range = NewType("Range", str)
RangeName = NewType("RangeName", str)

class Notifications:
    identify = lambda: "Live {}\nConnected".format(major_version())
    identify: "Notification"
    full_velocity = toggle_text_generator("Full Velocity\n{}")
    full_velocity: "Notification[Fn[bool]]"
    note_repeat = toggle_text_generator("Note Repeat\n{}")
    note_repeat: "Notification[Fn[bool]]"
    controlled_range = "{}\n{}".format
    controlled_range: "Notification[Fn[RangeName, Range]]"
    generic = "{}".format
    generic: "Notification[Fn[str]]"

    class Element:
        button_lock = lambda name, state: "{}\n{}".format(name.replace("_", " "), "locked" if state else "unlocked")
        button_lock: "Notification[Fn[str, bool]]"

    class Clipboard:
        clear = "Clipboard\ncleared"
        clear: "Notification"

    class UndoRedo:
        undo = "{}".format
        undo: "Notification[Fn[str]]"
        error_undo_no_action = "No Action To Undo"
        error_undo_no_action: "Notification"
        redo = "{}".format
        redo: "Notification[Fn[str]]"
        error_redo_no_action = "No Action To Redo"
        error_redo_no_action: "Notification"

    class Transport:
        metronome = toggle_text_generator("Metronome\n{}")
        metronome: "Notification[Fn[bool]]"
        midi_capture = lambda tempo_set_by_capture, tempo: "Captured\n{} BPM".format(int(tempo)) if tempo_set_by_capture else "Captured"
        midi_capture: "Notification[Fn[bool, float]]"
        loop = toggle_text_generator("Loop\n{}")
        loop: "Notification[Fn[bool]]"
        tap_tempo = lambda tempo: "Tap Tempo\n{}".format(int(tempo))
        tap_tempo: "Notification[Fn[float]]"
        record_quantize = toggle_text_generator("Record Quantize\n{}")
        record_quantize: "Notification[Fn[bool]]"

    class Recording:
        new = "New Clip Slot\nselected"
        new: "Notification"

    class Automation:
        delete = "Automation\ndeleted"
        delete: "Notification"

    class Scene:
        select = "{}\nselected".format
        select: "Notification[Fn[SceneName]]"
        delete = "{}\ndeleted".format
        delete: "Notification[Fn[SceneName]]"
        duplicate = "{}\nduplicated".format
        duplicate: "Notification[Fn[SceneName]]"

    class Track:
        lock = lambda name, state: "{}\n{}".format(name, "locked" if state else "unlocked")
        lock: "Notification[Fn[TrackName, bool]]"
        select = "{}".format
        select: "Notification[Fn[TrackName]]"
        delete = "{}\ndeleted".format
        delete: "Notification[Fn[TrackName]]"
        duplicate = "{}\nduplicated".format
        duplicate: "Notification[Fn[TrackName]]"
        mute = lambda name, state: "{}\n{}".format(name, "muted" if state else "unmuted")
        mute: "Notification[Fn[TrackName, bool]]"
        arm = lambda name, state: "{}\n{}".format(name, "armed" if state else "disarmed")
        arm: "Notification[Fn[TrackName, bool]]"

    class Clip:
        select = "{}\nselected".format
        select: "Notification[Fn[ClipName]]"
        delete = "{}\ndeleted".format
        delete: "Notification[Fn[ClipName]]"
        duplicate = "{}\nduplicated".format
        duplicate: "Notification[Fn[ClipName]]"
        error_delete_empty_slot = "Clip Slot\nalready empty"
        error_delete_empty_slot: "Notification"
        quantize = "{} {}\nquantized".format
        quantize: "Notification[Fn[ClipName, Subdivision]]"
        error_quantize_invalid_resolution = "Cannot quantize to {}".format
        error_quantize_invalid_resolution: "Notification[Fn[Resolution]]"
        double_loop = "Loop\ndoubled"
        double_loop: "Notification"

        class CopyPaste:
            error_copy_from_group_slot = "Cannot copy from Group Slot"
            error_copy_from_group_slot: "Notification"
            error_copy_from_empty_slot = "Cannot copy from empty Slot"
            error_copy_from_empty_slot: "Notification"
            error_copy_recording_clip = "Cannot copy recording Clip"
            error_copy_recording_clip: "Notification"
            copy = lambda slot: "{}\ncopied".format(display_name(slot))
            copy: "Notification[Fn[ClipSlot]]"
            error_paste_to_group_slot = "Cannot paste into Group Slot"
            error_paste_to_group_slot: "Notification"
            error_paste_audio_to_midi = "Cannot paste an audio Clip into a MIDI Track"
            error_paste_audio_to_midi: "Notification"
            error_paste_midi_to_audio = "Cannot paste a MIDI Clip into an audio Track"
            error_paste_midi_to_audio: "Notification"
            paste = lambda slot: "{}\npasted".format(display_name(slot))
            paste: "Notification[Fn[ClipSlot]]"

    class Device:
        lock = lambda name, state: "{}\n{}".format(name, "locked" if state else "unlocked")
        lock: "Notification[Fn[DeviceName, bool]]"
        fold = lambda name, state: "{}\n{}".format(name, "unfolded" if state else "folded")
        fold: "Notification[Fn[DeviceName, str]]"
        on_off = lambda name, state: "{}\n{}".format(name, state.lower())
        on_off: "Notification[Fn[DeviceName, str]]"
        select = "{}".format
        select: "Notification[Fn[DeviceName]]"
        bank = "{}".format
        bank: "Notification[Fn[DeviceBank]]"

    class DrumGroup:

        class Pad:
            select = "{}\nselected".format
            select: "Notification[Fn[PadName]]"
            delete = "{}\ndeleted".format
            delete: "Notification[Fn[PadName]]"
            mute = lambda name, state: "{}\n{}".format(name, "muted" if state else "unmuted")
            mute: "Notification[Fn[PadName]]"
            delete_notes = "{}\nnotes deleted".format
            delete_notes: "Notification[Fn[PadName]]"

            class CopyPaste:
                error_copy_from_empty_pad = "Cannot copy from empty Pad"
                error_copy_from_empty_pad: "Notification"
                copy = "{}\ncopied".format
                copy: "Notification[Fn[PadName]]"
                error_paste_to_source_pad = "Cannot paste to source Pad"
                error_paste_to_source_pad: "Notification"
                paste = "{}\npasted".format
                paste: "Notification[Fn[PadName]]"

        class Page:
            up = "Page up"
            up: "Notification"
            down = "Page down"
            down: "Notification"

        class Scroll:
            up = "Scroll up"
            up: "Notification"
            down = "Scroll down"
            down: "Notification"

    class Simpler:

        class Slice:
            select = "Slice {}\nselected".format
            select: "Notification[Fn[int]]"
            delete = "Slice {}\ndeleted".format
            delete: "Notification[Fn[int]]"
            delete_notes = "Slice {}\nnotes deleted".format
            delete_notes: "Notification[Fn[int]]"

        class Page:
            up = "Page up"
            up: "Notification"
            down = "Page down"
            down: "Notification"

        class Scroll:
            up = "Scroll up"
            up: "Notification"
            down = "Scroll down"
            down: "Notification"

    class Notes:
        delete = "Notes\ndeleted"
        delete: "Notification"
        error_no_notes_to_delete = "No notes\nto delete"
        error_no_notes_to_delete: "Notification"
        nudge = "Notes nudged to\n{}".format
        nudge: "Notification[Fn[str]]"

        class CopyPaste:
            copy = "Notes\ncopied"
            copy: "Notification"
            paste = "Notes\npasted"
            paste: "Notification"

        class Pitch:
            select = lambda index: "Pitch {}\nselected".format(pitch_index_to_string(index))
            select: "Notification[Fn[int]]"
            delete = lambda index: "{}\nnotes deleted".format(pitch_index_to_string(index))
            delete: "Notification[Fn[int]]"

        class Octave:
            up = "Octave up"
            up: "Notification"
            down = "Octave down"
            down: "Notification"

        class ScaleDegree:
            up = "Scale degree\nup"
            up: "Notification"
            down = "Scale degree\ndown"
            down: "Notification"

    class Sequence:
        current_bar = "Bar {}".format
        current_bar: "Notification[Fn[int]]"
        current_bar_with_page = "Bar {} Page {}".format
        current_bar_with_page: "Notification[Fn[int, int]]"

    class Modes:
        select = None
        select: "Notification[Fn[ComponentName, ModeName]]"

    class DefaultText(_DefaultText):
        pass

    class TransformDefaultText(_TransformDefaultText):
        pass
