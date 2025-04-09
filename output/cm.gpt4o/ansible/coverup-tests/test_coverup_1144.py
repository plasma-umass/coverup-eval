# file lib/ansible/module_utils/common/parameters.py:123-147
# lines [135, 136, 138, 140, 144, 145, 147]
# branches ['135->136', '135->144', '136->138', '136->140']

import pytest
from ansible.module_utils.common.parameters import _get_type_validator

# Mocking DEFAULT_TYPE_VALIDATORS for the purpose of this test
DEFAULT_TYPE_VALIDATORS = {
    'str': lambda x: isinstance(x, str),
    'int': lambda x: isinstance(x, int),
}

@pytest.fixture(autouse=True)
def mock_default_type_validators(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.parameters.DEFAULT_TYPE_VALIDATORS', DEFAULT_TYPE_VALIDATORS)

def test_get_type_validator_with_none():
    type_checker, type_name = _get_type_validator(None)
    assert type_name == 'str'
    assert type_checker is DEFAULT_TYPE_VALIDATORS['str']

def test_get_type_validator_with_builtin_type():
    type_checker, type_name = _get_type_validator('int')
    assert type_name == 'int'
    assert type_checker is DEFAULT_TYPE_VALIDATORS['int']

def test_get_type_validator_with_custom_callable():
    custom_validator = lambda x: isinstance(x, list)
    type_checker, type_name = _get_type_validator(custom_validator)
    assert type_name == '<lambda>'
    assert type_checker is custom_validator
