# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/_Framework/DrumRackComponent.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 2093 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import filter, map, range
from .ControlSurfaceComponent import ControlSurfaceComponent
from .Dependency import depends
from .Util import product
NUM_PADS_X = 4
NUM_PADS_Y = 4

def _validate_matrix(matrix):
    if matrix.width() > NUM_PADS_X or matrix.height() > NUM_PADS_Y:
        raise RuntimeError("The provided button matrix should not be bigger than %dx%d" % (
         NUM_PADS_X, NUM_PADS_Y))


class DrumRackComponent(ControlSurfaceComponent):

    @depends(set_pad_translations=None, request_rebuild_midi_map=None)
    def __init__(self, set_pad_translations=None, request_rebuild_midi_map=None, *a, **k):
        (super(DrumRackComponent, self).__init__)(*a, **k)
        self._set_pad_translations = set_pad_translations
        self._request_rebuild_midi_map = request_rebuild_midi_map

    def _create_and_set_pad_translations(self, matrix):

        def create_translation_entry(y_x):
            y, x = y_x
            button = matrix.get_button(x, y)
            return (
             x,
             y + NUM_PADS_Y - matrix.height(),
             button.message_identifier() if button is not None else 0,
             button.message_channel() if button is not None else 0)

        translations = list(map(create_translation_entry, product(range(matrix.height()), range(matrix.width()))))
        self._set_pad_translations(tuple(translations))

    def set_pads(self, matrix):
        if matrix is not None:
            _validate_matrix(matrix)
            self._create_and_set_pad_translations(matrix)
            for button in filter(None, matrix):
                button.suppress_script_forwarding = True

        else:
            self._set_pad_translations(None)
        self._request_rebuild_midi_map()
