# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/novation/session_navigation.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 969 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import SessionNavigationComponent as SessionNavigationComponentBase
from .util import skin_scroll_buttons

class SessionNavigationComponent(SessionNavigationComponentBase):

    def __init__(self, *a, **k):
        (super(SessionNavigationComponent, self).__init__)(*a, **k)
        skin_scroll_buttons(self._vertical_banking, "Session.Navigation", "Session.NavigationPressed")
        skin_scroll_buttons(self._horizontal_banking, "Session.Navigation", "Session.NavigationPressed")
        skin_scroll_buttons(self._vertical_paginator, "Session.Navigation", "Session.NavigationPressed")
        skin_scroll_buttons(self._horizontal_paginator, "Session.Navigation", "Session.NavigationPressed")
