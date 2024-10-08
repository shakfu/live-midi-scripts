# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/APC20/BackgroundComponent.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 595 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.BackgroundComponent import BackgroundComponent as BackgroundComponentBase
from _Framework.Util import nop

class BackgroundComponent(BackgroundComponentBase):

    def _clear_control(self, name, control):
        if control:
            control.add_value_listener(nop)
        elif name in self._control_map:
            self._control_map[name].remove_value_listener(nop)
        super(BackgroundComponent, self)._clear_control(name, control)
