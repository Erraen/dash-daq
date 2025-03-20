# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class GraduatedBar(Component):
    """A GraduatedBar component.
A graduated bar component that displays
a value within some range as a
percentage.

Keyword arguments:

- id (string; optional):
    The ID used to identify this compnent in Dash callbacks.

- className (string; optional):
    Class to apply to the root component element.

- color (dict; default light.primary):
    Color configuration for the graduated bar's progress blocks.

    `color` is a string | dict with keys:

    - default (string; optional):
        Fallback color to use when color.ranges has gaps.

    - gradient (boolean; optional):
        Display ranges as a gradient between given colors. Requires
        color.ranges to be contiguous along the entirety of the
        graduated bar's range of values.

    - ranges (dict; optional):
        Define multiple color ranges on the graduated bar's track. The
        key determines the color of the range and the value is the
        start,end of the range itself.

        `ranges` is a dict with keys:

        - color (list of numbers; optional)

- label (dict; optional):
    Description to be displayed alongside the control. To control
    styling, pass an object with label and style properties.

    `label` is a string | dict with keys:

    - style (dict; optional)

    - label (string; optional)

- labelPosition (a value equal to: 'top', 'bottom'; default 'top'):
    Where the component label is positioned.

- max (number; default 10):
    The maximum value of the graduated bar.

- min (number; default 0):
    The minimum value of the graduated bar.

- showCurrentValue (boolean; optional):
    If True, the current percentage  of the bar will be displayed.

- size (number; default 250):
    The size (length) of the graduated bar in pixels.

- step (number; default 0.5):
    Value by which progress blocks appear.

- theme (dict; default light):
    Theme configuration to be set by a ThemeProvider.

- value (number; optional):
    The value of the graduated bar.

- vertical (boolean; optional):
    If True, will display bar vertically instead of horizontally."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_daq'
    _type = 'GraduatedBar'
    ColorRanges = TypedDict(
        "ColorRanges",
            {
            "color": NotRequired[typing.Sequence[typing.Union[int, float, numbers.Number]]]
        }
    )

    Color = TypedDict(
        "Color",
            {
            "default": NotRequired[str],
            "gradient": NotRequired[bool],
            "ranges": NotRequired["ColorRanges"]
        }
    )

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
        value: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        color: typing.Optional[typing.Union[str, "Color"]] = None,
        size: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        vertical: typing.Optional[bool] = None,
        min: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        max: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        step: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        showCurrentValue: typing.Optional[bool] = None,
        theme: typing.Optional[dict] = None,
        label: typing.Optional[typing.Union[str, "Label"]] = None,
        labelPosition: typing.Optional[Literal["top", "bottom"]] = None,
        className: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'className', 'color', 'label', 'labelPosition', 'max', 'min', 'showCurrentValue', 'size', 'step', 'style', 'theme', 'value', 'vertical']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'color', 'label', 'labelPosition', 'max', 'min', 'showCurrentValue', 'size', 'step', 'style', 'theme', 'value', 'vertical']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(GraduatedBar, self).__init__(**args)
