# file: lib/ansible/module_utils/common/parameters.py:123-147
# asked: {"lines": [123, 135, 136, 138, 140, 144, 145, 147], "branches": [[135, 136], [135, 144], [136, 138], [136, 140]]}
# gained: {"lines": [123, 135, 136, 138, 140, 144, 145, 147], "branches": [[135, 136], [135, 144], [136, 138], [136, 140]]}

import pytest
from ansible.module_utils.common.parameters import _get_type_validator
from ansible.module_utils.common.validation import (
    check_type_str, check_type_list, check_type_dict, check_type_bool,
    check_type_int, check_type_float, check_type_path, check_type_raw,
    check_type_jsonarg, check_type_bytes, check_type_bits
)

DEFAULT_TYPE_VALIDATORS = {
    'str': check_type_str, 'list': check_type_list, 'dict': check_type_dict,
    'bool': check_type_bool, 'int': check_type_int, 'float': check_type_float,
    'path': check_type_path, 'raw': check_type_raw, 'jsonarg': check_type_jsonarg,
    'json': check_type_jsonarg, 'bytes': check_type_bytes, 'bits': check_type_bits
}

def test_get_type_validator_with_none():
    type_checker, type_name = _get_type_validator(None)
    assert type_checker == check_type_str
    assert type_name == 'str'

def test_get_type_validator_with_string():
    type_checker, type_name = _get_type_validator('int')
    assert type_checker == check_type_int
    assert type_name == 'int'

def test_get_type_validator_with_callable():
    def custom_validator(value):
        return True

    type_checker, type_name = _get_type_validator(custom_validator)
    assert type_checker == custom_validator
    assert type_name == 'custom_validator'

def test_get_type_validator_with_unknown_string():
    type_checker, type_name = _get_type_validator('unknown')
    assert type_checker is None
    assert type_name == 'unknown'
