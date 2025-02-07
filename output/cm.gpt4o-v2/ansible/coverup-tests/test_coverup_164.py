# file: lib/ansible/module_utils/common/arg_spec.py:42-84
# asked: {"lines": [42, 43, 50, 55, 56, 60, 61, 62, 63, 64, 65, 71, 72, 74, 76, 77, 79, 81, 82, 84], "branches": []}
# gained: {"lines": [42, 43, 50, 55, 56, 60, 61, 62, 63, 64, 65, 71, 72, 74, 76, 77, 79, 81, 82, 84], "branches": []}

import pytest
from copy import deepcopy
from ansible.module_utils.common.arg_spec import ValidationResult
from ansible.module_utils.errors import AnsibleValidationErrorMultiple, AnsibleValidationError

def test_validation_result_init():
    parameters = {'param1': 'value1', 'param2': 'value2'}
    result = ValidationResult(parameters)
    
    assert result._validated_parameters == parameters
    assert isinstance(result._no_log_values, set)
    assert isinstance(result._unsupported_parameters, set)
    assert isinstance(result.errors, AnsibleValidationErrorMultiple)
    assert result._deprecations == []
    assert result._warnings == []

def test_validated_parameters_property():
    parameters = {'param1': 'value1', 'param2': 'value2'}
    result = ValidationResult(parameters)
    
    assert result.validated_parameters == parameters

def test_unsupported_parameters_property():
    parameters = {'param1': 'value1', 'param2': 'value2'}
    result = ValidationResult(parameters)
    
    assert result.unsupported_parameters == set()

def test_error_messages_property():
    parameters = {'param1': 'value1', 'param2': 'value2'}
    result = ValidationResult(parameters)
    
    assert result.error_messages == []

def test_error_messages_with_errors():
    parameters = {'param1': 'value1', 'param2': 'value2'}
    result = ValidationResult(parameters)
    error1 = AnsibleValidationError("Error 1")
    error2 = AnsibleValidationError("Error 2")
    result.errors.append(error1)
    result.errors.append(error2)
    
    assert result.error_messages == [str(error1), str(error2)]
