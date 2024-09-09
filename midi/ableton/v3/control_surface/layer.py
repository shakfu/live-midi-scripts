# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/ableton/v3/control_surface/layer.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 695 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import Layer as LayerBaseClass

class Layer(LayerBaseClass):

    def on_received(self, client, *a, **k):
        (super().on_received)(client, *a, **k)
        client.num_layers += 1

    def on_lost(self, client):
        super().on_lost(client)
        client.num_layers -= 1
