# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/KeyLab_mkII/__init__.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 885 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, REMOTE, SCRIPT, controller_id, inport, outport
from .keylab_mkii import KeyLabMkII

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=7285,
                          product_ids=[
                         587, 651, 715],
                          model_name=[
                         "KeyLab mkII 49", "KeyLab mkII 61", "KeyLab mkII 88"])), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC, REMOTE]),
                 inport(props=[NOTES_CC, SCRIPT, REMOTE]),
                 outport(props=[]),
                 outport(props=[SCRIPT])]}


def create_instance(c_instance):
    return KeyLabMkII(c_instance=c_instance)
