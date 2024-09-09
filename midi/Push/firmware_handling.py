# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push/firmware_handling.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1307 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import open, range, str
from os import path
VERSION_PREFIX = b'10F4000041444139204E69636F6C6C73'
NUM_VERSION_BYTES = 8
PRESET_FILE_NAME = "Preset.syx"

def get_version_number_from_string(version_string):
    result = 0.0
    if version_string:
        figures = [version_string[i:i + 2] for i in range(0, len(version_string), 2)]
        result = sum([int(fig) * 10 ** (1 - i) for i, fig in enumerate(figures)])
    return result


def get_version_string_from_file_content(content):
    result = None
    if VERSION_PREFIX in content:
        number_start = content.find(VERSION_PREFIX) + len(VERSION_PREFIX)
        if len(content) >= number_start + NUM_VERSION_BYTES:
            result = content[number_start:number_start + NUM_VERSION_BYTES]
        return result


def get_provided_firmware_version():
    result = 0.0
    try:
        mod_path = path.dirname(path.realpath(__file__))
        with open(path.join(mod_path, PRESET_FILE_NAME), "rb") as f:
            version_string = get_version_string_from_file_content(f.read())
            result = get_version_number_from_string(version_string)
    except IOError:
        pass

    return result
