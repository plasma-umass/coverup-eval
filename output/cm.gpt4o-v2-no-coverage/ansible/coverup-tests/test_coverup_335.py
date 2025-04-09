# file: lib/ansible/module_utils/common/parameters.py:466-500
# asked: {"lines": [466, 484, 485, 489, 493, 495, 496, 498, 500], "branches": [[485, 489], [485, 500], [493, 485], [493, 495], [495, 496], [495, 498]]}
# gained: {"lines": [466, 484, 485, 489, 493, 495, 496, 498, 500], "branches": [[485, 489], [485, 500], [493, 485], [493, 495], [495, 496], [495, 498]]}

import pytest

from ansible.module_utils.common.parameters import _set_defaults

def test_set_defaults_with_no_defaults():
    argument_spec = {
        'param1': {'type': 'str'},
        'param2': {'type': 'int'}
    }
    parameters = {}

    no_log_values = _set_defaults(argument_spec, parameters)

    assert parameters == {'param1': None, 'param2': None}
    assert no_log_values == set()

def test_set_defaults_with_defaults():
    argument_spec = {
        'param1': {'type': 'str', 'default': 'default1'},
        'param2': {'type': 'int', 'default': 2}
    }
    parameters = {}

    no_log_values = _set_defaults(argument_spec, parameters)

    assert parameters == {'param1': 'default1', 'param2': 2}
    assert no_log_values == set()

def test_set_defaults_with_no_log():
    argument_spec = {
        'param1': {'type': 'str', 'default': 'default1', 'no_log': True},
        'param2': {'type': 'int', 'default': 2}
    }
    parameters = {}

    no_log_values = _set_defaults(argument_spec, parameters)

    assert parameters == {'param1': 'default1', 'param2': 2}
    assert no_log_values == {'default1'}

def test_set_defaults_with_existing_parameters():
    argument_spec = {
        'param1': {'type': 'str', 'default': 'default1'},
        'param2': {'type': 'int', 'default': 2}
    }
    parameters = {'param1': 'existing1'}

    no_log_values = _set_defaults(argument_spec, parameters)

    assert parameters == {'param1': 'existing1', 'param2': 2}
    assert no_log_values == set()

def test_set_defaults_with_set_default_false():
    argument_spec = {
        'param1': {'type': 'str', 'default': 'default1'},
        'param2': {'type': 'int', 'default': 2}
    }
    parameters = {}

    no_log_values = _set_defaults(argument_spec, parameters, set_default=False)

    assert parameters == {'param1': 'default1', 'param2': 2}
    assert no_log_values == set()
