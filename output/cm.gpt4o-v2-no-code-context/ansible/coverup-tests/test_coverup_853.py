# file: lib/ansible/module_utils/common/validation.py:538-540
# asked: {"lines": [538, 540], "branches": []}
# gained: {"lines": [538, 540], "branches": []}

import pytest
from ansible.module_utils.common.validation import check_type_raw

def test_check_type_raw_with_string():
    value = "test_string"
    result = check_type_raw(value)
    assert result == value

def test_check_type_raw_with_int():
    value = 123
    result = check_type_raw(value)
    assert result == value

def test_check_type_raw_with_list():
    value = [1, 2, 3]
    result = check_type_raw(value)
    assert result == value

def test_check_type_raw_with_dict():
    value = {"key": "value"}
    result = check_type_raw(value)
    assert result == value

def test_check_type_raw_with_none():
    value = None
    result = check_type_raw(value)
    assert result == value
