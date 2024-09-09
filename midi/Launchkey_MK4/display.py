# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: /MIDI Remote Scripts/Launchkey_MK4/display.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 11352 bytes
from __future__ import absolute_import, print_function, unicode_literals
from dataclasses import dataclass
from enum import IntEnum
from functools import partial
from typing import Optional, Tuple
from ableton.v3.control_surface.components.mixer import send_letter_to_index
from ableton.v3.control_surface.display import DefaultNotifications, DisplaySpecification, Text, view
from ableton.v3.live import display_name, find_parent_track, liveobj_name, liveobj_valid, song
DisplayText = partial(Text, max_width=16, justification=(Text.Justification.NONE))

def cancel_temp_screens(elements):
    elements.temp_display_command.cancel()


class Config(IntEnum):
    two_line = 97
    three_line = 98
    two_by_four = 99


@dataclass
class TargetContent:
    config = Config.two_line
    config: Optional[Config]
    lines = ()
    lines: Optional[Tuple[(str, ...)]]
    trigger = False
    trigger: Optional[bool]


@dataclass
class DisplayContent:
    static = None
    static: Optional[TargetContent]
    temp = None
    temp: Optional[TargetContent]
    daw_label = None
    daw_label: Optional[TargetContent]
    mixer_label = None
    mixer_label: Optional[TargetContent]
    encoders = ()
    encoders: Tuple[(Optional[Tuple[(TargetContent, TargetContent)]], ...)]
    faders = ()
    faders: Tuple[(Optional[Tuple[(TargetContent, TargetContent)]], ...)]
    cancel_temp = False
    cancel_temp: Optional[bool]

    @classmethod
    def with_parameters(cls, state, released_encoder_index=None, **k):

        def parameter_header(element):
            if state.main_encoder_modes.selected_mode == "transport":
                if not state.note_settings_modes.selected_mode == "active":
                    return "Transport"
                if liveobj_valid(element.mapped_object.canonical_parent):
                    return liveobj_name(find_parent_track(element.mapped_object))
                return liveobj_name(state.target_track.target_track)

        def parameter_content(elements, is_encoders=False):
            return tuple((TargetContent(config=(Config.three_line), lines=((parameter_header(element), display_name(element.mapped_object), str(element.mapped_object)) if liveobj_valid(element.mapped_object) else ('-',
                                                                                                                                                                                                                      '-',
                                                                                                                                                                                                                      '-')), trigger=(is_encoders and i == released_encoder_index)) for (i, element) in enumerate(elements)))

        return cls(encoders=parameter_content((state.elements.encoders), is_encoders=True), 
         faders=parameter_content(state.elements.faders + [state.elements.master_fader]) if hasattr(state.elements, "faders") else (), **k)


class Notifications(DefaultNotifications):
    controlled_range = DefaultNotifications.DefaultText()
    generic = DefaultNotifications.DefaultText()
    identify = DefaultNotifications.TransformDefaultText(lambda x: "\n{}".format(x.replace("Connected", "")))

    class Track(DefaultNotifications.Track):
        select = "track_select"

    class Device(DefaultNotifications.Device):
        select = "device_select"
        bank = "device_bank_select"

    class Clip(DefaultNotifications.Clip):
        double_loop = DefaultNotifications.DefaultText()

    class Notes(DefaultNotifications.Notes):
        INCLUDE_ALL = True

    class Sequence(DefaultNotifications.Sequence):
        INCLUDE_ALL = True

    class Modes(DefaultNotifications.Modes):
        select = lambda _, mode_name: "mode:{}".format(mode_name)


def default_label_content():
    return DisplayContent(daw_label=TargetContent(lines=('Clip 1/2', )),
      mixer_label=TargetContent(lines=('Level', )))


def is_in_sequencer_mode(state):
    return state.main_pad_modes.selected_mode == "daw" and state.daw_pad_modes.selected_mode == "sequencer"


def track_and_device_names(state):
    return TargetContent(lines=(
     liveobj_name(state.target_track.target_track),
     liveobj_name(state.device.device) or "-"))


