# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_mk3/display.py
# Compiled at: 2024-08-28 00:56:43
# Size of source mod 2**32: 9655 bytes
from __future__ import absolute_import, print_function, unicode_literals
from dataclasses import dataclass
from enum import IntEnum
from functools import partial
from typing import Optional, Tuple
from ableton.v3.control_surface.display import DefaultNotifications, DisplaySpecification, Text, view
from ableton.v3.live import display_name, is_track_armed, liveobj_color_to_midi_rgb_values, liveobj_name, parameter_value_to_midi_value, scene_index, simple_track_name, song
Line1Text = partial(Text, max_width=17, justification=(Text.Justification.NONE))
Line2Text = partial(Text, max_width=30, justification=(Text.Justification.NONE))
PopupLine2Text = partial(Text, max_width=21, justification=(Text.Justification.NONE))
BUTTON_TYPES = {'toggle':(2, 3), 
 'tab':(4, 6),  'icon':(10, 11)}

class ScreenId(IntEnum):
    TWO_LINE = 13
    TWO_LINE_POPUP = 24
    THREE_LINE_POPUP = 25
    ENCODER_PARAMETER = 28
    FADER_PARAMETER = 29
    ICONIFIED_TWO_LINE_POPUP = 31


class Icon(IntEnum):
    NONE = 0
    UP = 1
    DOWN = 2
    AUDIO_ARM = 5
    MIDI_ARM = 6
    PLAY = 12
    SOLO = 13
    STOP = 14
    ABLETON = 60


class Color:
    BLACK = (0, 0, 0)
    GREY = (66, 66, 66)
    WHITE = (127, 127, 127)
    RED = (120, 28, 19)
    GREEN = (0, 127, 0)
    BLUE = (0, 108, 122)
    YELLOW = (127, 88, 0)


@dataclass
class ParameterContent:
    name: str
    value_as_str: str
    value: int
    screen_id: ScreenId


@dataclass
class ButtonContent:
    text = None
    text: Optional[str]
    icon = Icon.NONE
    icon: Optional[Icon]
    on_color = Color.WHITE
    on_color: Optional[Color]
    off_color = Color.WHITE
    off_color: Optional[Color]
    is_on = False
    is_on: Optional[bool]
    button_type = BUTTON_TYPES["icon"]
    button_type: Optional[tuple]

    @property
    def color(self):
        if self.is_on:
            return self.on_color
        return self.off_color


@dataclass
class Content:
    primary_lines = None
    primary_lines: Optional[Tuple[(str, str)]]
    primary_color = Color.WHITE
    primary_color: Optional[Color]
    popup_lines = None
    popup_lines: Optional[Tuple[(str, str, str)]]
    popup_colors = (Color.WHITE,
     Color.WHITE,
     Color.WHITE)
    popup_colors: Optional[Tuple[(Color, Color, Color)]]
    popup_icon = Icon.NONE
    popup_icon: Optional[Icon]
    parameter = None
    parameter: Optional[ParameterContent]
    context_buttons = None
    context_buttons: Optional[Tuple[(ButtonContent, ButtonContent, ButtonContent, ButtonContent, ButtonContent, ButtonContent, ButtonContent, ButtonContent)]]


class Notifications(DefaultNotifications):
    identify = lambda: Content(popup_lines=('Ableton Live', 'Connected'),
      popup_icon=(Icon.ABLETON))
    controlled_range = "mixer"

    class Transport(DefaultNotifications.Transport):
        tap_tempo = lambda tempo: Content(popup_lines=(
         "Tap Tempo", "{:0.2f} BPM".format(tempo)),
          popup_colors=(
         Color.WHITE, Color.BLUE))

    class Device(DefaultNotifications.Device):
        select = "device"


def render_notification(state, notification):
    if notification == "mixer":
        return create_mixer_popup_screen(state)
    if notification == "device":
        return create_device_popup_screen(state)
    return notification


def create_mixer_popup_screen(state):
    if state.continuous_control_modes.selected_mode == "mixer":
        return Content(popup_lines=(
         "Mixer Control",
         state.mixer_session_ring.controlled_range,
         "HOLD TO OFFSET"),
          popup_colors=(
         Color.WHITE, Color.BLUE, Color.GREY))


def create_device_popup_screen(state):
    if state.continuous_control_modes.selected_mode == "device":
        return Content(popup_lines=(
         "Device Control",
         liveobj_name(state.device.device) or "No Device",
         "HOLD TO SELECT DEVICES"),
          popup_colors=(
         Color.WHITE, Color.BLUE, Color.GREY))


