# file lib/ansible/module_utils/common/validation.py:367-388
# lines [367, 381, 382, 384, 385, 387, 388]
# branches ['381->382', '381->384', '384->385', '384->387']

import pytest
from ansible.module_utils.common.validation import check_type_str
from ansible.module_utils._text import to_native
from ansible.module_utils.six import string_types

def test_check_type_str_string():
    assert check_type_str("test") == "test"

def test_check_type_str_conversion_allowed():
    assert check_type_str(123, allow_conversion=True) == "123"

def test_check_type_str_conversion_not_allowed():
    with pytest.raises(TypeError) as excinfo:
        check_type_str(123, allow_conversion=False)
    assert str(excinfo.value) == to_native("'123' is not a string and conversion is not allowed")

def test_check_type_str_with_param_and_prefix():
    assert check_type_str("test", param="param", prefix="prefix") == "test"

def test_check_type_str_non_string_with_param_and_prefix():
    with pytest.raises(TypeError) as excinfo:
        check_type_str(123, allow_conversion=False, param="param", prefix="prefix")
    assert str(excinfo.value) == to_native("'123' is not a string and conversion is not allowed")
