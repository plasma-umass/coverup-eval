# file: lib/ansible/module_utils/common/validation.py:391-411
# asked: {"lines": [391, 403, 404, 406, 407, 408, 409, 411], "branches": [[403, 404], [403, 406], [406, 407], [406, 408], [408, 409], [408, 411]]}
# gained: {"lines": [391, 403, 404, 406, 407, 408, 409, 411], "branches": [[403, 404], [403, 406], [406, 407], [406, 408], [408, 409], [408, 411]]}

import pytest
from ansible.module_utils.common.validation import check_type_list

def test_check_type_list_with_list():
    assert check_type_list([1, 2, 3]) == [1, 2, 3]

def test_check_type_list_with_comma_separated_string():
    assert check_type_list("a,b,c") == ["a", "b", "c"]

def test_check_type_list_with_string_without_comma():
    assert check_type_list("abc") == ["abc"]

def test_check_type_list_with_int():
    assert check_type_list(123) == ["123"]

def test_check_type_list_with_float():
    assert check_type_list(123.45) == ["123.45"]

def test_check_type_list_with_invalid_type():
    with pytest.raises(TypeError):
        check_type_list({'a': 1})
