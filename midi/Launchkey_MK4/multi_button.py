# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK4/multi_button.py
# Compiled at: 2024-07-31 03:21:20
# Size of source mod 2**32: 1321 bytes
from ableton.v3.control_surface.elements import ButtonElement

class MultiButtonElement(ButtonElement):

    def __init__(self, *a, **k):
        self._secondary_button = SecondaryButtonElement(
         self, (k.pop("secondary_identifier")), **k)
        (super().__init__)(a, is_private=True, **k)

    def send_value(self, value, force=False, channel=None):
        super().send_value(value, force=force, channel=channel)
        self._secondary_button.send_value(value, force=force, channel=channel)


class SecondaryButtonElement(ButtonElement):

    def __init__(self, parent, *a, **k):
        (super().__init__)(a, is_private=True, **k)
        self._parent = parent

    def receive_value(self, value):
        super().receive_value(value)
        self._parent.receive_value(value)

    def script_wants_forwarding(self):
        return True
