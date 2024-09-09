# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/elements/optional.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1136 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ...base import listens
from .combo import ToggleElement

class ChoosingElement(ToggleElement):

    def __init__(self, flag=None, *a, **k):
        (super(ChoosingElement, self).__init__)(*a, **k)
        self._ChoosingElement__on_flag_changed.subject = flag
        self._ChoosingElement__on_flag_changed(flag.value)

    @listens("value")
    def __on_flag_changed(self, value):
        self.set_toggled(value)


class OptionalElement(ChoosingElement):

    def __init__(self, control=None, flag=None, value=None, *a, **k):
        on_control = control if value else None
        off_control = None if value else control
        (super(OptionalElement, self).__init__)(a, on_control=on_control, off_control=off_control, flag=flag, **k)
