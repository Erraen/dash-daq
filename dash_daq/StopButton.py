# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class StopButton(Component):
    """A StopButton component.
A Stop button component

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of the button.

- id (string; optional):
    The ID used to identify this compnent in Dash callbacks.

- buttonText (string; default 'Stop'):
    Text displayed in the button.

- className (string; optional):
    Class to apply to the root component element.

- disabled (boolean; optional):
    If True, button cannot be pressesd.

- label (dict; optional):
    Description to be displayed alongside the button. To control
    styling, pass an object with label and style properties.

    `label` is a string | dict with keys:

    - style (dict; optional)

    - label (string; optional)

- labelPosition (a value equal to: 'top', 'bottom'; default 'top'):
    Where the  label is positioned.

- n_clicks (number; default 0):
    Number of times the button was clicked.

- size (number; default 92):
    The size (width) of the stop button in pixels.

- theme (dict; optional):
    Theme configuration to be set by a ThemeProvider."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_daq'
    _type = 'StopButton'
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
        children: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        size: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        buttonText: typing.Optional[str] = None,
        n_clicks: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        disabled: typing.Optional[bool] = None,
        theme: typing.Optional[dict] = None,
        label: typing.Optional[typing.Union[str, "Label"]] = None,
        labelPosition: typing.Optional[Literal["top", "bottom"]] = None,
        className: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'buttonText', 'className', 'disabled', 'label', 'labelPosition', 'n_clicks', 'size', 'style', 'theme']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'buttonText', 'className', 'disabled', 'label', 'labelPosition', 'n_clicks', 'size', 'style', 'theme']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(StopButton, self).__init__(children=children, **args)
