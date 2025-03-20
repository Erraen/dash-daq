# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class ColorPicker(Component):
    """A ColorPicker component.
A color picker.

Keyword arguments:

- id (string; optional):
    The ID used to identify the color picker in Dash callbacks.

- className (string; optional):
    Class to apply to the root component element.

- disabled (boolean; optional):
    If True, color cannot be picked.

- label (dict; optional):
    Description to be displayed alongside the control. To control
    styling, pass an object with label and style properties.

    `label` is a string | dict with keys:

    - style (dict; optional)

    - label (string; optional)

- labelPosition (a value equal to: 'top', 'bottom'; default 'top'):
    Where the indicator label is positioned.

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

- size (number; default 225):
    Size (width) of the component in pixels.

- theme (dict; default light):
    Theme configuration to be set by a ThemeProvider.

- value (dict; optional):
    Color value of the picker.

    `value` is a dict with keys:

    - hex (string; optional):
        Hex string.

    - rbg (dict; optional):
        RGB/RGBA object.

        `rbg` is a dict with keys:

        - r (number; optional)

        - g (number; optional)

        - b (number; optional)

        - a (number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_daq'
    _type = 'ColorPicker'
    ValueRbg = TypedDict(
        "ValueRbg",
            {
            "r": NotRequired[typing.Union[int, float, numbers.Number]],
            "g": NotRequired[typing.Union[int, float, numbers.Number]],
            "b": NotRequired[typing.Union[int, float, numbers.Number]],
            "a": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    Value = TypedDict(
        "Value",
            {
            "hex": NotRequired[str],
            "rbg": NotRequired["ValueRbg"]
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
        value: typing.Optional["Value"] = None,
        disabled: typing.Optional[bool] = None,
        size: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        theme: typing.Optional[dict] = None,
        label: typing.Optional[typing.Union[str, "Label"]] = None,
        labelPosition: typing.Optional[Literal["top", "bottom"]] = None,
        className: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        persistence: typing.Optional[typing.Union[bool, str, typing.Union[int, float, numbers.Number]]] = None,
        persisted_props: typing.Optional[typing.Sequence[Literal["value"]]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'className', 'disabled', 'label', 'labelPosition', 'persisted_props', 'persistence', 'persistence_type', 'size', 'style', 'theme', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'disabled', 'label', 'labelPosition', 'persisted_props', 'persistence', 'persistence_type', 'size', 'style', 'theme', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(ColorPicker, self).__init__(**args)
