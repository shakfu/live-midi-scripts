# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Akai_Force_MPC/sysex.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 600 bytes
from __future__ import absolute_import, print_function, unicode_literals
SYSEX_MSG_HEADER = (240, 71, 0)
SYSEX_END_BYTE = 247
MPC_X_PRODUCT_ID = 58
MPC_LIVE_PRODUCT_ID = 59
FORCE_PRODUCT_ID = 64
SUPPORTED_PRODUCT_IDS = (MPC_LIVE_PRODUCT_ID, MPC_X_PRODUCT_ID, FORCE_PRODUCT_ID)
BROADCAST_ID = 127
PING_MSG_TYPE = 0
PONG_MSG_TYPE = 1
TEXT_MSG_TYPE = 16
COLOR_MSG_TYPE = 17
PING_MSG = SYSEX_MSG_HEADER + (BROADCAST_ID, PING_MSG_TYPE, SYSEX_END_BYTE)
INNER_MESSAGE_MAX_LENGTH = 251
NUM_MSG_IDENTIFYING_BYTES = 3
