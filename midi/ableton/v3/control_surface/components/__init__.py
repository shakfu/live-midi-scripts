# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/components/__init__.py
# Compiled at: 2024-08-28 00:56:44
# Size of source mod 2**32: 4332 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .accent import AccentComponent
from .active_parameter import ActiveParameterComponent
from .auto_arm import AutoArmComponent
from .background import BackgroundComponent, ModifierBackgroundComponent, TranslatingBackgroundComponent
from .channel_strip import ChannelStripComponent
from .clip_actions import ClipActionsComponent
from .clip_slot import ClipSlotComponent
from .clipboard import BufferedClipboardComponent, ClipboardComponent
from .device import DeviceComponent
from .device_bank_navigation import DeviceBankNavigationComponent
from .device_navigation import DeviceNavigationComponent
from .device_parameters import DeviceParametersComponent
from .drum_group import DEFAULT_DRUM_TRANSLATION_CHANNEL, DrumGroupComponent, DrumPadClipboardComponent
from .drum_group_scroll import DrumGroupScrollComponent
from .grid_resolution import GRID_RESOLUTIONS, GridResolutionComponent
from .item_list import ItemListComponent, ItemProvider
from .loop_selector import LoopSelectorComponent
from .mixer import MixerComponent, SendIndexManager
from .note_editor import DEFAULT_STEP_TRANSLATION_CHANNEL, NoteEditorComponent, NoteRegionClipboardComponent, PitchProvider
from .page import Pageable, PageComponent
from .paginator import NoteEditorPaginator, Paginator
from .playable import PlayableComponent
from .playhead import PlayheadComponent
from .recording import BasicRecordingMethod, NextSlotRecordingMethod, NextSlotWithOverdubRecordingMethod, RecordingComponent, RecordingMethod, SelectedSlotRecordingMethod, ViewBasedRecordingComponent
from .scene import SceneComponent
from .scroll import Scrollable, ScrollComponent
from .session import ClipSlotClipboardComponent, SessionComponent
from .session_navigation import SessionNavigationComponent
from .session_overview import SessionOverviewComponent
from .session_ring import SessionRingComponent
from .sliced_simpler import DEFAULT_SIMPLER_TRANSLATION_CHANNEL, SlicedSimplerComponent
from .step_sequence import SequencerClip, StepSequenceComponent, create_sequencer_clip
from .target_track import ArmedTargetTrackComponent, TargetTrackComponent
from .transport import TransportComponent
from .undo_redo import UndoRedoComponent
from .view_control import ViewControlComponent
from .view_toggle import ViewToggleComponent
from .zoom import ZoomComponent
__all__ = ('DEFAULT_DRUM_TRANSLATION_CHANNEL', 'DEFAULT_SIMPLER_TRANSLATION_CHANNEL',
           'DEFAULT_STEP_TRANSLATION_CHANNEL', 'GRID_RESOLUTIONS', 'AccentComponent',
           'ActiveParameterComponent', 'ArmedTargetTrackComponent', 'AutoArmComponent',
           'BackgroundComponent', 'BasicRecordingMethod', 'BufferedClipboardComponent',
           'ChannelStripComponent', 'ClipActionsComponent', 'ClipboardComponent',
           'ClipSlotClipboardComponent', 'ClipSlotComponent', 'DeviceBankNavigationComponent',
           'DeviceComponent', 'DeviceNavigationComponent', 'DeviceParametersComponent',
           'DrumGroupComponent', 'DrumGroupScrollComponent', 'DrumPadClipboardComponent',
           'GridResolutionComponent', 'ItemListComponent', 'ItemProvider', 'LoopSelectorComponent',
           'MixerComponent', 'ModifierBackgroundComponent', 'NextSlotRecordingMethod',
           'NextSlotWithOverdubRecordingMethod', 'NoteEditorComponent', 'NoteEditorPaginator',
           'NoteRegionClipboardComponent', 'Pageable', 'PageComponent', 'Paginator',
           'PitchProvider', 'PlayableComponent', 'PlayheadComponent', 'RecordingComponent',
           'RecordingMethod', 'SceneComponent', 'Scrollable', 'ScrollComponent',
           'SelectedSlotRecordingMethod', 'SendIndexManager', 'SequencerClip', 'SessionComponent',
           'SessionNavigationComponent', 'SessionOverviewComponent', 'SessionRingComponent',
           'SlicedSimplerComponent', 'StepSequenceComponent', 'TargetTrackComponent',
           'TranslatingBackgroundComponent', 'TransportComponent', 'UndoRedoComponent',
           'ViewBasedRecordingComponent', 'ViewControlComponent', 'ViewToggleComponent',
           'ZoomComponent', 'create_sequencer_clip')
