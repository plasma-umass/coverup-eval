# file: lib/ansible/module_utils/common/arg_spec.py:42-84
# asked: {"lines": [42, 43, 50, 55, 56, 60, 61, 62, 63, 64, 65, 71, 72, 74, 76, 77, 79, 81, 82, 84], "branches": []}
# gained: {"lines": [42, 43, 50, 55, 56, 60, 61, 62, 63, 64, 65, 71, 72, 74, 76, 77, 79, 81, 82, 84], "branches": []}

import pytest
from ansible.module_utils.common.arg_spec import ValidationResult
from ansible.module_utils.errors import AnsibleValidationErrorMultiple

@pytest.fixture
def validation_result():
    parameters = {'param1': 'value1', 'param2': 'value2'}
    return ValidationResult(parameters)

def test_validated_parameters(validation_result):
    assert validation_result.validated_parameters == {'param1': 'value1', 'param2': 'value2'}

def test_unsupported_parameters(validation_result):
    assert validation_result.unsupported_parameters == set()

def test_error_messages(validation_result):
    assert validation_result.error_messages == []

def test_no_log_values_initialization(validation_result):
    assert validation_result._no_log_values == set()

def test_deprecations_initialization(validation_result):
    assert validation_result._deprecations == []

def test_warnings_initialization(validation_result):
    assert validation_result._warnings == []

def test_errors_initialization(validation_result):
    assert isinstance(validation_result.errors, AnsibleValidationErrorMultiple)
