# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/ableton/v3/control_surface/components/item_list.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 3433 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ...base import EventObject, clamp, listenable_property
from ...live import liveobj_changed, liveobj_valid
from .scroll import Scrollable, ScrollComponent

class ItemProvider(EventObject, Scrollable):

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._items = []
        self._selected_item = None
        self._selected_index = 0

    @property
    def has_valid_selection(self):
        return liveobj_valid(self._selected_item)

    @listenable_property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items
        self._selected_item = items[0] if items else None
        self._selected_index = 0
        self.notify_items()

    @listenable_property
    def selected_item(self):
        return self._selected_item

    @selected_item.setter
    def selected_item(self, item):
        if item in self._items:
            if liveobj_changed(self._selected_item, item):
                self._selected_item = item
                self._update_selected_index()
                self.notify_selected_item()

    @listenable_property
    def selected_index(self):
        return self._selected_index

    @selected_index.setter
    def selected_index(self, index):
        self.selected_item = self._items[clamp(index, 0, len(self._items))]

    def can_scroll_up(self):
        return self.has_valid_selection and self._selected_index > 0

    def can_scroll_down(self):
        return self.has_valid_selection and self._selected_index < len(self._items) - 1

    def scroll_up(self):
        if self.can_scroll_up():
            self.selected_index -= 1

    def scroll_down(self):
        if self.can_scroll_down():
            self.selected_index += 1

    def _update_selected_index(self):
        if self.has_valid_selection:
            self._selected_index = self._items.index(self._selected_item)
        else:
            self._selected_index = 0
        self.notify_selected_index()


class ItemListComponent(ScrollComponent):

    def __init__(self, item_provider=None, *a, **k):
        (super().__init__)(a, scrollable=item_provider or ItemProvider(), **k)
        self._item_provider = self.register_disconnectable(item_provider)
        self.register_slot(item_provider, self.update, "selected_index")
        self.register_slot(item_provider, self.update, "items")

    def set_prev_button(self, button):
        self.set_scroll_up_button(button)

    def set_next_button(self, button):
        self.set_scroll_down_button(button)
