# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/components/step_sequence.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 8998 bytes
from __future__ import absolute_import, print_function, unicode_literals
from Live.Song import Quantization
from ...base import EventObject, depends, listenable_property, listens
from ...live import get_bar_length, liveobj_changed, liveobj_valid, prepare_new_clip_slot, song
from .. import Component
from . import LoopSelectorComponent, NoteEditorComponent, NoteEditorPaginator, PlayheadComponent

def create_sequencer_clip(track, slot=None, length=None):
    length = length or get_bar_length()
    slot = slot or prepare_new_clip_slot(track)
    slot.create_clip(length)
    slot.fire(force_legato=True, launch_quantization=(Quantization.q_no_q))
    song().view.detail_clip = slot.clip
    return slot.clip


class SequencerClip(EventObject):

    @depends(target_track=None)
    def __init__(self, target_track=None, *a, **k):
        (super().__init__)(*a, **k)
        self._clip = None
        self._target_track = target_track
        self._SequencerClip__on_target_clip_changed.subject = target_track
        self._SequencerClip__on_target_clip_changed()

    @listenable_property
    def clip(self):
        return self._clip

    @clip.setter
    def clip(self, clip):
        if liveobj_valid(clip):
            clip = clip if clip.is_midi_clip else None
            if liveobj_changed(clip, self._clip):
                self._clip = clip
                self._SequencerClip__on_looping_changed.subject = self._clip
                self._SequencerClip__on_loop_start_changed.subject = self._clip
                self._SequencerClip__on_loop_end_changed.subject = self._clip
                self._SequencerClip__on_signature_numerator_changed.subject = self._clip
                self._SequencerClip__on_signature_denominator_changed.subject = self._clip
                self.notify_clip()
                self.notify_length()
                self.notify_bar_length()

    @listenable_property
    def length(self):
        if liveobj_valid(self._clip):
            return self._clip.loop_end - self._clip.loop_start
        return 0

    @listenable_property
    def bar_length(self):
        return get_bar_length(clip=(self._clip))

    @property
    def num_bars(self):
        return self.length / self.bar_length

    def create_clip(self, length=None):
        if self._target_track.target_track.has_midi_input:
            self.clip = create_sequencer_clip((self._target_track.target_track),
              length=length)
            return self.clip

    @listens("target_clip")
    def __on_target_clip_changed(self):
        clip = self._target_track.target_clip
        self.clip = clip if (liveobj_valid(clip)) and (clip.is_midi_clip) else None

    @listens("looping")
    def __on_looping_changed(self):
        self.notify_length()

    @listens("loop_start")
    def __on_loop_start_changed(self):
        self.notify_length()

    @listens("loop_end")
    def __on_loop_end_changed(self):
        self.notify_length()

    @listens("signature_numerator")
    def __on_signature_numerator_changed(self):
        self.notify_length()
        self.notify_bar_length()

    @listens("signature_denominator")
    def __on_signature_denominator_changed(self):
        self.notify_length()
        self.notify_bar_length()


class StepSequenceComponent(Component):

    @depends(grid_resolution=None)
    def __init__(self, name='Step_Sequence', grid_resolution=None, note_editor_component_type=None, note_editor_paginator_type=None, loop_selector_component_type=None, playhead_component_type=None, playhead_notes=None, playhead_triplet_notes=None, playhead_channels=None, *a, **k):
        (super().__init__)(a, name=name, **k)
        self._grid_resolution = self.add_children(grid_resolution)
        note_editor_component_type = note_editor_component_type or NoteEditorComponent
        self._note_editor = note_editor_component_type(grid_resolution=(self._grid_resolution),
          parent=self)
        note_editor_paginator_type = note_editor_paginator_type or NoteEditorPaginator
        paginator = note_editor_paginator_type(note_editor=(self._note_editor), parent=self)
        loop_selector_component_type = loop_selector_component_type or LoopSelectorComponent
        self._loop_selector = loop_selector_component_type(paginator=paginator,
          parent=self)
        playhead_component_type = playhead_component_type or PlayheadComponent
        self._playhead = playhead_component_type(notes=playhead_notes,
          triplet_notes=playhead_triplet_notes,
          channels=playhead_channels,
          grid_resolution=(self._grid_resolution),
          paginator=paginator,
          parent=self)

    @property
    def note_editor(self):
        return self._note_editor

    def set_pitch_provider(self, provider):
        self._note_editor.pitch_provider = provider

    def set_step_buttons(self, buttons):
        self._note_editor.set_matrix(buttons)

    def set_note_copy_button(self, button):
        self._note_editor.set_copy_button(button)

    def set_resolution_buttons(self, buttons):
        self._grid_resolution.resolution_buttons.set_control_element(buttons)

    def set_loop_buttons(self, matrix):
        self._loop_selector.set_matrix(matrix)

    def set_loop_delete_button(self, button):
        self._loop_selector.delete_button.set_control_element(button)

    def set_loop_copy_button(self, button):
        self._loop_selector.set_copy_button(button)

    def set_prev_page_button(self, button):
        self._loop_selector.prev_page_button.set_control_element(button)

    def set_next_page_button(self, button):
        self._loop_selector.next_page_button.set_control_element(button)
