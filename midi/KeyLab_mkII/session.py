# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_mkII/session.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 514 bytes
from __future__ import absolute_import, print_function, unicode_literals
from KeyLab_Essential.session import SceneComponent as SceneComponentBase
from KeyLab_Essential.session import SessionComponent as SessionComponentBase
from .clip_slot import ClipSlotComponent

class SceneComponent(SceneComponentBase):
    clip_slot_component_type = ClipSlotComponent


class SessionComponent(SessionComponentBase):
    scene_component_type = SceneComponent
