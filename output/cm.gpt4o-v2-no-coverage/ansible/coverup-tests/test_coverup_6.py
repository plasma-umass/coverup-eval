# file: lib/ansible/module_utils/common/arg_spec.py:142-254
# asked: {"lines": [142, 176, 178, 180, 181, 182, 183, 184, 185, 186, 188, 190, 191, 193, 194, 195, 196, 197, 198, 201, 202, 203, 204, 206, 207, 208, 209, 210, 211, 213, 214, 215, 216, 218, 220, 221, 222, 223, 225, 226, 228, 229, 230, 231, 232, 234, 236, 237, 238, 239, 241, 242, 243, 244, 245, 247, 249, 250, 251, 252, 254], "branches": [[190, 191], [190, 193], [193, 194], [193, 201], [228, 229], [228, 234], [241, 242], [241, 254], [243, 244], [243, 249], [244, 245], [244, 247]]}
# gained: {"lines": [142, 176, 178, 180, 181, 182, 183, 188, 190, 193, 201, 202, 206, 207, 213, 214, 215, 216, 218, 220, 221, 222, 223, 225, 226, 228, 229, 230, 234, 236, 237, 238, 239, 241, 242, 243, 244, 247, 249, 250, 251, 252, 254], "branches": [[190, 193], [193, 201], [228, 229], [228, 234], [241, 242], [241, 254], [243, 244], [243, 249], [244, 247]]}

import pytest
from ansible.module_utils.common.arg_spec import ArgumentSpecValidator
from ansible.module_utils.errors import AliasError, MutuallyExclusiveError, NoLogError, RequiredDefaultError, RequiredError, UnsupportedError

@pytest.fixture
def argument_spec():
    return {
        'name': {'type': 'str'},
        'age': {'type': 'int', 'aliases': ['years']},
        'email': {'type': 'str', 'no_log': True},
        'country': {'type': 'str', 'required': True},
    }

@pytest.fixture
def validator(argument_spec):
    return ArgumentSpecValidator(argument_spec)

def test_validate_success(validator):
    parameters = {
        'name': 'John Doe',
        'age': 30,
        'email': 'john.doe@example.com',
        'country': 'Wonderland'
    }
    result = validator.validate(parameters)
    assert not result.errors.errors
    assert result._validated_parameters == parameters

def test_validate_alias(validator):
    parameters = {
        'name': 'John Doe',
        'years': 30,
        'email': 'john.doe@example.com',
        'country': 'Wonderland'
    }
    result = validator.validate(parameters)
    assert not result.errors.errors
    assert result._validated_parameters['age'] == 30

def test_validate_no_log(validator):
    parameters = {
        'name': 'John Doe',
        'age': 30,
        'email': 'john.doe@example.com',
        'country': 'Wonderland'
    }
    result = validator.validate(parameters)
    assert 'john.doe@example.com' in result._no_log_values

def test_validate_required(validator):
    parameters = {
        'name': 'John Doe',
        'age': 30,
        'email': 'john.doe@example.com'
    }
    result = validator.validate(parameters)
    assert result.errors.errors
    assert isinstance(result.errors.errors[0], RequiredError)

def test_validate_unsupported(validator):
    parameters = {
        'name': 'John Doe',
        'age': 30,
        'email': 'john.doe@example.com',
        'country': 'Wonderland',
        'unsupported_param': 'value'
    }
    result = validator.validate(parameters)
    assert result.errors.errors
    assert isinstance(result.errors.errors[0], UnsupportedError)

def test_validate_mutually_exclusive():
    argument_spec = {
        'param1': {'type': 'str'},
        'param2': {'type': 'str'},
    }
    validator = ArgumentSpecValidator(argument_spec, mutually_exclusive=[['param1', 'param2']])
    parameters = {
        'param1': 'value1',
        'param2': 'value2'
    }
    result = validator.validate(parameters)
    assert result.errors.errors
    assert isinstance(result.errors.errors[0], MutuallyExclusiveError)
