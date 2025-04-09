# file: lib/ansible/module_utils/common/parameters.py:123-147
# asked: {"lines": [123, 135, 136, 138, 140, 144, 145, 147], "branches": [[135, 136], [135, 144], [136, 138], [136, 140]]}
# gained: {"lines": [123, 135, 136, 138, 140, 144, 145, 147], "branches": [[135, 136], [135, 144], [136, 138], [136, 140]]}

import pytest
from ansible.module_utils.common.parameters import _get_type_validator

# Mocking DEFAULT_TYPE_VALIDATORS for testing purposes
DEFAULT_TYPE_VALIDATORS = {
    'str': lambda x: isinstance(x, str),
    'int': lambda x: isinstance(x, int),
}

def test_get_type_validator_with_builtin_type(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.parameters.DEFAULT_TYPE_VALIDATORS', DEFAULT_TYPE_VALIDATORS)
    type_checker, type_name = _get_type_validator('str')
    assert type_checker is not None
    assert type_name == 'str'
    assert type_checker('test') is True
    assert type_checker(123) is False

def test_get_type_validator_with_none(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.parameters.DEFAULT_TYPE_VALIDATORS', DEFAULT_TYPE_VALIDATORS)
    type_checker, type_name = _get_type_validator(None)
    assert type_checker is not None
    assert type_name == 'str'
    assert type_checker('test') is True
    assert type_checker(123) is False

def test_get_type_validator_with_custom_callable():
    custom_validator = lambda x: isinstance(x, list)
    type_checker, type_name = _get_type_validator(custom_validator)
    assert type_checker is custom_validator
    assert type_name == '<lambda>'
    assert type_checker([]) is True
    assert type_checker('test') is False

def test_get_type_validator_with_nonexistent_builtin_type(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.parameters.DEFAULT_TYPE_VALIDATORS', DEFAULT_TYPE_VALIDATORS)
    type_checker, type_name = _get_type_validator('nonexistent')
    assert type_checker is None
    assert type_name == 'nonexistent'
