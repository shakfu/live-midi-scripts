# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/ableton/v3/control_surface/display/state.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 3815 bytes
from __future__ import absolute_import, print_function, unicode_literals
from dataclasses import dataclass
from pprint import pformat
from typing import Callable, Optional
from weakref import ref
import Live
from ...base import EventObject, listenable_property

@dataclass
class StateFilters:
    key_filter = lambda k: not k.startswith("_")
    key_filter: Callable
    value_filter = lambda v: v is not None and v != ""
    value_filter: Callable


class State(EventObject):
    notification_visible = listenable_property.managed(False)
    repr_filters = StateFilters()

    def __init__(self):
        super().__init__()
        self._timers = {}

    def disconnect(self):
        super().disconnect()
        for timer in self._timers:
            timer.stop()

        self._timers = None

    def __repr__(self):
        return pformat((self.get_repr_data()), indent=4)

    def set_delayed(self, attr_name: str, value, delay_time: Optional[float]):

        def do_setattr(obj, name, value):
            setattr(obj, name, value)
            getattr(obj, "_timers").pop(name, None)
            self.notification_visible = bool(getattr(obj, "_timers"))

        if delay_time is None:
            do_setattr(self, attr_name, value)
        else:
            _self = ref(self)

            def delayed_setattr():
                if _self():
                    do_setattr(_self(), attr_name, value)

            self._timers[attr_name] = Live.Base.Timer(callback=delayed_setattr,
              interval=(int(delay_time * 1000)),
              start=True)
            self.notification_visible = True

    def get_repr_data(self):
        return State.as_dict(self, self.repr_filters)

    @staticmethod
    def as_dict(instance, state_filters=StateFilters(value_filter=(lambda _: True))):
        if isinstance(instance, dict):
            return instance
        dct = dict(vars(instance))
        keys_to_remove = set()
        for (key, value) in dct.items():
            if not not state_filters.key_filter(key):
                keys_to_remove.add(key)
            if isinstance(value, State):
                dct[key] = State.as_dict(value, state_filters)
            if not state_filters.value_filter(value):
                keys_to_remove.add(key)

        for key in keys_to_remove:
            del dct[key]

        return dct

    def trigger_timers(self, from_test=False):
        for timer in list(self._timers.values()):
            timer.trigger()
