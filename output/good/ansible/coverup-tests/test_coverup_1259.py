# file lib/ansible/module_utils/common/arg_spec.py:42-84
# lines [55, 56, 60, 61, 62, 63, 64, 65, 74, 79, 84]
# branches []

import pytest
from ansible.module_utils.common.arg_spec import ValidationResult
from ansible.module_utils.errors import AnsibleValidationError, AnsibleValidationErrorMultiple

@pytest.fixture
def validation_result():
    return ValidationResult(parameters={'param1': 'value1', 'param2': 'value2'})

def test_validation_result_properties(validation_result):
    # Access the validated_parameters property
    assert validation_result.validated_parameters == {'param1': 'value1', 'param2': 'value2'}
    
    # Access the unsupported_parameters property
    assert validation_result.unsupported_parameters == set()
    
    # Access the error_messages property without errors
    assert validation_result.error_messages == []
    
    # Add an error and check error_messages property again
    error = AnsibleValidationError('Test error')
    validation_result.errors = AnsibleValidationErrorMultiple(errors=[error])
    assert validation_result.error_messages == [str(error)]
