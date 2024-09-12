# file: lib/ansible/utils/context_objects.py:20-50
# asked: {"lines": [20, 22, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 47, 48, 50], "branches": [[22, 24], [22, 25], [25, 26], [25, 33], [27, 28], [27, 32], [28, 29], [28, 31], [33, 34], [33, 41], [35, 36], [35, 40], [36, 37], [36, 39], [41, 42], [41, 50], [43, 44], [43, 48], [44, 45], [44, 47]]}
# gained: {"lines": [20, 22, 24, 25, 26, 27, 28, 29, 32, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 48, 50], "branches": [[22, 24], [22, 25], [25, 26], [25, 33], [27, 28], [27, 32], [28, 29], [33, 34], [33, 41], [35, 36], [35, 40], [36, 37], [41, 42], [41, 50], [43, 44], [43, 48], [44, 45]]}

import pytest
from ansible.module_utils.common._collections_compat import Container, Mapping, Sequence, Set
from ansible.module_utils.common.collections import ImmutableDict
from ansible.module_utils.six import binary_type, text_type
from ansible.utils.context_objects import _make_immutable

def test_make_immutable_with_text_type():
    obj = text_type("test string")
    result = _make_immutable(obj)
    assert result == obj

def test_make_immutable_with_binary_type():
    obj = binary_type(b"test bytes")
    result = _make_immutable(obj)
    assert result == obj

def test_make_immutable_with_mapping():
    obj = {"key1": "value1", "key2": {"subkey": "subvalue"}}
    result = _make_immutable(obj)
    assert isinstance(result, ImmutableDict)
    assert result["key1"] == "value1"
    assert isinstance(result["key2"], ImmutableDict)
    assert result["key2"]["subkey"] == "subvalue"

def test_make_immutable_with_set():
    obj = {"value1", "value2", frozenset({"subvalue1", "subvalue2"})}
    result = _make_immutable(obj)
    assert isinstance(result, frozenset)
    assert "value1" in result
    assert "value2" in result
    assert any(isinstance(item, frozenset) and "subvalue1" in item for item in result)

def test_make_immutable_with_sequence():
    obj = ["value1", "value2", ["subvalue1", "subvalue2"]]
    result = _make_immutable(obj)
    assert isinstance(result, tuple)
    assert result[0] == "value1"
    assert result[1] == "value2"
    assert isinstance(result[2], tuple)
    assert result[2][0] == "subvalue1"
    assert result[2][1] == "subvalue2"

def test_make_immutable_with_other():
    obj = 12345
    result = _make_immutable(obj)
    assert result == obj
