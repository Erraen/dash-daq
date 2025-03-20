# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class Tank(Component):
    """A Tank component.
A Tank component that fills to
a value between some range.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- base (number; default 10):
    Base to be used in logarithmic scale.

- className (string; optional):
    Class to apply to the root component element.

- color (string; optional):
    The color of tank fill.

- currentValueStyle (dict; optional):
    text style of current value.

- exceedMessage (string; optional):
    Warning message when value exceed max.

- height (number; default 192):
    The height of the tank in pixels.

- label (dict; optional):
    Description to be displayed alongside the control. To control
    styling, pass an object with label and style properties.

    `label` is a string | dict with keys:

    - style (dict; optional)

    - label (string; optional)

- labelPosition (a value equal to: 'top', 'bottom'; default 'top'):
    Where the component label is positioned.

- lagingMessage (string; optional):
    Warning message when value is laging from min.

- logarithmic (boolean; optional):
    If set to True, a logarithmic scale will be used.

- max (number; default 10):
    The maximum value of the tank. If logarithmic, represents the
    maximum exponent.

- min (number; default 0):
    The minimum value of the tank. If logarithmic, represents minimum
    exponent.

- scale (dict; optional):
    Configuration for the component scale.

    `scale` is a dict with keys:

    - start (number; optional):
        Value to start the scale from. Defaults to min.

    - interval (number; optional):
        Interval by which the scale goes up. Attempts to dynamically
        divide min-max range by default.

    - labelInterval (number; optional):
        Interval by which labels are added to scale marks. Defaults to
        2 (every other mark has a label).

    - custom (dict; optional):
        Custom scale marks. The key determines the position and the
        value determines what will show. If you want to set the style
        of a specific mark point, the value should be an object which
        contains style and label properties.

        `custom` is a number

      Or dict with keys:

        - style (string; optional)

        - label (string; optional)

- showCurrentValue (boolean; optional):
    If True, the current value of the tank will be displayed.

- textColor (string; optional):
    text color.

- theme (dict; default light):
    Theme configuration to be set by a ThemeProvider.

- units (string; optional):
    Label for the current value.

- value (number; optional):
    The value of tank. If logarithmic, the displayed value will be the
    logarithm of the inputted value.

- width (number; default 112):
    The width of the tank in pixels."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_daq'
    _type = 'Tank'
    Label = TypedDict(
        "Label",
            {
            "style": NotRequired[dict],
            "label": NotRequired[str]
        }
    )

    ScaleCustom = TypedDict(
        "ScaleCustom",
            {
            "style": NotRequired[str],
            "label": NotRequired[str]
        }
    )

    Scale = TypedDict(
        "Scale",
            {
            "start": NotRequired[typing.Union[int, float, numbers.Number]],
            "interval": NotRequired[typing.Union[int, float, numbers.Number]],
            "labelInterval": NotRequired[typing.Union[int, float, numbers.Number]],
            "custom": NotRequired[typing.Union[typing.Union[int, float, numbers.Number], "ScaleCustom"]]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        value: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        height: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        width: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        color: typing.Optional[str] = None,
        theme: typing.Optional[dict] = None,
        currentValueStyle: typing.Optional[dict] = None,
        min: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        max: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        base: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        logarithmic: typing.Optional[bool] = None,
        showCurrentValue: typing.Optional[bool] = None,
        units: typing.Optional[str] = None,
        label: typing.Optional[typing.Union[str, "Label"]] = None,
        labelPosition: typing.Optional[Literal["top", "bottom"]] = None,
        scale: typing.Optional["Scale"] = None,
        className: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        exceedMessage: typing.Optional[typing.Union[str]] = None,
        lagingMessage: typing.Optional[typing.Union[str]] = None,
        textColor: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'base', 'className', 'color', 'currentValueStyle', 'exceedMessage', 'height', 'label', 'labelPosition', 'lagingMessage', 'logarithmic', 'max', 'min', 'scale', 'showCurrentValue', 'style', 'textColor', 'theme', 'units', 'value', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'base', 'className', 'color', 'currentValueStyle', 'exceedMessage', 'height', 'label', 'labelPosition', 'lagingMessage', 'logarithmic', 'max', 'min', 'scale', 'showCurrentValue', 'style', 'textColor', 'theme', 'units', 'value', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Tank, self).__init__(**args)
