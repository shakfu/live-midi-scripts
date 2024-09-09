# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Novation_Impulse/__init__.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1163 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .Novation_Impulse import Novation_Impulse

def create_instance(c_instance):
    return Novation_Impulse(c_instance)


from _Framework.Capabilities import *

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=4661,
                          product_ids=[25],
                          model_name="Impulse 25")), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC, REMOTE, SCRIPT]),
                 inport(props=[NOTES_CC, REMOTE]),
                 outport(props=[NOTES_CC, REMOTE, SCRIPT])]}
