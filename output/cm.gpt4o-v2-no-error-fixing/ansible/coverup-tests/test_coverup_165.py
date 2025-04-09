# file: lib/ansible/module_utils/common/parameters.py:466-500
# asked: {"lines": [466, 484, 485, 489, 493, 495, 496, 498, 500], "branches": [[485, 489], [485, 500], [493, 485], [493, 495], [495, 496], [495, 498]]}
# gained: {"lines": [466, 484, 485, 489, 493, 495, 496, 498, 500], "branches": [[485, 489], [485, 500], [493, 485], [493, 495], [495, 496], [495, 498]]}

import pytest
from ansible.module_utils.common.parameters import _set_defaults

def test_set_defaults_with_no_log(monkeypatch):
    argument_spec = {
        'param1': {'default': 'value1', 'no_log': True},
        'param2': {'default': 'value2', 'no_log': False},
        'param3': {'default': None, 'no_log': True},
        'param4': {'no_log': True},
    }
    parameters = {}

    no_log_values = _set_defaults(argument_spec, parameters)

    assert parameters == {
        'param1': 'value1',
        'param2': 'value2',
        'param3': None,
        'param4': None,
    }
    assert no_log_values == {'value1'}

def test_set_defaults_without_no_log(monkeypatch):
    argument_spec = {
        'param1': {'default': 'value1'},
        'param2': {'default': 'value2'},
        'param3': {'default': None},
        'param4': {},
    }
    parameters = {}

    no_log_values = _set_defaults(argument_spec, parameters)

    assert parameters == {
        'param1': 'value1',
        'param2': 'value2',
        'param3': None,
        'param4': None,
    }
    assert no_log_values == set()

def test_set_defaults_with_existing_parameters(monkeypatch):
    argument_spec = {
        'param1': {'default': 'value1', 'no_log': True},
        'param2': {'default': 'value2', 'no_log': False},
    }
    parameters = {
        'param1': 'existing_value1',
    }

    no_log_values = _set_defaults(argument_spec, parameters)

    assert parameters == {
        'param1': 'existing_value1',
        'param2': 'value2',
    }
    assert no_log_values == set()

def test_set_defaults_with_set_default_false(monkeypatch):
    argument_spec = {
        'param1': {'default': 'value1', 'no_log': True},
        'param2': {'default': 'value2', 'no_log': False},
    }
    parameters = {}

    no_log_values = _set_defaults(argument_spec, parameters, set_default=False)

    assert parameters == {
        'param1': 'value1',
        'param2': 'value2',
    }
    assert no_log_values == {'value1'}
