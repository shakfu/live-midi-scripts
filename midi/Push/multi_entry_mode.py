# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Push/multi_entry_mode.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1060 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.mode import Mode, tomode

class MultiEntryMode(Mode):

    def __init__(self, mode=None, *a, **k):
        (super(MultiEntryMode, self).__init__)(*a, **k)
        self._mode = tomode(mode)
        self._entry_count = 0

    def enter_mode(self):
        if self._entry_count == 0:
            self._mode.enter_mode()
        self._entry_count += 1

    def leave_mode(self):
        if self._entry_count == 1:
            self._mode.leave_mode()
        self._entry_count -= 1

    @property
    def is_entered(self):
        return self._entry_count > 0
