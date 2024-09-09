# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/_Arturia/ScrollComponent.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 821 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Control import EncoderControl
from _Framework.ScrollComponent import ScrollComponent as ScrollComponentBase

class ScrollComponent(ScrollComponentBase):
    scroll_encoder = EncoderControl()

    def set_scroll_encoder(self, encoder):
        self.scroll_encoder.set_control_element(encoder)
        self.update()

    @scroll_encoder.value
    def scroll_encoder(self, value, encoder):
        scroll_step = None
        if value > 0 and self.can_scroll_down():
            scroll_step = self._do_scroll_down
        elif value < 0:
            if self.can_scroll_up():
                scroll_step = self._do_scroll_up
        if scroll_step is not None:
            scroll_step()
