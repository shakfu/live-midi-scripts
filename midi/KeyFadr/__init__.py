# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/KeyFadr/__init__.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 647 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, SCRIPT, controller_id, inport, outport
from .KeyFadr import KeyFadr

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=9901,
                          product_ids=[28150],
                          model_name="Reloop KeyFadr")), 
     
     PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT]), outport(props=[NOTES_CC, SCRIPT])]}


def create_instance(c_instance):
    return KeyFadr(c_instance)
