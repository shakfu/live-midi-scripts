# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Push/with_priority.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 622 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import DEFAULT_PRIORITY
from ableton.v2.control_surface.elements import WrapperElement

class WithPriority(WrapperElement):

    def __init__(self, wrapped_priority=DEFAULT_PRIORITY, *a, **k):
        (super(WithPriority, self).__init__)(*a, **k)
        self.wrapped_priority = wrapped_priority
        self.register_control_element(self.wrapped_control)

    def get_control_element_priority(self, element, priority):
        return self.wrapped_priority
