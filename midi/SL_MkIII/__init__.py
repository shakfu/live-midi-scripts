# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/SL_MkIII/__init__.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 920 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, REMOTE, SCRIPT, controller_id, inport, outport
from .sl_mkiii import SLMkIII

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=4661,
                          product_ids=[257],
                          model_name=["Novation SL MkIII"])), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC, REMOTE]),
                 inport(props=[NOTES_CC, SCRIPT, REMOTE]),
                 inport(props=[NOTES_CC, REMOTE]),
                 outport(props=[]),
                 outport(props=[NOTES_CC, SCRIPT]),
                 outport(props=[]),
                 outport(props=[])]}


def create_instance(c_instance):
    return SLMkIII(c_instance=c_instance)
