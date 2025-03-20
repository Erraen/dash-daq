# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class Slider(Component):
    """A Slider component.
A slider component with support for
a target value.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- className (string; optional):
    Additional CSS class for the root DOM node.

- color (dict; default colors.DARKER_PRIMARY):
    Color configuration for the slider's track.

    `color` is a string | dict with keys:

    - default (string; optional):
        Fallback color to use when color.ranges has gaps.

    - gradient (boolean; optional):
        Display ranges as a gradient between given colors. Requires
        color.ranges to be contiguous along the entirety of the
        gauge's range of values.

    - ranges (dict; optional):
        Define multiple color ranges on the slider's track. The key
        determines the color of the range and the value is the
        start,end of the range itself.

        `ranges` is a dict with keys:

        - color (list of numbers; optional)

- disabled (boolean; optional):
    If True, the handles can't be moved.

- dots (boolean; optional):
    When the step value is greater than 1, you can set the dots to
    True if you want to render the slider with dots.  Note: dots are
    disabled automatically when using color.ranges.

- fullSize (boolean; optional):
    make slider same size of its parent.

- handleLabel (dict; optional):
    Configuration of the slider handle's label. Passing falsy value
    will disable the label.

    `handleLabel` is a string | dict with keys:

    - showCurrentValue (boolean; optional)

    - label (string; optional)

    - color (string; optional)

    - style (dict; optional)

- included (boolean; optional):
    If the value is True, it means a continuous value is included.
    Otherwise, it is an independent value.

- labelPosition (a value equal to: 'top', 'bottom'; default 'bottom'):
    Where the component label is positioned.

- marks (dict; optional):
    Marks on the slider. The key determines the position, and the
    value determines what will show. If you want to set the style of a
    specific mark point, the value should be an object which contains
    style and label properties.

    `marks` is a dict with keys:

    - number (dict; optional)

        `number` is a string

      Or dict with keys:

        - style (dict; optional)

        - label (string; optional)

- max (number; optional):
    Maximum allowed value of the slider.

- min (number; default 0):
    Minimum allowed value of the slider.

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

- size (number; default 265):
    Size of the slider in pixels.

- step (number; optional):
    Value by which increments or decrements are made.

- targets (dict; optional):
    Targets on the slider. The key determines the position, and the
    value determines what will show. If you want to set the style of a
    specific target point, the value should be an object which
    contains style and label properties.

    `targets` is a dict with keys:

    - number (dict; optional)

        `number` is a string

      Or dict with keys:

        - showCurrentValue (boolean; optional)

        - label (string; optional)

        - color (string; optional)

        - style (dict; optional)

- theme (dict; default light):
    Theme configuration to be set by a ThemeProvider.

- updatemode (a value equal to: 'mouseup', 'drag'; default 'mouseup'):
    Determines when the component should update its value. If
    `mouseup`, then the slider will only trigger its value when the
    user has finished dragging the slider. If `drag`, then the slider
    will update its value continuously as it is being dragged. Only
    use `drag` if your updates are fast.

- value (number; optional):
    The value of the input.

- vertical (boolean; optional):
    If True, the slider will be vertical."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_daq'
    _type = 'Slider'
    MarksNumber = TypedDict(
        "MarksNumber",
            {
            "style": NotRequired[dict],
            "label": NotRequired[str]
        }
    )

    Marks = TypedDict(
        "Marks",
            {
            "number": NotRequired[typing.Union[str, "MarksNumber"]]
        }
    )

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

    TargetsNumber = TypedDict(
        "TargetsNumber",
            {
            "showCurrentValue": NotRequired[bool],
            "label": NotRequired[str],
            "color": NotRequired[str],
            "style": NotRequired[dict]
        }
    )

    Targets = TypedDict(
        "Targets",
            {
            "number": NotRequired[typing.Union[str, "TargetsNumber"]]
        }
    )

    HandleLabel = TypedDict(
        "HandleLabel",
            {
            "showCurrentValue": NotRequired[bool],
            "label": NotRequired[str],
            "color": NotRequired[str],
            "style": NotRequired[dict]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        style: typing.Optional[typing.Any] = None,
        marks: typing.Optional["Marks"] = None,
        color: typing.Optional[typing.Union[str, "Color"]] = None,
        value: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        className: typing.Optional[str] = None,
        labelPosition: typing.Optional[Literal["top", "bottom"]] = None,
        disabled: typing.Optional[bool] = None,
        dots: typing.Optional[bool] = None,
        included: typing.Optional[bool] = None,
        min: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        max: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        step: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        vertical: typing.Optional[bool] = None,
        size: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        targets: typing.Optional["Targets"] = None,
        theme: typing.Optional[dict] = None,
        handleLabel: typing.Optional[typing.Union[str, "HandleLabel"]] = None,
        updatemode: typing.Optional[Literal["mouseup", "drag"]] = None,
        persistence: typing.Optional[typing.Union[bool, str, typing.Union[int, float, numbers.Number]]] = None,
        persisted_props: typing.Optional[typing.Sequence[Literal["value"]]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        fullSize: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'className', 'color', 'disabled', 'dots', 'fullSize', 'handleLabel', 'included', 'labelPosition', 'marks', 'max', 'min', 'persisted_props', 'persistence', 'persistence_type', 'size', 'step', 'style', 'targets', 'theme', 'updatemode', 'value', 'vertical']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'color', 'disabled', 'dots', 'fullSize', 'handleLabel', 'included', 'labelPosition', 'marks', 'max', 'min', 'persisted_props', 'persistence', 'persistence_type', 'size', 'step', 'style', 'targets', 'theme', 'updatemode', 'value', 'vertical']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Slider, self).__init__(**args)
