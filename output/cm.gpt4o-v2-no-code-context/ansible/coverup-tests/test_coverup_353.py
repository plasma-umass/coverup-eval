# file: lib/ansible/module_utils/common/validation.py:367-388
# asked: {"lines": [367, 381, 382, 384, 385, 387, 388], "branches": [[381, 382], [381, 384], [384, 385], [384, 387]]}
# gained: {"lines": [367, 381, 382, 384, 385, 387, 388], "branches": [[381, 382], [381, 384], [384, 385], [384, 387]]}

import pytest
from ansible.module_utils.common.validation import check_type_str

def test_check_type_str_with_string():
    assert check_type_str("test") == "test"

def test_check_type_str_with_non_string_conversion_allowed():
    assert check_type_str(123, allow_conversion=True) == "123"

def test_check_type_str_with_non_string_conversion_not_allowed():
    with pytest.raises(TypeError) as excinfo:
        check_type_str(123, allow_conversion=False)
    assert "'123' is not a string and conversion is not allowed" in str(excinfo.value)

def test_check_type_str_with_param_and_prefix():
    assert check_type_str("test", param="param", prefix="prefix") == "test"

def test_check_type_str_with_non_string_and_param_prefix_conversion_allowed():
    assert check_type_str(123, allow_conversion=True, param="param", prefix="prefix") == "123"

def test_check_type_str_with_non_string_and_param_prefix_conversion_not_allowed():
    with pytest.raises(TypeError) as excinfo:
        check_type_str(123, allow_conversion=False, param="param", prefix="prefix")
    assert "'123' is not a string and conversion is not allowed" in str(excinfo.value)
