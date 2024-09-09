# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/display/type_decl.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1109 bytes
from __future__ import absolute_import, print_function, unicode_literals
from typing import Any, Callable, NamedTuple, TypeVar
from .state import State

class Event(NamedTuple):
    name: str
    origin: Any
    value: Any


INIT_EVENT = Event(name="init", origin=None, value=None)
DISCONNECT_EVENT = Event(name="disconnect", origin=None, value=None)
ContentType = TypeVar("ContentType")
Render = Callable[([State], ContentType)]
