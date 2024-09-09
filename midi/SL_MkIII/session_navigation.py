# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/SL_MkIII/session_navigation.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 547 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import SessionNavigationComponent as SessionNavigationComponentBase

class SessionNavigationComponent(SessionNavigationComponentBase):

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._vertical_banking.scroll_up_button.color = "Session.Navigation"
        self._vertical_banking.scroll_down_button.color = "Session.Navigation"
