# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/APC40_MkII/__init__.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 767 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, REMOTE, SCRIPT, SYNC, controller_id, inport, outport
from .APC40_MkII import APC40_MkII

def create_instance(c_instance):
    return APC40_MkII(c_instance)


def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=2536,
                          product_ids=[
                         41],
                          model_name=[
                         "APC40 mkII", "Akai APC40 MkII"])), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC, SCRIPT, REMOTE]),
                 outport(props=[SYNC, SCRIPT, REMOTE])]}
