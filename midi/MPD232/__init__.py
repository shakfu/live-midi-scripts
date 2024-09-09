# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/MPD232/__init__.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 633 bytes
from __future__ import absolute_import, print_function, unicode_literals
import _Framework.Capabilities as caps
from .MPD232 import MPD232

def get_capabilities():
    return {(caps.CONTROLLER_ID_KEY): (caps.controller_id(vendor_id=2536,
                                 product_ids=[54],
                                 model_name="MPD232")), 
     
     (caps.PORTS_KEY): [
                        caps.inport(props=[caps.NOTES_CC, caps.SCRIPT, caps.REMOTE]),
                        caps.outport(props=[caps.NOTES_CC, caps.SCRIPT, caps.REMOTE])]}


def create_instance(c_instance):
    return MPD232(c_instance)
