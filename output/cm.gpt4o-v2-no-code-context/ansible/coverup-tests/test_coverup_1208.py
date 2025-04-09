# file: lib/ansible/module_utils/common/validation.py:414-465
# asked: {"lines": [], "branches": [[459, 461]]}
# gained: {"lines": [], "branches": [[459, 461]]}

import pytest
from ansible.module_utils.common.validation import check_type_dict

def test_check_type_dict_with_key_value_string():
    value = "key1=value1, key2=value2"
    expected_result = {"key1": "value1", "key2": "value2"}
    result = check_type_dict(value)
    assert result == expected_result

def test_check_type_dict_with_key_value_string_trailing_comma():
    value = "key1=value1, key2=value2, "
    expected_result = {"key1": "value1", "key2": "value2"}
    result = check_type_dict(value)
    assert result == expected_result

def test_check_type_dict_with_key_value_string_with_quotes():
    value = 'key1="value1, still value1", key2=value2'
    expected_result = {"key1": "value1, still value1", "key2": "value2"}
    result = check_type_dict(value)
    assert result == expected_result

def test_check_type_dict_with_key_value_string_with_escaped_characters():
    value = r'key1=value1\,with\,commas, key2=value2'
    expected_result = {"key1": "value1,with,commas", "key2": "value2"}
    result = check_type_dict(value)
    assert result == expected_result

def test_check_type_dict_with_invalid_key_value_string():
    value = "key1=value1, key2"
    with pytest.raises(ValueError, match="dictionary update sequence element #1 has length 1; 2 is required"):
        check_type_dict(value)
