# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/_Framework/CompoundComponent.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 2000 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import map
from .ControlSurfaceComponent import ControlSurfaceComponent

class CompoundComponent(ControlSurfaceComponent):

    def __init__(self, *a, **k):
        (super(CompoundComponent, self).__init__)(*a, **k)
        self._sub_components = []

    def update_all(self):
        self.update()
        for component in self._sub_components:
            component.update_all()

    def register_component(self, component):
        component._set_enabled_recursive(self.is_enabled())
        self._sub_components.append(component)
        return component

    def register_components(self, *a):
        return list(map(self.register_component, a))

    def has_component(self, component):
        return component in self._sub_components

    def set_enabled(self, enable):
        super(CompoundComponent, self).set_enabled(enable)
        for component in self._sub_components:
            component._set_enabled_recursive(self.is_enabled())

    def _set_enabled_recursive(self, enable):
        super(CompoundComponent, self)._set_enabled_recursive(enable)
        for component in self._sub_components:
            component._set_enabled_recursive(self.is_enabled())

    def set_allow_update(self, allow_updates):
        allow = bool(allow_updates)
        if self._allow_updates != allow:
            for component in self._sub_components:
                component.set_allow_update(allow)

            super(CompoundComponent, self).set_allow_update(allow)
