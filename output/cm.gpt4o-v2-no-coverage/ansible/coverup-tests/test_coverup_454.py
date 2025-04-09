# file: lib/ansible/module_utils/common/validation.py:367-388
# asked: {"lines": [367, 381, 382, 384, 385, 387, 388], "branches": [[381, 382], [381, 384], [384, 385], [384, 387]]}
# gained: {"lines": [367, 381, 382, 384, 385, 387, 388], "branches": [[381, 382], [381, 384], [384, 385], [384, 387]]}

import pytest
from ansible.module_utils.common.validation import check_type_str
from ansible.module_utils._text import to_native
from ansible.module_utils.six import string_types

def test_check_type_str_with_string():
    assert check_type_str("test") == "test"

def test_check_type_str_with_non_string_allow_conversion():
    assert check_type_str(123, allow_conversion=True) == to_native(123, errors='surrogate_or_strict')

def test_check_type_str_with_non_string_no_conversion():
    with pytest.raises(TypeError) as excinfo:
        check_type_str(123, allow_conversion=False)
    assert "'123' is not a string and conversion is not allowed" in str(excinfo.value)

def test_check_type_str_with_string_types():
    for string_type in string_types:
        assert check_type_str(string_type("test")) == "test"
