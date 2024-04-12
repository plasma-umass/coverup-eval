# file lib/ansible/module_utils/common/arg_spec.py:94-140
# lines [94, 95, 96, 97, 98, 99, 127, 128, 129, 130, 131, 132, 133, 135, 136, 137, 138, 140]
# branches ['135->exit', '135->136', '137->138', '137->140']

import pytest
from ansible.module_utils.common.arg_spec import ArgumentSpecValidator

def test_argument_spec_validator_aliases():
    argument_spec = {
        'name': {
            'type': 'str',
            'aliases': ['username']
        },
        'password': {
            'type': 'str'
        }
    }
    validator = ArgumentSpecValidator(argument_spec=argument_spec)

    # Check if aliases are included in the valid parameter names
    assert 'name (username)' in validator._valid_parameter_names
    assert 'password' in validator._valid_parameter_names
    assert 'username' not in validator._valid_parameter_names  # Alias should not be a standalone entry

def test_argument_spec_validator_no_aliases():
    argument_spec = {
        'name': {
            'type': 'str'
        },
        'password': {
            'type': 'str'
        }
    }
    validator = ArgumentSpecValidator(argument_spec=argument_spec)

    # Check if parameter names are included without aliases
    assert 'name' in validator._valid_parameter_names
    assert 'password' in validator._valid_parameter_names
    assert 'name (username)' not in validator._valid_parameter_names  # There should be no alias entry

# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])
