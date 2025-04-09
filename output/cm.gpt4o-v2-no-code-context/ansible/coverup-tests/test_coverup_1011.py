# file: lib/ansible/module_utils/common/validation.py:414-465
# asked: {"lines": [442, 443, 445, 463], "branches": [[435, 463], [441, 442], [444, 445], [459, 461]]}
# gained: {"lines": [442, 443, 445], "branches": [[441, 442], [444, 445]]}

import pytest
from ansible.module_utils.common.validation import check_type_dict

def test_check_type_dict_with_escaped_characters():
    value = "key1=value1\\,with\\,commas,key2=value2"
    expected = {"key1": "value1,with,commas", "key2": "value2"}
    result = check_type_dict(value)
    assert result == expected

def test_check_type_dict_with_invalid_json():
    value = "{invalid_json: true}"
    with pytest.raises(TypeError, match="unable to evaluate string as dictionary"):
        check_type_dict(value)

def test_check_type_dict_with_key_value_string():
    value = "key1=value1, key2=value2"
    expected = {"key1": "value1", "key2": "value2"}
    result = check_type_dict(value)
    assert result == expected

def test_check_type_dict_with_invalid_key_value_string():
    value = "key1=value1, key2"
    with pytest.raises(ValueError, match="dictionary update sequence element #1 has length 1; 2 is required"):
        check_type_dict(value)

def test_check_type_dict_with_non_convertible_type():
    value = 12345
    with pytest.raises(TypeError, match="cannot be converted to a dict"):
        check_type_dict(value)
