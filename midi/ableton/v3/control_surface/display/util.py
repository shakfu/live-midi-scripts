# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/ableton/v3/control_surface/display/util.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1957 bytes
from __future__ import absolute_import, print_function, unicode_literals
from typing import List
from ...base import BooleanContext
updating_display = BooleanContext()

def auto_break_lines(text: str, max_width: int, max_lines: int, pad_lines: bool=True) -> List[str]:
    words = [truncate_with_ellipses(word[:max_width]) if len(word) > max_width else word for word in text.split(" ")]
    lines = [
     ""]
    current_width = 0
    for word in words:
        if current_width + len(word) <= max_width:
            str_to_append = " {}".format(word) if current_width != 0 else word
            current_width += len(str_to_append)
            lines[-1] += str_to_append
        else:
            lines.append(word)
            current_width = len(word)

    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = truncate_with_ellipses(lines[-1])
    if pad_lines:
        if len(lines) < max_lines:
            lines += [""] * (max_lines - len(lines))
        return lines


def truncate_with_ellipses(string: str):
    if len(string) > 3:
        return string[:len(string) - 3] + "..."
    return "." * len(string)
