# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Hammer_88_Pro/__init__.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 868 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, REMOTE, SCRIPT, controller_id, inport, outport
from .hammer_88_pro import Hammer_88_Pro

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=1891,
                          product_ids=[60],
                          model_name=["Hammer 88 Pro"])), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC, REMOTE]),
                 inport(props=[]),
                 inport(props=[NOTES_CC, SCRIPT]),
                 outport(props=[]),
                 outport(props=[]),
                 outport(props=[SCRIPT])]}


def create_instance(c_instance):
    return Hammer_88_Pro(c_instance=c_instance)
