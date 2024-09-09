# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK4/session.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 3170 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.base import depends
from ableton.v3.control_surface.components import ClipSlotComponent as ClipSlotComponentBase
from ableton.v3.control_surface.components import SessionComponent as SessionComponentBase
from ableton.v3.control_surface.components import create_sequencer_clip
from ableton.v3.live import action, find_parent_track, liveobj_valid

def get_clip_for_slot(slot):
    if liveobj_valid(slot):
        track = find_parent_track(slot)
        if track.has_midi_input:
            if slot.has_clip:
                return slot.clip
            return create_sequencer_clip(track, slot=slot)


class ClipSlotComponent(ClipSlotComponentBase):

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self.is_selecting = False

    def _on_launch_button_pressed(self):
        if self.is_selecting:
            self.parent.parent.select_slot(self._clip_slot)
        else:
            super()._on_launch_button_pressed()

    def _feedback_value(self, track, slot_or_clip):
        value = super()._feedback_value(track, slot_or_clip)
        if self.is_selecting:
            is_midi = find_parent_track(slot_or_clip).has_midi_input
            if self._has_clip() or getattr(slot_or_clip, "controls_other_clips", False):
                value = "Session.SequencerClip" if is_midi else "Session.ClipStopped"
            else:
                value = "Session.SequencerSlot" if is_midi else "Session.Slot"
        return value


class SessionComponent(SessionComponentBase):
    __events__ = ('clip_selected', )

    @depends(sequencer_clip=None)
    def __init__(self, sequencer_clip=None, *a, **k):
        (super().__init__)(a, clip_slot_component_type=ClipSlotComponent, **k)
        self._sequencer_clip = sequencer_clip

    def set_clip_select_buttons(self, buttons):
        is_selecting = bool(buttons)
        for scene in self._scenes:
            for x in range(self._session_ring.num_tracks):
                scene.clip_slot(x).is_selecting = is_selecting

        super().set_clip_launch_buttons(buttons)

    def select_slot(self, slot):
        clip = get_clip_for_slot(slot)
        self._sequencer_clip.set_clip(clip)
        if clip:
            action.select(slot)
            self.notify_clip_selected()
