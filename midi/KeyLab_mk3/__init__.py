# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/KeyLab_mk3/__init__.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 2305 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface import ControlSurface, ControlSurfaceSpecification, create_skin
from ableton.v3.control_surface.capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, SCRIPT, controller_id, inport, outport
from .active_parameter import ActiveParameterComponent
from .colors import Rgb, Skin
from .display import display_specification
from .elements import Elements
from .mappings import create_mappings
from .midi import CONNECTION_MESSAGE, DISCONNECTION_MESSAGE
from .mixer import MixerComponent
from .mode_buttons import ModeButtonsComponent
from .scene_launch import SceneLaunchComponent

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=7285,
                          product_ids=[
                         590, 654, 718],
                          model_name=[
                         "KeyLab 49 mk3", "KeyLab 61 mk3", "KeyLab 88 mk3"])), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC]),
                 inport(props=[NOTES_CC, SCRIPT]),
                 outport(props=[NOTES_CC]),
                 outport(props=[NOTES_CC, SCRIPT])]}


def create_instance(c_instance):
    return KeyLab_mk3(specification=Specification, c_instance=c_instance)


class Specification(ControlSurfaceSpecification):
    elements_type = Elements
    control_surface_skin = create_skin(skin=Skin, colors=Rgb)
    num_tracks = 4
    num_scenes = 3
    link_session_ring_to_track_selection = True
    link_session_ring_to_scene_selection = True
    include_auto_arming = True
    identity_response_id_bytes = (0, 32, 107, 2, 0, 10)
    create_mappings_function = create_mappings
    hello_messages = (CONNECTION_MESSAGE,)
    goodbye_messages = (DISCONNECTION_MESSAGE,)
    parameter_bank_size = 16
    component_map = {
      'Active_Parameter': ActiveParameterComponent,
      'Mixer': MixerComponent,
      'Mode_Buttons': ModeButtonsComponent,
      'Scene_Launch': SceneLaunchComponent}
    display_specification = display_specification


class KeyLab_mk3(ControlSurface):

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self.set_can_auto_arm(True)