def render_mode_notification(state, mode):
    if mode in ('clip_launch', 'stop', 'solo', 'mute'):
        return DisplayContent(temp=TargetContent(lines=("Function", mode.replace("_", " ").title())))
    if mode in ('arm', 'select'):
        if state.fader_button_modes.previous_mode is not None:
            return DisplayContent(temp=TargetContent(lines=("Fader Mode", mode.title())))
        if mode in ('level', 'pan'):
            return DisplayContent(temp=TargetContent(lines=("Mixer", mode.title())),
              mixer_label=TargetContent(lines=(mode.title(),)))
        if mode in ('clip', 'sequencer', 'daw') and not state.main_pad_modes.previous_mode == "null_0":
            label = "Clip 1/2" if state.daw_pad_modes.selected_mode == "clip" else "Sequencer 2/2"
            return DisplayContent(temp=TargetContent(lines=("Pad Mode", label)),
              daw_label=TargetContent(lines=(label,)))


def render_notification(state, notification_text):
    if notification_text.startswith("mode:"):
        return render_mode_notification(state, notification_text.replace("mode:", ""))
    if notification_text in ('track_select', 'device_select'):
        return DisplayContent(temp=(track_and_device_names(state)))
    if notification_text == "device_bank_select":
        return DisplayContent(temp=TargetContent(lines=(
         liveobj_name(state.device.device) or "-",
         state.device.bank_name or "-")))
    if notification_text.startswith("Send"):
        index = send_letter_to_index(notification_text.split()[-1].lower())
        return DisplayContent(temp=TargetContent(lines=("Sends", liveobj_name(song().return_tracks[index]))))
    if "\n" in notification_text:
        lines = tuple(notification_text.split("\n"))
        return DisplayContent(temp=TargetContent(config=(Config.three_line if len(lines) == 3 else Config.two_line),
          lines=lines))


def create_root_view() -> view.View[Optional[DisplayContent]]:

    @view.View
    def main_view(state) -> Optional[DisplayContent]:
        if state.encoder_touch.last_released_index is not None:
            return DisplayContent.with_parameters(state,
              released_encoder_index=(state.encoder_touch.last_released_index))
        if is_in_sequencer_mode(state):
            if state.note_editor.clipboard.copy_button.is_pressed:
                return DisplayContent(static=TargetContent(lines=('Function', 'Duplicate')),
                  cancel_temp=(not state.note_editor.clipboard.copy_button.is_held))
            if state.sequencer_modes.selected_mode == "clip_select":
                return DisplayContent.with_parameters(state,
                  static=TargetContent(lines=('Sequencer', 'Select Clip')))
            if state.note_settings_modes.selected_mode == "active":
                return DisplayContent.with_parameters(state,
                  static=TargetContent(config=(Config.two_by_four),
                  lines=('Note Edit', 'Vel', 'Len', 'Fine', 'Nudg', '', '', '', '')))
            if state.main_encoder_modes.selected_mode == "transport":
                return DisplayContent.with_parameters(state,
                  static=TargetContent(config=(Config.two_by_four),
                  lines=('Transport', 'Scrb', 'ZmH', 'ZmV', 'LPS', 'LPE', 'Mark', '',
                         'BPM')))
            return DisplayContent.with_parameters(state, static=(track_and_device_names(state)))

    return view.CompoundView(view.DisconnectedView(), view.NotificationView(render_notification, duration=0.1, supports_new_line=True), main_view)


def protocol(elements):

    def display(content):
        if content:
            display_content("static", (content.static), show_immediately=True)
            display_content("temp", (content.temp), show_immediately=True)
            display_content("daw_label", content.daw_label)
            display_content("mixer_label", content.mixer_label)
            for (i, encoder) in enumerate(content.encoders):
                display_content("encoder_{}".format(i), encoder)

            for (i, fader) in enumerate(content.faders):
                display_content("fader_{}".format(i), fader)

            if content.cancel_temp:
                cancel_temp_screens(elements)

    def display_content(name, content, show_immediately=False):
        if content:
            if content.lines:
                command = getattr(elements, "{}_display_command".format(name))
                command.send_data((content.config),
                  (tuple((DisplayText(line).as_ascii() for line in content.lines))),
                  show_immediately=show_immediately,
                  trigger=(content.trigger))

    return display


display_specification = DisplaySpecification(create_root_view=create_root_view,
  protocol=protocol,
  notifications=Notifications)
