# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/_MxDCore/TupleWrapper.py
# Compiled at: 2024-07-08 19:27:51
# Size of source mod 2**32: 1821 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import old_hasattr

class TupleWrapper:
    _tuple_wrapper_registry = {}

    @staticmethod
    def forget_tuple_wrapper_instances():
        TupleWrapper._tuple_wrapper_registry = {}

    @staticmethod
    def get_tuple_wrapper(parent, attribute, element_filter=None, element_transform=None):
        if (parent, attribute) not in TupleWrapper._tuple_wrapper_registry:
            TupleWrapper._tuple_wrapper_registry[(parent, attribute)] = TupleWrapper(parent, attribute, element_filter, element_transform)
        return TupleWrapper._tuple_wrapper_registry[(parent, attribute)]

    def __init__(self, parent, attribute, element_filter=None, element_transform=None):
        self._parent = parent
        self._attribute = attribute
        self._element_filter = element_filter
        self._element_transform = element_transform

    def get_list(self):
        result = ()
        parent = self._parent
        if isinstance(parent, dict):
            if self._attribute in list(parent.keys()):
                result = parent[self._attribute]
        elif old_hasattr(parent, self._attribute):
            result = getattr(parent, self._attribute)
        filtered_result = [e if self._element_filter(e) else None for e in result] if self._element_filter else result
        if self._element_transform:
            return list(map(self._element_transform, filtered_result))
        return filtered_result
