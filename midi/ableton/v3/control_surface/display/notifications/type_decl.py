# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/display/notifications/type_decl.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1155 bytes
from __future__ import absolute_import, annotations, print_function, unicode_literals
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Callable, Optional, TypeVar, Union
if TYPE_CHECKING:
    from typing_extensions import ParamSpec, TypeVarTuple
    NotificationParams = TypeVarTuple("NotificationParams")
    NotificationParamSpec = ParamSpec("NotificationParamSpec")
else:
    NotificationParams = TypeVar("NotificationParams")
    NotificationParamSpec = ...

@dataclass
class _TransformDefaultText:
    transform_fn = lambda s: s
    transform_fn: "Callable[[str], str]"


class _DefaultText:
    pass


NotificationFnType = TypeVar("NotificationFnType", bound=Callable)
Notification = Optional[Union[(str, _DefaultText, _TransformDefaultText, NotificationFnType)]]
Fn = Callable[(NotificationParamSpec, Any)]
NOTIFICATION_EVENT_ID = "notification"
