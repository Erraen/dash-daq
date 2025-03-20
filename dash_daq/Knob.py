# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class Knob(Component):
    """A Knob component.
A knob component that can be turned
to a value between some range.

Keyword arguments:

- id (string; optional):
    The ID used to identify this compnent in Dash callbacks.

- className (string; optional):
    Class to apply to the root component element.

- color (dict; optional):
    Color configuration for the knob's track.

    `color` is a string | dict with keys:

    - default (string; optional):
        Color used for current value text and other minor accents.

    - gradient (boolean; optional):
        Display ranges as a gradient between given colors.

    - ranges (dict; optional):
        Define multiple color ranges on the knob's track. The key
        determines the color of the range and the value is the
        start,end of the range itself. Ranges must be contiguous along
        the entirety of the knob's range of values.

        `ranges` is a dict with keys:

        - color (list of numbers; optional)

- digits (number; optional):
    number of digits to show after decimal places.

- disabled (boolean; optional):
    If True, knob cannot be moved.

- label (dict; optional):
    Description to be displayed alongside the control. To control
    styling, pass an object with label and style properties.

    `label` is a string | dict with keys:

    - style (dict; optional)

    - label (string; optional)

- labelPosition (a value equal to: 'top', 'bottom'; default 'top'):
    Where the knob label is positioned.

- max (number; default 10):
    The maximum value of the knob.

- min (number; default 0):
    The minimum value of the knob.

- persisted_props (list of a value equal to: 'value's; default ['value']):
    Properties whose user interactions will persist after refreshing
    the component or the page. Since only `value` is allowed this prop
    can normally be ignored.

- persistence (boolean | string | number; optional):
    Used to allow user interactions in this component to be persisted
    when the component - or the page - is refreshed. If `persisted` is
    truthy and hasn't changed from its previous value, a `value` that
    the user has changed while using the app will keep that change, as
    long as the new `value` also matches what was given originally.
    Used in conjunction with `persistence_type`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    Where persisted user changes will be stored: memory: only kept in
    memory, reset on page refresh. local: window.localStorage, data is
    kept after the browser quit. session: window.sessionStorage, data
    is cleared once the browser quit.

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
    show current value of knob.

- size (number; default 114):
    The size (diameter) of the knob in pixels.

- textColor (string; optional):
    text color of scale.

- theme (dict; default light):
    Theme configuration to be set by a ThemeProvider.

- value (number; optional):
    The value of knob."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_daq'
    _type = 'Knob'
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
        color: typing.Optional[typing.Union[str, "Color"]] = None,
        size: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        min: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        max: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        disabled: typing.Optional[bool] = None,
        theme: typing.Optional[dict] = None,
        label: typing.Optional[typing.Union[str, "Label"]] = None,
        labelPosition: typing.Optional[Literal["top", "bottom"]] = None,
        scale: typing.Optional["Scale"] = None,
        className: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        persistence: typing.Optional[typing.Union[bool, str, typing.Union[int, float, numbers.Number]]] = None,
        persisted_props: typing.Optional[typing.Sequence[Literal["value"]]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        showCurrentValue: typing.Optional[bool] = None,
        textColor: typing.Optional[str] = None,
        digits: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'className', 'color', 'digits', 'disabled', 'label', 'labelPosition', 'max', 'min', 'persisted_props', 'persistence', 'persistence_type', 'scale', 'showCurrentValue', 'size', 'style', 'textColor', 'theme', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'color', 'digits', 'disabled', 'label', 'labelPosition', 'max', 'min', 'persisted_props', 'persistence', 'persistence_type', 'scale', 'showCurrentValue', 'size', 'style', 'textColor', 'theme', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Knob, self).__init__(**args)
