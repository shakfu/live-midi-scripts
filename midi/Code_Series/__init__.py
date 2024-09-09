# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Code_Series/__init__.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 959 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, REMOTE, SCRIPT, controller_id, inport, outport
from .code import Code

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=1891,
                          product_ids=[
                         12548, 12549, 12550],
                          model_name=[
                         "Code 25", "Code 49", "Code 61"])), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC, REMOTE]),
                 inport(props=[]),
                 inport(props=[NOTES_CC, SCRIPT]),
                 inport(props=[]),
                 outport(props=[]),
                 outport(props=[]),
                 outport(props=[SCRIPT]),
                 outport(props=[])]}


def create_instance(c_instance):
    return Code(c_instance=c_instance)
