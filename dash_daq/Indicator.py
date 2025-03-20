# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class Indicator(Component):
    """An Indicator component.
A boolean indicator LED.

Keyword arguments:

- id (string; optional):
    The ID used to identify the indicator in Dash callbacks.

- className (string; optional):
    Class to apply to the root component element.

- color (string; default colors.DARKER_PRIMARY):
    Color of the indicator.

- height (number; optional):
    Height of the component. Set both width and height for a
    rectangular indicator.

- label (dict; optional):
    Description to be displayed alongside the control. To control
    styling, pass an object with label and style properties.

    `label` is a string | dict with keys:

    - style (dict; optional)

    - label (string; optional)

- labelPosition (a value equal to: 'top', 'bottom', 'right', 'left'; default 'top'):
    Where the indicator label is positioned.

- size (number; default 15):
    Size of the component. Either use this or width and height.

- theme (dict; default light):
    Theme configuration to be set by a ThemeProvider.

- value (boolean; optional):
    If True, indicator is illuminated.

- width (number; optional):
    Width of the component. Set both width and height for a
    rectangular indicator."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_daq'
    _type = 'Indicator'
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
        value: typing.Optional[bool] = None,
        color: typing.Optional[str] = None,
        size: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        width: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        height: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        theme: typing.Optional[dict] = None,
        label: typing.Optional[typing.Union[str, "Label"]] = None,
        labelPosition: typing.Optional[Literal["top", "bottom", "right", "left"]] = None,
        className: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'className', 'color', 'height', 'label', 'labelPosition', 'size', 'style', 'theme', 'value', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'color', 'height', 'label', 'labelPosition', 'size', 'style', 'theme', 'value', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Indicator, self).__init__(**args)
