# file: lib/ansible/module_utils/common/validation.py:567-578
# asked: {"lines": [567, 574, 575, 576, 577, 578], "branches": [[574, 575], [574, 576], [576, 577], [576, 578]]}
# gained: {"lines": [567, 574, 575, 576, 577, 578], "branches": [[574, 575], [574, 576], [576, 577], [576, 578]]}

import pytest
from ansible.module_utils.common.validation import check_type_jsonarg
from ansible.module_utils._text import to_text as text_type, to_bytes as binary_type
import json

def test_check_type_jsonarg_string():
    assert check_type_jsonarg("  test  ") == "test"

def test_check_type_jsonarg_binary():
    assert check_type_jsonarg(b"  test  ") == b"test"

def test_check_type_jsonarg_list():
    assert check_type_jsonarg([1, 2, 3]) == json.dumps([1, 2, 3])

def test_check_type_jsonarg_tuple():
    assert check_type_jsonarg((1, 2, 3)) == json.dumps((1, 2, 3))

def test_check_type_jsonarg_dict():
    assert check_type_jsonarg({"key": "value"}) == json.dumps({"key": "value"})

def test_check_type_jsonarg_invalid_type():
    with pytest.raises(TypeError):
        check_type_jsonarg(123)
