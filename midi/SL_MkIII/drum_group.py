# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/SL_MkIII/drum_group.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 713 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import DrumGroupComponent as DrumGroupComponentBase

class DrumGroupComponent(DrumGroupComponentBase):

    def set_matrix(self, matrix):
        if matrix is None:
            if self.matrix.control_elements is not None:
                for button in self.matrix.control_elements:
                    button.clear_send_cache()
                    button.reset()

        super().set_matrix(matrix)
