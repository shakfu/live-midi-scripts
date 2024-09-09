# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Launchkey_MK2/BackgroundComponent.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 537 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.BackgroundComponent import BackgroundComponent as BackgroundComponentBase

class BackgroundComponent(BackgroundComponentBase):

    def _clear_control(self, name, control):
        super(BackgroundComponent, self)._clear_control(name, control)
        if control:
            control.add_value_listener(self._on_value_listener)

    def _on_value_listener(self, *a, **k):
        pass
