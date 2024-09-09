# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/ableton/v3/control_surface/display/notifications/util.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 599 bytes
from __future__ import absolute_import, annotations, print_function, unicode_literals
from typing import TYPE_CHECKING, Callable
if TYPE_CHECKING:
    from typing_extensions import LiteralString
else:
    LiteralString = str

def toggle_text_generator(format_string: "LiteralString") -> "Callable[[bool], str]":

    def notification_fn(is_on):
        return format_string.format("on" if is_on else "off")

    return notification_fn
