# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/display/renderable.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 6039 bytes
from __future__ import absolute_import, annotations, print_function, unicode_literals
import inspect
from typing import TYPE_CHECKING, Callable, Optional, Type
from ...base import CompoundDisconnectable, EventObject, EventObjectMeta, const, depends, lazy_attribute, nop
from .notifications import Notifications
from notifications.type_decl import NOTIFICATION_EVENT_ID, Notification, NotificationParams
from .state import State
from .type_decl import Event
if TYPE_CHECKING:
    from typing_extensions import Unpack

def collect_properties(cls):
    return (name for cls in inspect.getmro(cls))


class Renderable(CompoundDisconnectable):
    control_base_type = type(object)
    include_in_top_level_state = True

    @depends(react=(const(None)),
      notifications=(const(None)),
      suppress_notifications=(const(None)))
    def __init__(self, react=None, notifications=None, suppress_notifications=None, *a, **k):
        (super().__init__)(*a, **k)
        self._react = react or nop
        self._suppress_notifications = suppress_notifications or nop
        self.notifications = notifications if notifications is not None else Notifications

    @lazy_attribute
    def renderable_state(self):
        renderable_state = State()
        self._init_state_from_listenable_properties(renderable_state)
        self._init_state_from_controls(renderable_state)
        return renderable_state

    def notify(self, notification: "Notification[Callable[[Unpack[NotificationParams]], Optional[str]]]", *a: "Unpack[NotificationParams]"):
        if notification is not None:
            data = notification(*a) if callable(notification) else notification
            if data is not None:
                self.dispatch_event(NOTIFICATION_EVENT_ID, data)

    def suppress_notifications(self):
        self._suppress_notifications()

    def _init_state_from_listenable_properties(self, renderable_state):
        if isinstance(self, EventObject):
            for property_name in collect_properties(self.__class__):
                setattr(renderable_state, property_name, getattr(self, property_name))
                self.register_slot(self, self._create_event_handler(property_name), property_name)

    def _init_state_from_controls(self, renderable_state):
        if hasattr(self, "_control_states"):
            for cls in reversed(inspect.getmro(self.__class__)):
                for (name, value) in vars(cls).items():
                    if isinstance(value, self.control_base_type):
                        control_state = getattr(value, "_get_state")(self)
                        if isinstance(control_state, Renderable):
                            setattr(renderable_state, name, control_state.renderable_state)

    def dispatch_event(self, name: "str", value):
        self._react(Event(name=name, origin=self, value=value))

    def _create_event_handler(self, property_name):

        def on_event(*_):
            property_value = getattr(self, property_name)
            setattr(self.renderable_state, property_name, property_value.renderable_state if isinstance(property_value, Renderable) else property_value)
            self._react(Event(name=property_name, origin=self, value=property_value))

        return on_event