def create_mixer_button_content(state):
    track = state.target_track.target_track
    return (
     ButtonContent(text=(simple_track_name(track)),
       on_color=(Color.YELLOW),
       is_on=(track != song().master_track and not track.mute),
       button_type=(BUTTON_TYPES["toggle"])),
     ButtonContent(icon=(Icon.SOLO),
       on_color=(Color.BLUE),
       is_on=(track != song().master_track and track.solo)),
     ButtonContent(icon=(Icon.MIDI_ARM if track.has_midi_input else Icon.AUDIO_ARM),
       on_color=(Color.RED),
       is_on=(is_track_armed(track))),
     ButtonContent(icon=(Icon.STOP), on_color=(Color.RED), is_on=True) if state.scene_launch.launch_button.is_held else ButtonContent(icon=(Icon.PLAY),
       on_color=(Color.GREEN),
       is_on=(song().view.selected_scene.is_triggered)))


def create_mode_button_content(state, mode_name):
    return ButtonContent(text=(mode_name.upper()),
      is_on=(state.continuous_control_modes.selected_mode == mode_name),
      button_type=(BUTTON_TYPES["tab"]))


def create_navigation_button_content():
    index = scene_index()
    return (
     ButtonContent(icon=(Icon.UP), off_color=(Color.WHITE if index > 0 else Color.GREY)),
     ButtonContent(icon=(Icon.DOWN),
       off_color=(Color.WHITE if index < len(song().scenes) - 1 else Color.GREY)))


def create_root_view() -> view.View[Optional[Content]]:

    @view.View
    def main_view(state) -> Optional[Content]:
        if state.mode_buttons.device_button.is_held:
            return create_device_popup_screen(state)
        if state.mode_buttons.mixer_button.is_held:
            return create_mixer_popup_screen(state)
        return Content(primary_lines=(
         liveobj_name(state.target_track.target_track),
         display_name(song().view.selected_scene)),
          primary_color=(liveobj_color_to_midi_rgb_values(state.target_track.target_track)),
          context_buttons=(
         *create_mixer_button_content(state),
         
          create_mode_button_content(state, "device"),
          create_mode_button_content(state, "mixer"),
         *create_navigation_button_content()))

    @view.View
    def parameter_view(state) -> Optional[Content]:
        active_parameter = state.active_parameter.parameter
        if active_parameter:
            return Content(parameter=ParameterContent(name=(display_name(active_parameter)),
              value_as_str=(str(active_parameter)),
              value=(parameter_value_to_midi_value(active_parameter)),
              screen_id=(ScreenId.FADER_PARAMETER if state.active_parameter.is_fader else ScreenId.ENCODER_PARAMETER)))

    return view.CompoundView(view.DisconnectedView(), view.NotificationView(render_notification), parameter_view, main_view)


def protocol(elements):

    def display(content):
        if content:
            display_primary_content(content.primary_lines, content.primary_color)
            display_context_button_content(content.context_buttons)
            display_parameter_content(content.parameter)
            display_popup_content(content.popup_lines, content.popup_colors, content.popup_icon)

    def display_primary_content(text, color):
        if text:
            with elements.display_full_screen_command.deferring_send():
                elements.display_line_1.display_message(text[0])
                elements.display_line_2.display_message(text[1])
                elements.display_full_screen_command.send_value(color=color)

    def display_context_button_content(content):
        if content:
            for (i, button) in enumerate(content):
                if not not button.text:
                    if button.icon:
                        pass
                    getattr(elements, "display_button_command_{}".format(i)).send_value(text=(Text(button.text).as_ascii()),
                      button_type=(button.button_type[int(button.is_on)]),
                      color=(button.color),
                      icon=(button.icon))

    def display_parameter_content(parameter):
        if parameter:
            elements.display_parameter_command.send_value(screen_id=(parameter.screen_id),
              name=(Text(parameter.name).as_ascii()),
              value_as_str=(Text(parameter.value_as_str).as_ascii()),
              value=(parameter.value))

    def display_popup_content(text, colors, icon):
        if text:
            elements.display_popup_command.send_value(line_1=(Text(text[0]).as_ascii()),
              line_2=(PopupLine2Text(text[1]).as_ascii()),
              line_3=(Text(text[2]).as_ascii() if len(text) == 3 else None),
              colors=colors,
              icon=icon)

    return display


display_specification = DisplaySpecification(create_root_view=create_root_view,
  protocol=protocol,
  notifications=Notifications)
