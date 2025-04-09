# file: lib/ansible/module_utils/common/parameters.py:466-500
# asked: {"lines": [489, 493, 495, 496, 498], "branches": [[485, 489], [493, 485], [493, 495], [495, 496], [495, 498]]}
# gained: {"lines": [489, 493, 495, 496, 498], "branches": [[485, 489], [493, 485], [493, 495], [495, 496], [495, 498]]}

import pytest

from ansible.module_utils.common.parameters import _set_defaults

def test_set_defaults_with_default_value():
    argument_spec = {
        'param1': {'default': 'default_value1'},
        'param2': {'default': 'default_value2', 'no_log': True},
        'param3': {'required': True}
    }
    parameters = {}

    no_log_values = _set_defaults(argument_spec, parameters)

    assert parameters['param1'] == 'default_value1'
    assert parameters['param2'] == 'default_value2'
    assert 'param3' in parameters and parameters['param3'] is None
    assert 'default_value2' in no_log_values

def test_set_defaults_without_default_value():
    argument_spec = {
        'param1': {'default': None},
        'param2': {'required': True}
    }
    parameters = {}

    no_log_values = _set_defaults(argument_spec, parameters)

    assert parameters['param1'] is None
    assert 'param2' in parameters and parameters['param2'] is None
    assert len(no_log_values) == 0

def test_set_defaults_with_set_default_false():
    argument_spec = {
        'param1': {'default': 'default_value1'},
        'param2': {'default': 'default_value2', 'no_log': True},
        'param3': {'required': True}
    }
    parameters = {}

    no_log_values = _set_defaults(argument_spec, parameters, set_default=False)

    assert parameters['param1'] == 'default_value1'
    assert parameters['param2'] == 'default_value2'
    assert 'param3' not in parameters
    assert 'default_value2' in no_log_values

def test_set_defaults_with_existing_parameters():
    argument_spec = {
        'param1': {'default': 'default_value1'},
        'param2': {'default': 'default_value2', 'no_log': True},
        'param3': {'required': True}
    }
    parameters = {'param1': 'existing_value1'}

    no_log_values = _set_defaults(argument_spec, parameters)

    assert parameters['param1'] == 'existing_value1'
    assert parameters['param2'] == 'default_value2'
    assert 'param3' in parameters and parameters['param3'] is None
    assert 'default_value2' in no_log_values
