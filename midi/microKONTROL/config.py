# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/microKONTROL/config.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 4941 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .consts import *
TRANSPORT_CONTROLS = {
  'STOP': GENERIC_STOP,
  'PLAY': GENERIC_PLAY,
  'REC': GENERIC_REC,
  'LOOP': GENERIC_LOOP,
  'RWD': GENERIC_RWD,
  'FFWD': GENERIC_FFWD}
DEVICE_CONTROLS = (
 (
  GENERIC_ENC1, 0),
 (
  GENERIC_ENC2, 1),
 (
  GENERIC_ENC3, 2),
 (
  GENERIC_ENC4, 3),
 (
  GENERIC_ENC5, 4),
 (
  GENERIC_ENC6, 5),
 (
  GENERIC_ENC7, 6),
 (
  GENERIC_ENC8, 7))
VOLUME_CONTROLS = (
 (
  GENERIC_SLI1, 0),
 (
  GENERIC_SLI2, 1),
 (
  GENERIC_SLI3, 2),
 (
  GENERIC_SLI4, 3),
 (
  GENERIC_SLI5, 4),
 (
  GENERIC_SLI6, 5),
 (
  GENERIC_SLI7, 6),
 (
  GENERIC_SLI8, 7))
TRACKARM_CONTROLS = (
 GENERIC_BUT1,
 GENERIC_BUT2,
 GENERIC_BUT3,
 GENERIC_BUT4,
 GENERIC_BUT5,
 GENERIC_BUT6,
 GENERIC_BUT7,
 GENERIC_BUT8)
BANK_CONTROLS = {
  'TOGGLELOCK': GENERIC_BUT9,
  'BANKDIAL': -1,
  'NEXTBANK': GENERIC_PAD5,
  'PREVBANK': GENERIC_PAD1,
  'BANK1': (47, 1),
  'BANK2': (46, 8),
  'BANK3': (45, 8),
  'BANK4': (44, 8),
  'BANK5': (85, 8),
  'BANK6': (86, 8),
  'BANK7': (87, 8),
  'BANK8': (88, 8)}
PAD_TRANSLATION = ((0, 0, 61, 9), (1, 0, 69, 9), (2, 0, 65, 9), (3, 0, 63, 9), (0, 1, 60, 9),
                   (1, 1, 59, 9), (2, 1, 57, 9), (3, 1, 55, 9), (0, 2, 49, 9), (1, 2, 51, 9),
                   (2, 2, 68, 9), (3, 2, 56, 9), (0, 3, 48, 9), (1, 3, 52, 9), (2, 3, 54, 9),
                   (3, 3, 58, 9))
CONTROLLER_DESCRIPTIONS = {
  'INPUTPORT': "microKONTROL (PORT B)",
  'OUTPUTPORT': "microKONTROL (CTRL)",
  'CHANNEL': 8,
  'PAD_TRANSLATION': PAD_TRANSLATION}
MIXER_OPTIONS = {
  'NUMSENDS': 2,
  'SEND1': (-1, -1, -1, -1, -1, -1, -1, -1),
  'SEND2': (-1, -1, -1, -1, -1, -1, -1, -1),
  'MASTERVOLUME': -1}
