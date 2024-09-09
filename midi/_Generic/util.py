# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Generic/util.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1644 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.SubjectSlot import SlotManager, subject_slot
from _Framework.Util import nop

class DeviceAppointer(SlotManager):

    def __init__(self, song=None, appointed_device_setter=nop, *a, **k):
        (super(DeviceAppointer, self).__init__)(*a, **k)
        self._set_appointed_device = appointed_device_setter
        self._appointed_device = None
        self._song = song
        self._DeviceAppointer__on_appointed_device_changed.subject = self._song
        self._DeviceAppointer__on_selected_track_changed.subject = self._song.view
        self._DeviceAppointer__on_selected_track_changed()

    @subject_slot("appointed_device")
    def __on_appointed_device_changed(self):
        if self._appointed_device != self._song.appointed_device:
            self._update_appointed_device(self._song.appointed_device)

    @subject_slot("selected_device")
    def __on_selected_device_changed(self):
        song = self._song
        device = song.view.selected_track.view.selected_device
        if device != None:
            self._update_appointed_device(device)

    @subject_slot("selected_track")
    def __on_selected_track_changed(self):
        track_view = self._song.view.selected_track.view
        self._DeviceAppointer__on_selected_device_changed.subject = track_view
        self._update_appointed_device(track_view.selected_device)

    def _update_appointed_device(self, device):
        if device != None:
            self._appointed_device = device
            self._set_appointed_device(device)
            self._song.appointed_device = device
