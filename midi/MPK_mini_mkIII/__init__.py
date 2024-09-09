# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/MPK_mini_mkIII/__init__.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1559 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Generic.GenericScript import GenericScript as GenericScript
from .config import *

def create_instance(c_instance):
    return GenericScript(c_instance, Live.MidiMap.MapMode.absolute, Live.MidiMap.MapMode.absolute, DEVICE_CONTROLS, TRANSPORT_CONTROLS, VOLUME_CONTROLS, TRACKARM_CONTROLS, BANK_CONTROLS, CONTROLLER_DESCRIPTION)


from _Framework.Capabilities import *

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=2536,
                          product_ids=[73],
                          model_name="MPK mini 3")), 
     
     PORTS_KEY: [inport(props=[NOTES_CC, REMOTE, SCRIPT]), outport(props=[SCRIPT])]}
