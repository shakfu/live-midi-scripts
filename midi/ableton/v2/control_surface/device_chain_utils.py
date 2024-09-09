# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/device_chain_utils.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1446 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import map
from functools import partial
from itertools import chain
import Live
from ..base import find_if, liveobj_valid

def find_instrument_devices(track_or_chain):
    if liveobj_valid(track_or_chain):
        instrument = find_if((lambda d: d.type == Live.Device.DeviceType.instrument), track_or_chain.devices)
        if liveobj_valid(instrument):
            if not instrument.can_have_drum_pads:
                if instrument.can_have_chains:
                    return chain([
                     instrument], *map(find_instrument_devices, instrument.chains))
                return [
                 instrument]
        return []


def find_instrument_meeting_requirement(requirement, track_or_chain):
    if liveobj_valid(track_or_chain):
        instrument = find_if((lambda d: d.type == Live.Device.DeviceType.instrument), track_or_chain.devices)
        if liveobj_valid(instrument):
            if requirement(instrument):
                return instrument
            if instrument.can_have_chains:
                recursive_call = partial(find_instrument_meeting_requirement, requirement)
                return find_if(bool, map(recursive_call, instrument.chains))
