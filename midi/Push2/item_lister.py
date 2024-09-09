# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/item_lister.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1259 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import ItemListerComponent as ItemListerComponentBase
from ableton.v2.control_surface.components import ItemSlot, SimpleItemSlot

class IconItemSlot(SimpleItemSlot):

    def __init__(self, icon='', *a, **k):
        (super(IconItemSlot, self).__init__)(*a, **k)
        self._icon = icon

    @property
    def icon(self):
        return self._icon


class ItemListerComponent(ItemListerComponentBase):

    def _create_slot(self, index, item, nesting_level):
        items = self._item_provider.items[self.item_offset:]
        num_slots = min(self._num_visible_items, len(items))
        slot = None
        if index == 0 and self.can_scroll_left():
            slot = IconItemSlot(icon="page_left.svg")
            slot.is_scrolling_indicator = True
        elif index == num_slots - 1 and self.can_scroll_right():
            slot = IconItemSlot(icon="page_right.svg")
            slot.is_scrolling_indicator = True
        else:
            slot = ItemSlot(item=item, nesting_level=nesting_level)
            slot.is_scrolling_indicator = False
        return slot
