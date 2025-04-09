# file lib/ansible/module_utils/common/parameters.py:466-500
# lines [466, 484, 485, 489, 493, 495, 496, 498, 500]
# branches ['485->489', '485->500', '493->485', '493->495', '495->496', '495->498']

import pytest
from ansible.module_utils.common.parameters import _set_defaults

def test_set_defaults():
    # Mocking the argument_spec and parameters
    argument_spec = {
        'param1': {'default': 'value1', 'no_log': True},
        'param2': {'default': 'value2'},
        'param3': {'required': True},
        'param4': {}
    }
    parameters = {
        'param3': 'user_value3'
    }

    # Call the function with set_default=True
    no_log_values = _set_defaults(argument_spec, parameters, set_default=True)

    # Assertions to verify the postconditions
    assert parameters['param1'] == 'value1'
    assert parameters['param2'] == 'value2'
    assert parameters['param3'] == 'user_value3'
    assert 'param4' in parameters and parameters['param4'] is None
    assert no_log_values == {'value1'}

    # Clean up
    parameters.clear()

    # Call the function with set_default=False
    parameters['param3'] = 'user_value3'
    parameters['param1'] = 'user_value1'  # Ensure param1 is set by user
    parameters['param2'] = 'user_value2'  # Ensure param2 is set by user
    no_log_values = _set_defaults(argument_spec, parameters, set_default=False)

    # Assertions to verify the postconditions
    assert parameters['param1'] == 'user_value1'
    assert parameters['param2'] == 'user_value2'
    assert parameters['param3'] == 'user_value3'
    assert 'param4' not in parameters
    assert no_log_values == set()

    # Clean up
    parameters.clear()
