# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/_Framework/Disconnectable.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 2393 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object
from .Util import find_if

class Disconnectable(object):

    def disconnect(self):
        pass


class CompoundDisconnectable(Disconnectable):

    def __init__(self, *a, **k):
        (super(CompoundDisconnectable, self).__init__)(*a, **k)
        self._registered_disconnectables = []

    def register_disconnectable(self, slot):
        if slot not in self._registered_disconnectables:
            self._registered_disconnectables.append(slot)
        return slot

    def unregister_disconnectable(self, slot):
        if slot in self._registered_disconnectables:
            self._registered_disconnectables.remove(slot)

    def disconnect_disconnectable(self, slot):
        if slot in self._registered_disconnectables:
            self._registered_disconnectables.remove(slot)
            slot.disconnect()

    def find_disconnectable(self, predicate):
        return find_if(predicate, self._registered_disconnectables)

    def has_disconnectable(self, slot):
        return slot in self._registered_disconnectables

    def disconnect(self):
        for slot in self._registered_disconnectables:
            slot.disconnect()

        self._registered_disconnectables = []
        super(CompoundDisconnectable, self).disconnect()


class disconnectable(object):

    def __init__(self, managed=None, *a, **k):
        (super(disconnectable, self).__init__)(*a, **k)
        self._managed = managed

    def __enter__(self):
        managed = self._managed
        return managed

    def __exit__(self, *a, **k):
        if self._managed is not None:
            self._managed.disconnect()
