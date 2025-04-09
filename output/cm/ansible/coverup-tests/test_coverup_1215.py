# file lib/ansible/module_utils/common/parameters.py:466-500
# lines [484, 485, 489, 493, 495, 496, 498, 500]
# branches ['485->489', '485->500', '493->485', '493->495', '495->496', '495->498']

import pytest

from ansible.module_utils.common.parameters import _set_defaults

@pytest.fixture
def argument_spec():
    return {
        'param1': {'default': 'default_value1', 'no_log': False},
        'param2': {'default': 'default_value2', 'no_log': True},
        'param3': {'no_log': False},
        'param4': {'no_log': True},
    }

@pytest.fixture
def parameters():
    return {}

def test_set_defaults_with_no_log(argument_spec, parameters):
    no_log_values = _set_defaults(argument_spec, parameters, set_default=False)
    
    assert parameters['param1'] == 'default_value1'
    assert parameters['param2'] == 'default_value2'
    assert 'param3' not in parameters
    assert 'param4' not in parameters
    assert no_log_values == {'default_value2'}
