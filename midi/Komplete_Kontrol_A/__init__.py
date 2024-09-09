# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Komplete_Kontrol_A/__init__.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 484 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.capabilities import SUGGESTED_PORT_NAMES_KEY
from .komplete_kontrol_a import Komplete_Kontrol_A

def get_capabilities():
    return {SUGGESTED_PORT_NAMES_KEY: ["Komplete Kontrol A DAW", "Komplete Kontrol M DAW"]}


def create_instance(c_instance):
    return Komplete_Kontrol_A(c_instance=c_instance)
