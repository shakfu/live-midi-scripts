# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/ableton/v3/control_surface/display/event_signal/type_decl.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 498 bytes
from __future__ import absolute_import, print_function, unicode_literals
from typing import Callable, TypeVar
from ..state import State
from ..type_decl import Event
EventSignalDataType = TypeVar("EventSignalDataType")
EventSignalFn = Callable[([State, Event], EventSignalDataType)]
