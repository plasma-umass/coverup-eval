# file: lib/ansible/module_utils/common/validation.py:567-578
# asked: {"lines": [567, 574, 575, 576, 577, 578], "branches": [[574, 575], [574, 576], [576, 577], [576, 578]]}
# gained: {"lines": [567, 574, 575, 576, 577, 578], "branches": [[574, 575], [574, 576], [576, 577], [576, 578]]}

import pytest
from ansible.module_utils.common.validation import check_type_jsonarg
from ansible.module_utils.six import binary_type, text_type

def test_check_type_jsonarg_with_text_type():
    value = text_type("  some text  ")
    result = check_type_jsonarg(value)
    assert result == "some text"

def test_check_type_jsonarg_with_binary_type():
    value = binary_type(b"  some binary text  ")
    result = check_type_jsonarg(value)
    assert result == b"some binary text"

def test_check_type_jsonarg_with_list():
    value = [1, 2, 3]
    result = check_type_jsonarg(value)
    assert result == '[1, 2, 3]'

def test_check_type_jsonarg_with_tuple():
    value = (1, 2, 3)
    result = check_type_jsonarg(value)
    assert result == '[1, 2, 3]'

def test_check_type_jsonarg_with_dict():
    value = {"key": "value"}
    result = check_type_jsonarg(value)
    assert result == '{"key": "value"}'

def test_check_type_jsonarg_with_invalid_type():
    value = 12345
    with pytest.raises(TypeError, match="cannot be converted to a json string"):
        check_type_jsonarg(value)
