# file: lib/ansible/module_utils/common/validation.py:213-243
# asked: {"lines": [213, 228, 229, 230, 232, 233, 234, 235, 237, 238, 239, 240, 241, 243], "branches": [[229, 230], [229, 232], [232, 233], [232, 237], [234, 232], [234, 235], [237, 238], [237, 243], [239, 240], [239, 241]]}
# gained: {"lines": [213, 228, 229, 230, 232, 233, 234, 235, 237, 238, 239, 240, 241, 243], "branches": [[229, 230], [229, 232], [232, 233], [232, 237], [234, 232], [234, 235], [237, 238], [237, 243], [239, 240], [239, 241]]}

import pytest
from ansible.module_utils.common.validation import check_required_arguments

def test_check_required_arguments_no_argument_spec():
    assert check_required_arguments(None, {}) == []

def test_check_required_arguments_no_missing_params():
    argument_spec = {
        'param1': {'required': True},
        'param2': {'required': False},
    }
    parameters = {'param1': 'value1'}
    assert check_required_arguments(argument_spec, parameters) == []

def test_check_required_arguments_missing_params():
    argument_spec = {
        'param1': {'required': True},
        'param2': {'required': True},
    }
    parameters = {'param1': 'value1'}
    with pytest.raises(TypeError, match="missing required arguments: param2"):
        check_required_arguments(argument_spec, parameters)

def test_check_required_arguments_with_options_context():
    argument_spec = {
        'param1': {'required': True},
        'param2': {'required': True},
    }
    parameters = {'param1': 'value1'}
    options_context = ['parent']
    with pytest.raises(TypeError, match="missing required arguments: param2 found in parent"):
        check_required_arguments(argument_spec, parameters, options_context)
