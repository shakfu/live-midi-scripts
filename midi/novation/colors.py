# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/novation/colors.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 5501 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object
from ableton.v2.control_surface.elements import AnimatedColor, Color
BLINK_CHANNEL = 1
PULSE_CHANNEL = 2

class Pulse(AnimatedColor):
    _channel = PULSE_CHANNEL


class Blink(AnimatedColor):
    _channel = BLINK_CHANNEL


class Rgb(object):
    BLACK = Color(0)
    DARK_GREY = Color(1)
    GREY = Color(2)
    WHITE = Color(3)
    WHITE_HALF = Color(1)
    RED = Color(5)
    RED_BLINK = Blink(color1=BLACK, color2=RED)
    RED_PULSE = Pulse(color1=BLACK, color2=RED)
    RED_HALF = Color(7)
    OFF_WHITE = Color(8)
    ORANGE = Color(9)
    ORANGE_HALF = Color(11)
    CREAM = Color(12)
    AMBER = Color(96)
    AMBER_HALF = Color(14)
    DARK_YELLOW = Color(17)
    DARK_YELLOW_HALF = Color(19)
    GREEN = Color(21)
    GREEN_BLINK = Blink(color1=BLACK, color2=GREEN)
    GREEN_PULSE = Pulse(color1=BLACK, color2=GREEN)
    GREEN_HALF = Color(27)
    MINT = Color(29)
    MINT_HALF = Color(31)
    LIGHT_BLUE = Color(37)
    LIGHT_BLUE_HALF = Color(39)
    BLUE = Color(41)
    BLUE_PULSE = Pulse(color1=BLACK, color2=BLUE)
    BLUE_HALF = Color(43)
    DARK_BLUE = Color(49)
    DARK_BLUE_HALF = Color(51)
    VIOLET = Color(52)
    PURPLE = Color(53)
    PURPLE_HALF = Color(55)
    AQUA = Color(77)
    DARK_ORANGE = Color(84)
    PALE_GREEN = Color(87)
    PALE_GREEN_HALF = Color(89)
    YELLOW = Color(97)
    YELLOW_HALF = Color(125)


class Mono(object):
    OFF = Color(0)
    HALF = Color(63)
    ON = Color(127)


CLIP_COLOR_TABLE = {
  10927616: 74,
  16149507: 84,
  4047616: 76,
  6441901: 69,
  14402304: 99,
  8754719: 19,
  16725558: 5,
  3947580: 71,
  10056267: 15,
  8237133: 18,
  12026454: 11,
  12565097: 73,
  13381230: 58,
  12243060: 111,
  16249980: 13,
  13013643: 4,
  10208397: 88,
  695438: 65,
  13821080: 110,
  3101346: 46,
  16749734: 107,
  8962746: 102,
  5538020: 79,
  13684944: 117,
  15064289: 119,
  14183652: 94,
  11442405: 44,
  13408551: 100,
  1090798: 78,
  11096369: 127,
  16753961: 96,
  1769263: 87,
  5480241: 64,
  1698303: 90,
  16773172: 97,
  7491393: 126,
  8940772: 80,
  14837594: 10,
  8912743: 16,
  10060650: 105,
  13872497: 14,
  16753524: 108,
  8092539: 70,
  2319236: 39,
  1716118: 47,
  12349846: 59,
  11481907: 121,
  15029152: 57,
  2490280: 25,
  11119017: 112,
  10701741: 81,
  15597486: 8,
  49071: 77,
  10851765: 93,
  12558270: 48,
  32192: 43,
  8758722: 103,
  10204100: 104,
  11958214: 55,
  8623052: 66,
  16726484: 95,
  12581632: 86,
  13958625: 28,
  12173795: 115,
  13482980: 116,
  16777215: 3,
  6094824: 33,
  13496824: 114,
  9611263: 92,
  9160191: 36}
RGB_COLOR_TABLE = ((0, 0), (1, 1973790), (2, 8355711), (3, 16777215), (4, 16731212),
                   (5, 16711680), (6, 5832704), (7, 1638400), (8, 16760172), (9, 16733184),
                   (10, 5840128), (11, 2562816), (12, 16777036), (13, 16776960),
                   (14, 5855488), (15, 1644800), (16, 8978252), (17, 5570304), (18, 1923328),
                   (19, 1321728), (20, 5046092), (21, 65280), (22, 22784), (23, 6400),
                   (24, 5046110), (25, 65305), (26, 22797), (27, 6402), (28, 5046152),
                   (29, 65365), (30, 22813), (31, 7954), (32, 5046199), (33, 65433),
                   (34, 22837), (35, 6418), (36, 5030911), (37, 43519), (38, 16722),
                   (39, 4121), (40, 5015807), (41, 22015), (42, 7513), (43, 2073),
                   (44, 5000447), (45, 255), (46, 89), (47, 25), (48, 8867071), (49, 5505279),
                   (50, 1638500), (51, 983088), (52, 16731391), (53, 16711935), (54, 5832793),
                   (55, 1638425), (56, 16731271), (57, 16711764), (58, 5832733),
                   (59, 2228243), (60, 16717056), (61, 10040576), (62, 7950592),
                   (63, 4416512), (64, 211200), (65, 22325), (66, 21631), (67, 255),
                   (68, 17743), (69, 2425036), (70, 8355711), (71, 2105376), (72, 16711680),
                   (73, 12451629), (74, 11529478), (75, 6618889), (76, 1084160),
                   (77, 65415), (78, 43519), (79, 11007), (80, 4129023), (81, 7995647),
                   (82, 11672189), (83, 4202752), (84, 16730624), (85, 8970502),
                   (86, 7536405), (87, 65280), (88, 3931942), (89, 5898097), (90, 3735500),
                   (91, 5999359), (92, 3232198), (93, 8880105), (94, 13835775), (95, 16711773),
                   (96, 16744192), (97, 12169216), (98, 9502464), (99, 8609031),
                   (100, 3746560), (101, 1330192), (102, 872504), (103, 1381674),
                   (104, 1450074), (105, 6896668), (106, 11010058), (107, 14569789),
                   (108, 14182940), (109, 16769318), (110, 10412335), (111, 6796559),
                   (112, 1973808), (113, 14483307), (114, 8454077), (115, 10131967),
                   (116, 9332479), (117, 4210752), (118, 7697781), (119, 14745599),
                   (120, 10485760), (121, 3473408), (122, 1757184), (123, 475648),
                   (124, 12169216), (125, 4141312), (126, 11755264), (127, 4920578))
