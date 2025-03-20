# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class LEDDisplay(Component):
    """A LEDDisplay component.
A 7-bar LED display component.

Keyword arguments:

- id (string; optional):
    The ID used to identify the display in Dash callbacks.

- backgroundColor (string; default '#fff'):
    Color of the display's background.

- className (string; optional):
    Class to apply to the root component element.

- color (string; default colors.PRIMARY):
    Color of the display.

- label (dict; optional):
    Description to be displayed alongside the control. To control
    styling, pass an object with label and style properties.

    `label` is a string | dict with keys:

    - style (dict; optional)

    - label (string; optional)

- labelPosition (a value equal to: 'top', 'bottom'; default 'top'):
    Where the display label is positioned.

- n_digits (number; optional):
    Num of digits in display.

- size (number; default 42):
    Size of the display.

- theme (dict; default light):
    Theme configuration to be set by a ThemeProvider.

- value (number | string; optional):
    Value to be displayed. A number or a string containing only digits
    (0-9), periods, and colons, and possibly starting with a minus
    sign."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_daq'
    _type = 'LEDDisplay'
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
        value: typing.Optional[typing.Union[typing.Union[int, float, numbers.Number], str]] = None,
        n_digits: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        color: typing.Optional[str] = None,
        backgroundColor: typing.Optional[str] = None,
        size: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        theme: typing.Optional[dict] = None,
        label: typing.Optional[typing.Union[str, "Label"]] = None,
        labelPosition: typing.Optional[Literal["top", "bottom"]] = None,
        className: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'backgroundColor', 'className', 'color', 'label', 'labelPosition', 'n_digits', 'size', 'style', 'theme', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'backgroundColor', 'className', 'color', 'label', 'labelPosition', 'n_digits', 'size', 'style', 'theme', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(LEDDisplay, self).__init__(**args)
