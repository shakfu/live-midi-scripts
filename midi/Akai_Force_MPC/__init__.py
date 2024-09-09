# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Akai_Force_MPC/__init__.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 668 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.capabilities import NOTES_CC, PORTS_KEY, REMOTE, SCRIPT, SUGGESTED_PORT_NAMES_KEY, inport, outport
from .akai_force_mpc import Akai_Force_MPC

def get_capabilities():
    return {SUGGESTED_PORT_NAMES_KEY: ["Akai Network - DAW Control"], 
     PORTS_KEY: [
                 inport(props=[NOTES_CC, SCRIPT, REMOTE]),
                 outport(props=[NOTES_CC, SCRIPT, REMOTE])]}


def create_instance(c_instance):
    return Akai_Force_MPC(c_instance)
