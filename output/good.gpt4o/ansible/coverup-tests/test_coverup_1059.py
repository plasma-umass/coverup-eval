# file lib/ansible/module_utils/common/parameters.py:541-566
# lines [543, 544, 546, 547, 550, 551, 552, 553, 554, 555, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566]
# branches ['543->544', '543->546', '551->552', '551->557', '552->553', '552->554', '554->555', '554->557', '557->558', '557->566', '562->563', '562->564']

import pytest
from ansible.module_utils.common.parameters import _validate_elements, AnsibleValidationErrorMultiple, ElementError
from ansible.module_utils._text import to_native
from ansible.module_utils.six import string_types

def test_validate_elements_with_errors(mocker):
    # Mocking _get_type_validator to return a type checker that raises an error
    def mock_type_validator(value, **kwargs):
        raise ValueError("mock error")

    mocker.patch('ansible.module_utils.common.parameters._get_type_validator', return_value=(mock_type_validator, 'str'))

    parameter = 'test_param'
    values = ['value1', 'value2']
    options_context = ['context1', 'context2']

    errors = AnsibleValidationErrorMultiple()
    result = _validate_elements('str', parameter, values, options_context, errors)

    assert len(result) == 0
    assert len(errors.errors) == 2
    assert isinstance(errors.errors[0], ElementError)
    assert "Elements value for option 'test_param' found in 'context1 -> context2' is of type <class 'str'> and we were unable to convert to str: mock error" in str(errors.errors[0])

def test_validate_elements_without_errors(mocker):
    # Mocking _get_type_validator to return a type checker that works correctly
    def mock_type_validator(value, **kwargs):
        return value

    mocker.patch('ansible.module_utils.common.parameters._get_type_validator', return_value=(mock_type_validator, 'str'))

    parameter = 'test_param'
    values = ['value1', 'value2']
    options_context = ['context1', 'context2']

    result = _validate_elements('str', parameter, values, options_context)

    assert result == values

def test_validate_elements_with_param_as_dict(mocker):
    # Mocking _get_type_validator to return a type checker that works correctly
    def mock_type_validator(value, **kwargs):
        return value

    mocker.patch('ansible.module_utils.common.parameters._get_type_validator', return_value=(mock_type_validator, 'str'))

    parameter = {'test_param': 'value'}
    values = ['value1', 'value2']
    options_context = ['context1', 'context2']

    result = _validate_elements('str', parameter, values, options_context)

    assert result == values
