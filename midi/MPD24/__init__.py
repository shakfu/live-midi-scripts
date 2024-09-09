# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/MPD24/__init__.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1617 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Generic.GenericScript import GenericScript as GenericScript
from .config import *

def create_instance(c_instance):
    return GenericScript(c_instance, Live.MidiMap.MapMode.absolute, Live.MidiMap.MapMode.absolute, DEVICE_CONTROLS, TRANSPORT_CONTROLS, VOLUME_CONTROLS, TRACKARM_CONTROLS, BANK_CONTROLS, CONTROLLER_DESCRIPTION)


from _Framework.Capabilities import *

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=2536,
                          product_ids=[104],
                          model_name="Akai MPD24")), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC, REMOTE, SCRIPT]),
                 inport(props=[NOTES_CC]),
                 inport(props=[NOTES_CC]),
                 outport(props=[SCRIPT]),
                 outport(props=[])]}
