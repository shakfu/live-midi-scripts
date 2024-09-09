# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Launchkey_MK4/__init__.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 8172 bytes
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial
from ableton.v3.base import const, listens, task
from ableton.v3.control_surface import ControlSurface, ControlSurfaceSpecification, create_skin
from ableton.v3.control_surface.capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, SCRIPT, SYNC, controller_id, inport, outport
from ableton.v3.control_surface.components import DEFAULT_DRUM_TRANSLATION_CHANNEL, MixerComponent
from ableton.v3.live import liveobj_valid
from . import midi
from .auto_arm import AutoArmComponent
from .colors import Rgb
from .cue_point import CuePointComponent
from .display import default_label_content, display_specification
from .drum_group import DrumGroupComponent
from .elements import Elements
from .encoder_touch import EncoderTouchComponent
from .keyboard import KeyboardComponent
from .mappings import create_mappings
from .scale import ScaleComponent
from .session import SessionComponent
from .skin import Skin
from .step_sequence import SequencerClip, StepSequenceComponent
from .transport import TransportComponent
from .zoom import ZoomComponent

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=4661,
                          product_ids=[
                         323, 324, 325, 326],
                          model_name=[
                         "Launchkey MK4 25",
                         "Launchkey MK4 37",
                         "Launchkey MK4 49",
                         "Launchkey MK4 61"])), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC]),
                 inport(props=[NOTES_CC, SCRIPT]),
                 outport(props=[]),
                 outport(props=[NOTES_CC, SYNC, SCRIPT])]}


def create_instance(c_instance):
    return Launchkey_MK4(specification=(create_launchkey_specification(Elements, create_mappings, midi.MK4_SYSEX_HEADER)),
      c_instance=c_instance)


def create_launchkey_specification(elements_type, create_mappings_function, sysex_header):
    return ControlSurfaceSpecification(elements_type=(partial(elements_type, sysex_header)),
      control_surface_skin=create_skin(skin=Skin, colors=Rgb),
      num_tracks=8,
      num_scenes=2,
      include_auto_arming=True,
      link_session_ring_to_track_selection=True,
      feedback_channels=[
     DEFAULT_DRUM_TRANSLATION_CHANNEL],
      playing_feedback_velocity=(Rgb.WHITE.midi_value),
      recording_feedback_velocity=(Rgb.RED.midi_value),
      identity_response_id_bytes=(0, 32, 41, -1, 1, 0, 1),
      sysex_header=sysex_header,
      hello_messages=(
     midi.make_connection_message(sysex_header),
     midi.make_enable_touch_output_message(),
     midi.make_enable_drum_pads_message()),
      goodbye_messages=(
     midi.make_connection_message(sysex_header, connect=False),
     midi.make_enable_drum_pads_message(enable=False),
     midi.make_enable_keyboard_message(enable=True)),
      create_mappings_function=create_mappings_function,
      auto_arm_component_type=AutoArmComponent,
      component_map={'Cue_Point':CuePointComponent, 
     'Drum_Group':DrumGroupComponent, 
     'Encoder_Touch':EncoderTouchComponent, 
     'Keyboard':KeyboardComponent, 
     'Scale':ScaleComponent, 
     'Session':SessionComponent, 
     'Step_Sequence':StepSequenceComponent, 
     'Transport':TransportComponent, 
     'Volume_Mixer':partial(MixerComponent, name="Volume_Mixer"), 
     'Zoom':ZoomComponent},
      display_specification=display_specification)


def pitch_provider_for_track(track, instrument_finder):
    if liveobj_valid(track):
        if track.has_midi_input:
            if liveobj_valid(instrument_finder.drum_group):
                return "Drum_Group"
            return "Keyboard"


class LaunchkeyCommonControlSurface(ControlSurface):

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._enable_main_modes_task = self._tasks.add(task.sequence(task.wait(0.2), task.run(self._enable_main_modes)))
        self._enable_main_modes_task.kill()

    def send_midi(self, midi_bytes):
        self._send_midi(midi_bytes)

    def setup(self):
        super().setup()
        self._LaunchkeyCommonControlSurface__on_main_pad_mode_changed.subject = self.component_map["Main_Pad_Modes"]
        self.register_slot(self.component_map["Daw_Pad_Modes"], self._update_sequencer, "selected_mode")
        self.register_slot(self.component_map["Sequencer_Modes"], self._update_sequencer, "selected_mode")
        self.component_map["Keyboard"].set_note_editor(self.component_map["Step_Sequence"].note_editor)

    def target_track_changed(self, _):
        self._update_sequencer()

    def drum_group_changed(self, _):
        self._update_sequencer()

    def identification_state_changed(self, state):
        if state:
            self.display.display(default_label_content())
            self.component_map["Main_Pad_Modes"].selected_mode = "null_0"
            self.send_midi(midi.make_disable_daw_label_popup(self.specification.sysex_header))
        self._enable_main_modes_task.restart()

    def _enable_main_modes(self):
        state = self._identification.is_identified
        with self.component_guard():
            self.component_map["Main_Encoder_Modes"].selected_mode = "plugin"
            self.component_map["Main_Encoder_Modes"].set_enabled(state)
            self.component_map["Daw_Pad_Modes"].selected_mode = "clip"
            self.component_map["Main_Pad_Modes"].selected_mode = "daw"
            self.component_map["Main_Pad_Modes"].set_enabled(state)
        self.set_can_auto_arm(state)

    def _update_sequencer(self, *_):
        if self.component_map["Main_Pad_Modes"].selected_mode == "daw" and self.component_map["Daw_Pad_Modes"].selected_mode == "sequencer" and self.component_map["Sequencer_Modes"].selected_mode == "default":
            pitch_provider = pitch_provider_for_track(self._target_track.target_track, self.instrument_finder)
            self.component_map["Step_Sequence"].set_pitch_provider(self.component_map[pitch_provider] if pitch_provider else None)
            self._send_midi(midi.make_enable_keyboard_message(enable=(pitch_provider == "Keyboard")))
        else:
            self._send_midi(midi.make_enable_keyboard_message(enable=False))

    @staticmethod
    def _should_include_element_in_background(element):
        return "Keyboard" not in element.name

    @listens("selected_mode")
    def __on_main_pad_mode_changed(self, selected_mode):
        self.set_can_update_controlled_track(selected_mode == "drum")
        self._update_sequencer()

    def _get_additional_dependencies(self):
        sequencer_clip = self.register_disconnectable(SequencerClip(target_track=(self._target_track)))
        return {"sequencer_clip": (const(sequencer_clip))}


class Launchkey_MK4(LaunchkeyCommonControlSurface):

    def on_identified(self, response_bytes):
        super().on_identified(response_bytes)
        has_faders = response_bytes[6] not in midi.SMALL_MODEL_ID_BYTES
        with self.component_guard():
            self.component_map["Fader_Button_Modes"].set_enabled(has_faders)
            self.component_map["Volume_Mixer"].set_enabled(has_faders)
