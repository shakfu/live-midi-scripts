# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/KeyLab_mk3/mappings.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 2361 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.mode import ImmediateBehaviour

def create_mappings(_):
    mappings = {}
    mappings["Transport"] = dict(play_button="play_button",
      stop_button="stop_button",
      metronome_button="metronome_button",
      loop_button="loop_button",
      tap_tempo_button="tap_button",
      rewind_button="rewind_button",
      fastforward_button="fastforward_button",
      capture_midi_button="save_button")
    mappings["View_Based_Recording"] = dict(record_button="record_button")
    mappings["Undo_Redo"] = dict(undo_button="undo_button", redo_button="redo_button")
    mappings["Clip_Actions"] = dict(quantize_button="quantize_button")
    mappings["View_Control"] = dict(prev_scene_button="context_button_2",
      next_scene_button="context_button_3",
      track_encoder="display_encoder")
    mappings["Mixer"] = dict(target_track_mute_button="context_button_4",
      target_track_solo_button="context_button_5",
      target_track_arm_button="context_button_6",
      target_track_volume_control="fader_8",
      target_track_pan_control="encoder_8")
    mappings["Session"] = dict(clip_launch_buttons="pads")
    mappings["Scene_Launch"] = dict(launch_button="context_button_7")
    mappings["Active_Parameter"] = dict(touch_controls="parameter_touch_elements")
    mappings["Mode_Buttons"] = dict(device_button="context_button_0",
      mixer_button="context_button_1")
    mappings["Continuous_Control_Modes"] = dict(device_button="context_button_0",
      mixer_button="context_button_1",
      device=dict(modes=[
     dict(component="Device", parameter_controls="continuous_controls"),
     dict(component="Device_Navigation",
       scroll_encoder="display_encoder_with_context_button_0")]),
      mixer=dict(component="Mixer",
      volume_controls="faders",
      pan_controls="encoders",
      track_bank_encoder="display_encoder_with_context_button_1"),
      default_behaviour=(ImmediateBehaviour()))
    return mappings
