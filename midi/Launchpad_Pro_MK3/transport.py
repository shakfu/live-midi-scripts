# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Pro_MK3/transport.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 783 bytes
from __future__ import absolute_import, print_function, unicode_literals
from novation.blinking_button import BlinkingButtonControl
from novation.transport import TransportComponent as TransportComponentBase

class TransportComponent(TransportComponentBase):
    capture_midi_button = BlinkingButtonControl(color="Transport.CaptureOff",
      blink_on_color="Transport.CaptureOn",
      blink_off_color="Transport.CaptureOff")

    @capture_midi_button.pressed
    def capture_midi_button(self, _):
        try:
            if self.song.can_capture_midi:
                self.song.capture_midi()
                self.capture_midi_button.start_blinking()
        except RuntimeError:
            pass
