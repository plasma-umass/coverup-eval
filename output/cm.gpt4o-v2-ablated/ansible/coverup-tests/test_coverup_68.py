# file: lib/ansible/module_utils/common/arg_spec.py:42-84
# asked: {"lines": [42, 43, 50, 55, 56, 60, 61, 62, 63, 64, 65, 71, 72, 74, 76, 77, 79, 81, 82, 84], "branches": []}
# gained: {"lines": [42, 43, 50, 55, 56, 60, 61, 62, 63, 64, 65, 71, 72, 74, 76, 77, 79, 81, 82, 84], "branches": []}

import pytest
from copy import deepcopy
from ansible.module_utils.errors import AnsibleValidationErrorMultiple

# Assuming the ValidationResult class is imported from ansible/module_utils/common/arg_spec.py
from ansible.module_utils.common.arg_spec import ValidationResult

@pytest.fixture
def mock_parameters():
    return {
        'param1': 'value1',
        'param2': 'value2'
    }

def test_validation_result_initialization(mock_parameters):
    result = ValidationResult(mock_parameters)
    
    assert result._no_log_values == set()
    assert result._unsupported_parameters == set()
    assert result._validated_parameters == deepcopy(mock_parameters)
    assert result._deprecations == []
    assert result._warnings == []
    assert isinstance(result.errors, AnsibleValidationErrorMultiple)

def test_validated_parameters_property(mock_parameters):
    result = ValidationResult(mock_parameters)
    assert result.validated_parameters == deepcopy(mock_parameters)

def test_unsupported_parameters_property(mock_parameters):
    result = ValidationResult(mock_parameters)
    assert result.unsupported_parameters == set()

def test_error_messages_property(mock_parameters):
    result = ValidationResult(mock_parameters)
    assert result.error_messages == result.errors.messages
