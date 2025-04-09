# file: lib/ansible/module_utils/common/arg_spec.py:42-84
# asked: {"lines": [42, 43, 50, 55, 56, 60, 61, 62, 63, 64, 65, 71, 72, 74, 76, 77, 79, 81, 82, 84], "branches": []}
# gained: {"lines": [42, 43, 50, 55, 56, 60, 61, 62, 63, 64, 65, 71, 72, 74, 76, 77, 79, 81, 82, 84], "branches": []}

import pytest
from ansible.module_utils.common.arg_spec import ValidationResult
from ansible.module_utils.errors import AnsibleValidationErrorMultiple

def test_validation_result_init():
    params = {'param1': 'value1', 'param2': 'value2'}
    result = ValidationResult(params)
    
    assert result._validated_parameters == params
    assert isinstance(result.errors, AnsibleValidationErrorMultiple)
    assert result._no_log_values == set()
    assert result._unsupported_parameters == set()
    assert result._deprecations == []
    assert result._warnings == []

def test_validated_parameters_property():
    params = {'param1': 'value1', 'param2': 'value2'}
    result = ValidationResult(params)
    
    assert result.validated_parameters == params

def test_unsupported_parameters_property():
    params = {'param1': 'value1', 'param2': 'value2'}
    result = ValidationResult(params)
    
    assert result.unsupported_parameters == set()

def test_error_messages_property(mocker):
    params = {'param1': 'value1', 'param2': 'value2'}
    result = ValidationResult(params)
    
    mock_error = mocker.Mock()
    mock_error.messages = ['error1', 'error2']
    result.errors = mock_error
    
    assert result.error_messages == ['error1', 'error2']
