# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Launchpad_Mini_MK3/notifying_background.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 812 bytes
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial
from ableton.v2.base import nop
from ableton.v2.control_surface.components import BackgroundComponent
from ableton.v2.control_surface.elements import ButtonMatrixElement

class NotifyingBackgroundComponent(BackgroundComponent):
    __events__ = ('value', )

    def register_slot(self, control, *a):
        listener = nop if isinstance(control, ButtonMatrixElement) else partial(self._NotifyingBackgroundComponent__on_control_value, control)
        return super(BackgroundComponent, self).register_slot(control, listener, "value")

    def __on_control_value(self, control, value):
        self.notify_value(control, value)
