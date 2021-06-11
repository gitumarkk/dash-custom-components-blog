# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MyCalendar(Component):
    """A MyCalendar component.
MyCalendar allows the user to select a date

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- date (string; optional):
    The date as a string."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, date=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'date']
        self._type = 'MyCalendar'
        self._namespace = 'custom_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'date']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(MyCalendar, self).__init__(**args)
