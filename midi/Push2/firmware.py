# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/firmware.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 7368 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import filter, object
import fnmatch, logging, os, re
from collections import namedtuple
from functools import total_ordering
import Live
from ableton.v2.base import find_if, listenable_property, task
from ableton.v2.control_surface import Component
logger = logging.getLogger(__name__)
WELCOME_STATE_TIME = 2.0
FIRMWARE_PATH = os.path.join(os.path.dirname(__file__), "firmware")

@total_ordering
class FirmwareVersion(object):

    def __init__(self, major=0, minor=0, build=0, release_type='unknown', *a, **k):
        (super(FirmwareVersion, self).__init__)(*a, **k)
        self.major = major
        self.minor = minor
        self.build = build
        self.release_type = release_type

    def __cmp__(self, other):
        if other is None:
            return -1
        if self.major == other.major and self.minor == other.minor:
            if self.build == other.build:
                return 0
            if not ((self.major > other.major or self.major) == other.major and self.minor > other.minor) and self.major == other.major:
                if not self.minor == other.minor or self.build > other.build:
                    return 1
                return -1

    def __eq__(self, other):
        return isinstance(other, FirmwareVersion) and self.major == other.major and self.minor == other.minor and self.build == other.build

    def __lt__(self, other):
        return self.major < other.major or self.major == other.major and self.minor < other.minor or self.major == other.major and self.minor == other.minor and self.build < other.build

    def __repr__(self):
        return "<FirmwareVersion %i.%i.%i %s>" % (
         self.major,
         self.minor,
         self.build,
         self.release_type)


_firmware_version_re = "([0-9]+)\\.([0-9]+)\\.([0-9]+)"

def extract_firmware_version(filename, prefix, release_type='unknown'):
    match = re.match("%s%s.*" % (prefix, _firmware_version_re), filename)
    if match:
        return FirmwareVersion(int(match.group(1)), int(match.group(2)), int(match.group(3)), release_type)


FirmwareInfo = namedtuple("FirmwareInfo", ["version", "filename"])

class FirmwareCollector(object):
    STABLE_PREFIX = "app_push2_stable_"
    DEV_PREFIX = "app_push2_dev_"

    def __init__(self, firmware_path=FIRMWARE_PATH, *a, **k):
        (super(FirmwareCollector, self).__init__)(*a, **k)
        self.firmware_path = firmware_path
        self.stable_firmwares = self._collect_firmware_files(self.STABLE_PREFIX, "stable")
        self.dev_firmwares = self._collect_firmware_files(self.DEV_PREFIX, "dev")
        logger.debug("Available stable firmware files %r", self.stable_firmwares)
        logger.debug("Available dev firmware files %r", self.dev_firmwares)

    @property
    def latest_stable_firmware(self):
        if self.stable_firmwares:
            return max((self.stable_firmwares), key=(lambda f: f.version))

    @property
    def latest_dev_firmware(self):
        if self.dev_firmwares:
            return max((self.dev_firmwares), key=(lambda f: f.version))

    def get_release_type(self, version):
        if version in map((lambda f: f.version), self.stable_firmwares):
            return "stable"
        if version in map((lambda f: f.version), self.dev_firmwares):
            return "dev"
        return "unknown"

    def _collect_firmware_files(self, prefix, release_type):
        return list(filter((lambda x: x.version is not None), [FirmwareInfo(extract_firmware_version(f, prefix, release_type), f) for f in os.listdir(FIRMWARE_PATH) if fnmatch.fnmatch(f, "*.upgrade")]))


class FirmwareUpdateComponent(Component):
    state = listenable_property.managed("welcome")

    def __init__(self, *a, **k):
        (super(FirmwareUpdateComponent, self).__init__)(a, is_enabled=False, **k)
        self._firmware = None

    def start(self, firmware):
        logger.info("Start firmware update using %r", firmware.filename)
        self._firmware = firmware
        self.notify_firmware_file()
        self.set_enabled(True)

        def set_state():
            self.state = "start"

        self._tasks.add(task.sequence(task.wait(WELCOME_STATE_TIME), task.run(set_state)))

    def process_firmware_response(self, data):
        entry = find_if((lambda entry: entry["type"] == "firmware"), data)
        if entry:
            self.state = "success" if entry["success"] else "failure"

    @listenable_property
    def firmware_file(self):
        if self._firmware is not None:
            return os.path.join(FIRMWARE_PATH, self._firmware.filename)
        return ""

    @property
    def data_file(self):
        return os.path.join(FIRMWARE_PATH, "FlashData.bin")


class FirmwareSwitcher(object):

    def __init__(self, firmware_collector=None, firmware_update=None, installed_firmware_version=None, *a, **k):
        (super(FirmwareSwitcher, self).__init__)(*a, **k)
        self._installed_version = installed_firmware_version
        self._update = firmware_update
        self._collector = firmware_collector

    @property
    def firmware_to_switch_to(self):
        if self.can_switch_firmware:
            if self._installed_version.release_type == "dev":
                return self._collector.latest_stable_firmware
            return self._collector.latest_dev_firmware

    @property
    def version_to_switch_to(self):
        firmware = self.firmware_to_switch_to
        if firmware is not None:
            return firmware.version

    @property
    def can_switch_firmware(self):
        application = Live.Application.get_application()
        return application.has_option("_Push2DevFirmware") and self._collector.latest_stable_firmware is not None and self._collector.latest_dev_firmware is not None

    def switch_firmware(self):
        if not self.can_switch_firmware:
            raise RuntimeError("Cannot switch firmware")
        self._update.start(self.firmware_to_switch_to)
