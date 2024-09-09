# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/profile.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 1775 bytes
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial, wraps
ENABLE_PROFILING = False
if ENABLE_PROFILING:
    import cProfile
    PROFILER = cProfile.Profile()

def profile(fn):
    if ENABLE_PROFILING:

        @wraps(fn)
        def wrapper(self, *a, **k):
            if PROFILER:
                return PROFILER.runcall(partial(fn, self, *a, **k))
            print("Can not profile (%s), it is probably reloaded" % fn.__name__)
            return fn(*a, **k)

        return wrapper
    return fn


def dump(name='default'):
    import pstats
    fname = name + ".profile"
    PROFILER.dump_stats(fname)

    def save_human_data(sort):
        s = pstats.Stats(fname, stream=(open("%s.%s.txt" % (fname, sort), "w")))
        s.sort_stats(sort)
        s.print_stats()

    save_human_data("time")
    save_human_data("cumulative")
