# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Launchkey_Mini_MK4/__init__.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1247 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, SCRIPT, SYNC, controller_id, inport, outport
from Launchkey_MK4.__init__ import LaunchkeyCommonControlSurface, create_launchkey_specification, midi
from .elements import Elements
from .mappings import create_mappings

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=4661,
                          product_ids=[
                         321, 322],
                          model_name=[
                         "Launchkey Mini MK4 25", "Launchkey Mini MK4 37"])), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC]),
                 inport(props=[NOTES_CC, SCRIPT]),
                 outport(props=[]),
                 outport(props=[NOTES_CC, SYNC, SCRIPT])]}


def create_instance(c_instance):
    return Launchkey_Mini_MK4(specification=(create_launchkey_specification(Elements, create_mappings, midi.MINI_MK4_SYSEX_HEADER)),
      c_instance=c_instance)


class Launchkey_Mini_MK4(LaunchkeyCommonControlSurface):
    pass
