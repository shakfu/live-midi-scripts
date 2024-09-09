# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/ableton/v3/control_surface/components/zoom.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 3648 bytes
from __future__ import absolute_import, print_function, unicode_literals
from Live.Application import Application as Application
from .. import Component
from . import Scrollable, ScrollComponent
NavDirection = Application.View.NavDirection

class ZoomScroller(ScrollComponent, Scrollable):

    def __init__(self, arrangement_only, vertical=True, zoom_all_tracks=False, *a, **k):
        (super().__init__)(
 self, *a, scroll_skin_name="Zoom.{}".format("Vertical" if vertical else "Horizontal"), **k)
        self._arrangement_only = arrangement_only
        self._is_vertical = vertical
        self._zoom_all_tracks = zoom_all_tracks

    def can_scroll_up(self):
        return True

    def can_scroll_down(self):
        return True

    def scroll_up(self):
        self.application.view.zoom_view(NavDirection.up if self._is_vertical else NavDirection.left, self._view_name, self._zoom_all_tracks)

    def scroll_down(self):
        self.application.view.zoom_view(NavDirection.down if self._is_vertical else NavDirection.right, self._view_name, self._zoom_all_tracks)

    @property
    def _view_name(self):
        if self._arrangement_only:
            return "Arranger"
        return self.application.view.focused_document_view


class ZoomComponent(Component):

    def __init__(self, name='Zoom', arrangement_only=False, zoom_all_tracks=False, *a, **k):
        (super().__init__)(a, name=name, **k)
        view_name = "Arranger" if arrangement_only else ""
        (self._vertical_zoom, self._horizontal_zoom) = self.add_children(ZoomScroller(view_name, zoom_all_tracks=zoom_all_tracks), ZoomScroller(view_name, vertical=False))

    def set_vertical_zoom_encoder(self, encoder):
        self._vertical_zoom.set_scroll_encoder(encoder)

    def set_vertical_zoom_in_button(self, button):
        self._vertical_zoom.set_scroll_down_button(button)

    def set_vertical_zoom_out_button(self, button):
        self._vertical_zoom.set_scroll_up_button(button)

    def set_horizontal_zoom_encoder(self, encoder):
        self._horizontal_zoom.set_scroll_encoder(encoder)

    def set_horizontal_zoom_in_button(self, button):
        self._horizontal_zoom.set_scroll_down_button(button)

    def set_horizontal_zoom_out_button(self, button):
        self._horizontal_zoom.set_scroll_up_button(button)
