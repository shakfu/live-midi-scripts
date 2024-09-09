# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/ableton/v3/control_surface/components/accent.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1865 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ...base import depends, listenable_property
from .. import Component
from ..controls import ToggleButtonControl
from ..display import Renderable

class AccentComponent(Component, Renderable):
    accent_button = ToggleButtonControl(color="Accent.Off", on_color="Accent.On")

    @depends(full_velocity=None)
    def __init__(self, name='Accent', full_velocity=None, *a, **k):
        (super().__init__)(a, name=name, **k)
        self._full_velocity = full_velocity
        self.accent_button.connect_property(self, "activated")

    @listenable_property
    def activated(self):
        return self._full_velocity.enabled

    @activated.setter
    def activated(self, state):
        if state != self._full_velocity.enabled:
            self._full_velocity.enabled = state
            self.notify(self.notifications.full_velocity, state)
            self.notify_activated()

    @accent_button.released_delayed
    def accent_button(self, _):
        self.activated = False

    def update(self):
        super().update()
        if self._full_velocity.enabled != self.accent_button.is_on:
            self._full_velocity.enabled = self.accent_button.is_on
