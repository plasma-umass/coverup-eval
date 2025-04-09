# file: lib/ansible/module_utils/common/validation.py:391-411
# asked: {"lines": [391, 403, 404, 406, 407, 408, 409, 411], "branches": [[403, 404], [403, 406], [406, 407], [406, 408], [408, 409], [408, 411]]}
# gained: {"lines": [391, 403, 404, 406, 407, 408, 409, 411], "branches": [[403, 404], [403, 406], [406, 407], [406, 408], [408, 409], [408, 411]]}

import pytest
from ansible.module_utils.common.validation import check_type_list

def test_check_type_list_with_list():
    value = [1, 2, 3]
    result = check_type_list(value)
    assert result == value

def test_check_type_list_with_comma_separated_string():
    value = "a,b,c"
    result = check_type_list(value)
    assert result == ["a", "b", "c"]

def test_check_type_list_with_int():
    value = 42
    result = check_type_list(value)
    assert result == ["42"]

def test_check_type_list_with_float():
    value = 3.14
    result = check_type_list(value)
    assert result == ["3.14"]

def test_check_type_list_with_invalid_type():
    value = {"key": "value"}
    with pytest.raises(TypeError) as excinfo:
        check_type_list(value)
    assert str(excinfo.value) == "<class 'dict'> cannot be converted to a list"
