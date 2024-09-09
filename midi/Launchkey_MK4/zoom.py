# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK4/zoom.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1685 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.components import ZoomComponent as ZoomComponentBase
from .internal_parameter import InternalParameterControl, register_internal_parameter

class ZoomComponent(ZoomComponentBase):
    vertical_zoom_encoder = InternalParameterControl()
    horizontal_zoom_encoder = InternalParameterControl()

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._direction = "In"
        self.vertical_zoom_encoder.parameter = register_internal_parameter(self, "Zoom Vertical", (lambda _: self._direction))
        self.horizontal_zoom_encoder.parameter = register_internal_parameter(self, "Zoom Horizontal", (lambda _: self._direction))

    def set_vertical_zoom_encoder(self, encoder):
        self.vertical_zoom_encoder.set_control_element(encoder)

    def set_horizontal_zoom_encoder(self, encoder):
        self.horizontal_zoom_encoder.set_control_element(encoder)

    @vertical_zoom_encoder.value
    def vertical_zoom_encoder(self, value, _):
        self._do_zoom(value, self._vertical_zoom)

    @horizontal_zoom_encoder.value
    def horizontal_zoom_encoder(self, value, _):
        self._do_zoom(value, self._horizontal_zoom)

    def _do_zoom(self, value, scroller):
        if value < 0:
            self._direction = "Out"
            scroller.scroll_up()
        else:
            self._direction = "In"
            scroller.scroll_down()
