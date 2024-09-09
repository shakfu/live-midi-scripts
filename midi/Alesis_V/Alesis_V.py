# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Alesis_V/Alesis_V.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 1465 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
import Live
from _Framework.ButtonMatrixElement import ButtonMatrixElement as ButtonMatrixElement
from _Framework.ControlSurface import ControlSurface as ControlSurface
from _Framework.DeviceComponent import DeviceComponent as DeviceComponent
from _Framework.EncoderElement import EncoderElement as EncoderElement
from _Framework.InputControlElement import MIDI_CC_TYPE
from _Framework.Layer import Layer as Layer

class Alesis_V(ControlSurface):

    def __init__(self, *a, **k):
        (super(Alesis_V, self).__init__)(*a, **k)
        with self.component_guard():
            encoders = ButtonMatrixElement(rows=[
             [EncoderElement(MIDI_CC_TYPE, 0, (identifier + 20), (Live.MidiMap.MapMode.absolute), name=("Encoder_%d" % identifier)) for identifier in range(4)]])
            device = DeviceComponent(name="Device",
              is_enabled=False,
              layer=Layer(parameter_controls=encoders),
              device_selection_follows_track_selection=True)
            device.set_enabled(True)
            self.set_device_component(device)
