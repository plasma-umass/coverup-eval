# file: lib/ansible/module_utils/common/arg_spec.py:94-140
# asked: {"lines": [94, 95, 96, 97, 98, 99, 127, 128, 129, 130, 131, 132, 133, 135, 136, 137, 138, 140], "branches": [[135, 0], [135, 136], [137, 138], [137, 140]]}
# gained: {"lines": [94, 95, 96, 97, 98, 99, 127, 128, 129, 130, 131, 132, 133, 135, 136, 137, 138, 140], "branches": [[135, 0], [135, 136], [137, 138], [137, 140]]}

import pytest
from ansible.module_utils.common.arg_spec import ArgumentSpecValidator

def test_argument_spec_validator_no_aliases():
    argument_spec = {
        'param1': {},
        'param2': {}
    }
    validator = ArgumentSpecValidator(argument_spec)
    assert validator._valid_parameter_names == {'param1', 'param2'}

def test_argument_spec_validator_with_aliases():
    argument_spec = {
        'param1': {'aliases': ['p1', 'p_one']},
        'param2': {'aliases': ['p2']}
    }
    validator = ArgumentSpecValidator(argument_spec)
    assert validator._valid_parameter_names == {'param1 (p1, p_one)', 'param2 (p2)'}

def test_argument_spec_validator_mixed_aliases():
    argument_spec = {
        'param1': {'aliases': ['p1', 'p_one']},
        'param2': {}
    }
    validator = ArgumentSpecValidator(argument_spec)
    assert validator._valid_parameter_names == {'param1 (p1, p_one)', 'param2'}
