# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/KeyLab/SessionComponent.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 374 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Arturia.SessionComponent import SessionComponent as SessionComponentBase

class SessionComponent(SessionComponentBase):

    def set_selected_scene_launch_button(self, button):
        self.selected_scene().set_launch_button(button)
