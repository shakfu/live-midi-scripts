# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Roland_FA/navigation.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 591 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import SessionNavigationComponent as SessionNavigationComponentBase
from .scroll import ScrollComponent

class SessionNavigationComponent(SessionNavigationComponentBase):

    def __init__(self, *a, **k):
        (super(SessionNavigationComponent, self).__init__)(*a, **k)
        self._horizontal_paginator = ScrollComponent((self.track_pager_type(self._session_ring)),
          parent=self)
