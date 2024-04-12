# file lib/ansible/module_utils/common/parameters.py:123-147
# lines [123, 135, 136, 138, 140, 144, 145, 147]
# branches ['135->136', '135->144', '136->138', '136->140']

import pytest
from ansible.module_utils.common.parameters import _get_type_validator
from ansible.module_utils._text import to_native

# Mock DEFAULT_TYPE_VALIDATORS for testing purposes
DEFAULT_TYPE_VALIDATORS = {
    'str': str,
    'int': int,
    'float': float,
    'bool': bool,
}

@pytest.fixture
def mock_default_type_validators(mocker):
    mocker.patch('ansible.module_utils.common.parameters.DEFAULT_TYPE_VALIDATORS', DEFAULT_TYPE_VALIDATORS)

def custom_validator(value):
    return isinstance(value, list)

def test_get_type_validator_with_string(mock_default_type_validators):
    type_checker, type_name = _get_type_validator('str')
    assert type_checker == str
    assert type_name == 'str'

    type_checker, type_name = _get_type_validator('int')
    assert type_checker == int
    assert type_name == 'int'

    type_checker, type_name = _get_type_validator(None)
    assert type_checker == str
    assert type_name == 'str'

def test_get_type_validator_with_callable(mock_default_type_validators):
    type_checker, type_name = _get_type_validator(custom_validator)
    assert type_checker == custom_validator
    assert type_name == 'custom_validator'

def test_get_type_validator_with_unregistered_type(mock_default_type_validators):
    type_checker, type_name = _get_type_validator('unregistered')
    assert type_checker is None
    assert type_name == 'unregistered'
