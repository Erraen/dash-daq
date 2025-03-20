# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class Joystick(Component):
    """A Joystick component.
A joystick.

Keyword arguments:

- id (string; optional):
    The ID used to identify the Joystick in Dash callbacks.

- angle (number; optional):
    Joystick angle in degrees, 0 = right, 90 = up, 180 = left, 270 =
    down.

- className (string; optional):
    Class to apply to the root component element.

- force (number; optional):
    Joystick force: distance between cursor and center in big-circle
    radii.

- label (dict; optional):
    Description to be displayed alongside the control. To control
    styling, pass an object with label and style properties.

    `label` is a string | dict with keys:

    - style (dict; optional)

    - label (string; optional)

- labelPosition (a value equal to: 'top', 'bottom'; default 'top'):
    Where the indicator label is positioned.

- size (number; default 100):
    Size (width) of the component in pixels.

- theme (dict; default light):
    Theme configuration to be set by a ThemeProvider."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_daq'
    _type = 'Joystick'
    Label = TypedDict(
        "Label",
            {
            "style": NotRequired[dict],
            "label": NotRequired[str]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        angle: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        force: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        size: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        theme: typing.Optional[dict] = None,
        label: typing.Optional[typing.Union[str, "Label"]] = None,
        labelPosition: typing.Optional[Literal["top", "bottom"]] = None,
        className: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'angle', 'className', 'force', 'label', 'labelPosition', 'size', 'style', 'theme']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'angle', 'className', 'force', 'label', 'labelPosition', 'size', 'style', 'theme']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Joystick, self).__init__(**args)
