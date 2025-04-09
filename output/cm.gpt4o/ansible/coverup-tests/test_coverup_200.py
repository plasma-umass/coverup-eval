# file lib/ansible/module_utils/common/arg_spec.py:42-84
# lines [42, 43, 50, 55, 56, 60, 61, 62, 63, 64, 65, 71, 72, 74, 76, 77, 79, 81, 82, 84]
# branches []

import pytest
from ansible.module_utils.common.arg_spec import ValidationResult
from ansible.module_utils.errors import AnsibleValidationError, AnsibleValidationErrorMultiple

def test_validation_result():
    parameters = {
        'param1': 'value1',
        'param2': 'value2'
    }
    
    # Create an instance of ValidationResult
    result = ValidationResult(parameters)
    
    # Check that the validated parameters are correctly set
    assert result.validated_parameters == parameters
    
    # Check that unsupported parameters set is empty
    assert result.unsupported_parameters == set()
    
    # Check that error messages list is empty
    assert result.error_messages == []
    
    # Add an unsupported parameter and check again
    result._unsupported_parameters.add('unsupported_param')
    assert result.unsupported_parameters == {'unsupported_param'}
    
    # Add an error and check error messages
    error = AnsibleValidationError('Test error message')
    result.errors.errors.append(error)
    assert result.error_messages == ['Test error message']
