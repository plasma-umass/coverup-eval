# file: lib/ansible/module_utils/common/parameters.py:347-369
# asked: {"lines": [351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 365, 366, 367, 369], "branches": [[351, 352], [351, 355], [352, 353], [352, 354], [355, 356], [355, 359], [356, 0], [356, 357], [357, 356], [357, 358], [359, 360], [359, 363], [360, 0], [360, 361], [361, 360], [361, 362], [363, 365], [363, 366], [366, 367], [366, 369]]}
# gained: {"lines": [351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 365, 366, 367, 369], "branches": [[351, 352], [351, 355], [352, 353], [352, 354], [355, 356], [355, 359], [356, 0], [356, 357], [357, 356], [357, 358], [359, 360], [359, 363], [360, 0], [360, 361], [361, 360], [361, 362], [363, 365], [363, 366], [366, 367], [366, 369]]}

import pytest
from ansible.module_utils.common.parameters import _return_datastructure_name
from ansible.module_utils._text import to_native, text_type, binary_type
from collections.abc import Mapping
from ansible.module_utils.six import integer_types, string_types, text_type, binary_type
from ansible.module_utils.six.moves import collections_abc
from ansible.module_utils.common.collections import is_iterable

def test_return_datastructure_name_string():
    result = list(_return_datastructure_name("test"))
    assert result == ["test"]

def test_return_datastructure_name_empty_string():
    result = list(_return_datastructure_name(""))
    assert result == []

def test_return_datastructure_name_bytes():
    result = list(_return_datastructure_name(b"test"))
    assert result == ["test"]

def test_return_datastructure_name_mapping():
    result = list(_return_datastructure_name({"key": "value"}))
    assert result == ["value"]

def test_return_datastructure_name_nested_mapping():
    result = list(_return_datastructure_name({"key": {"subkey": "subvalue"}}))
    assert result == ["subvalue"]

def test_return_datastructure_name_iterable():
    result = list(_return_datastructure_name(["value1", "value2"]))
    assert result == ["value1", "value2"]

def test_return_datastructure_name_nested_iterable():
    result = list(_return_datastructure_name([["value1"], ["value2"]]))
    assert result == ["value1", "value2"]

def test_return_datastructure_name_bool():
    result = list(_return_datastructure_name(True))
    assert result == []

def test_return_datastructure_name_none():
    result = list(_return_datastructure_name(None))
    assert result == []

def test_return_datastructure_name_int():
    result = list(_return_datastructure_name(42))
    assert result == ["42"]

def test_return_datastructure_name_float():
    result = list(_return_datastructure_name(3.14))
    assert result == ["3.14"]

def test_return_datastructure_name_unknown_type():
    with pytest.raises(TypeError, match="Unknown parameter type: <class 'complex'>"):
        list(_return_datastructure_name(1+2j))
