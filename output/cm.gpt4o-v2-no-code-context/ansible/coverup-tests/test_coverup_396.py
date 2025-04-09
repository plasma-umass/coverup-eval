# file: lib/ansible/module_utils/common/validation.py:567-578
# asked: {"lines": [567, 574, 575, 576, 577, 578], "branches": [[574, 575], [574, 576], [576, 577], [576, 578]]}
# gained: {"lines": [567, 574, 575, 576, 577, 578], "branches": [[574, 575], [574, 576], [576, 577], [576, 578]]}

import pytest
import json
from ansible.module_utils.common.validation import check_type_jsonarg
from ansible.module_utils._text import to_text, to_bytes

def test_check_type_jsonarg_with_text_type():
    value = "  some string  "
    result = check_type_jsonarg(value)
    assert result == "some string"

def test_check_type_jsonarg_with_binary_type():
    value = b"  some binary string  "
    result = check_type_jsonarg(value)
    assert result == b"some binary string"

def test_check_type_jsonarg_with_list():
    value = [1, 2, 3]
    result = check_type_jsonarg(value)
    assert result == to_text(json.dumps(value))

def test_check_type_jsonarg_with_tuple():
    value = (1, 2, 3)
    result = check_type_jsonarg(value)
    assert result == to_text(json.dumps(value))

def test_check_type_jsonarg_with_dict():
    value = {"key": "value"}
    result = check_type_jsonarg(value)
    assert result == to_text(json.dumps(value))

def test_check_type_jsonarg_with_invalid_type():
    value = 12345
    with pytest.raises(TypeError) as excinfo:
        check_type_jsonarg(value)
    assert str(excinfo.value) == "<class 'int'> cannot be converted to a json string"
