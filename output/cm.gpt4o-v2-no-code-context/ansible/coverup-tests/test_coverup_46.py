# file: lib/ansible/module_utils/common/parameters.py:347-369
# asked: {"lines": [347, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 365, 366, 367, 369], "branches": [[351, 352], [351, 355], [352, 353], [352, 354], [355, 356], [355, 359], [356, 0], [356, 357], [357, 356], [357, 358], [359, 360], [359, 363], [360, 0], [360, 361], [361, 360], [361, 362], [363, 365], [363, 366], [366, 367], [366, 369]]}
# gained: {"lines": [347, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 365, 366, 367, 369], "branches": [[351, 352], [351, 355], [352, 353], [352, 354], [355, 356], [355, 359], [356, 0], [356, 357], [357, 356], [357, 358], [359, 360], [359, 363], [360, 0], [360, 361], [361, 360], [361, 362], [363, 365], [363, 366], [366, 367], [366, 369]]}

import pytest
from ansible.module_utils.common.parameters import _return_datastructure_name
from ansible.module_utils._text import to_native, text_type, binary_type
from collections.abc import Mapping
from ansible.module_utils.common.collections import is_iterable
from ansible.module_utils.six import integer_types

def test_return_datastructure_name_text_type():
    result = list(_return_datastructure_name("test string"))
    assert result == ["test string"]

def test_return_datastructure_name_binary_type():
    result = list(_return_datastructure_name(b"test string"))
    assert result == ["test string"]

def test_return_datastructure_name_empty_string():
    result = list(_return_datastructure_name(""))
    assert result == []

def test_return_datastructure_name_mapping():
    obj = {"key1": "value1", "key2": "value2"}
    result = list(_return_datastructure_name(obj))
    assert result == ["value1", "value2"]

def test_return_datastructure_name_iterable():
    obj = ["value1", "value2"]
    result = list(_return_datastructure_name(obj))
    assert result == ["value1", "value2"]

def test_return_datastructure_name_bool():
    result = list(_return_datastructure_name(True))
    assert result == []

def test_return_datastructure_name_none():
    result = list(_return_datastructure_name(None))
    assert result == []

def test_return_datastructure_name_integer():
    result = list(_return_datastructure_name(42))
    assert result == ["42"]

def test_return_datastructure_name_float():
    result = list(_return_datastructure_name(3.14))
    assert result == ["3.14"]

def test_return_datastructure_name_unknown_type():
    with pytest.raises(TypeError, match="Unknown parameter type: <class 'object'>"):
        list(_return_datastructure_name(object()))
