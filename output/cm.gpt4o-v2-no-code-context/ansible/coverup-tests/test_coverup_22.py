# file: lib/ansible/utils/context_objects.py:20-50
# asked: {"lines": [20, 22, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 47, 48, 50], "branches": [[22, 24], [22, 25], [25, 26], [25, 33], [27, 28], [27, 32], [28, 29], [28, 31], [33, 34], [33, 41], [35, 36], [35, 40], [36, 37], [36, 39], [41, 42], [41, 50], [43, 44], [43, 48], [44, 45], [44, 47]]}
# gained: {"lines": [20, 22, 24, 25, 26, 27, 28, 29, 32, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 48, 50], "branches": [[22, 24], [22, 25], [25, 26], [25, 33], [27, 28], [27, 32], [28, 29], [33, 34], [33, 41], [35, 36], [35, 40], [36, 37], [41, 42], [41, 50], [43, 44], [43, 48], [44, 45]]}

import pytest
from collections.abc import Mapping, Set, Sequence, Container
from ansible.utils.context_objects import _make_immutable, ImmutableDict

def test_make_immutable_string():
    assert _make_immutable("test") == "test"
    assert _make_immutable(b"test") == b"test"

def test_make_immutable_mapping(monkeypatch):
    class MockImmutableDict(dict):
        pass

    monkeypatch.setattr("ansible.utils.context_objects.ImmutableDict", MockImmutableDict)
    
    input_dict = {"key1": "value1", "key2": {"nested_key": "nested_value"}}
    result = _make_immutable(input_dict)
    
    assert isinstance(result, MockImmutableDict)
    assert result["key1"] == "value1"
    assert isinstance(result["key2"], MockImmutableDict)
    assert result["key2"]["nested_key"] == "nested_value"

def test_make_immutable_set():
    input_set = {"value1", frozenset({"nested_value"})}
    result = _make_immutable(input_set)
    
    assert isinstance(result, frozenset)
    assert "value1" in result
    assert frozenset({"nested_value"}) in result

def test_make_immutable_sequence():
    input_list = ["value1", ["nested_value"]]
    result = _make_immutable(input_list)
    
    assert isinstance(result, tuple)
    assert result[0] == "value1"
    assert isinstance(result[1], tuple)
    assert result[1][0] == "nested_value"

def test_make_immutable_other():
    input_obj = 42
    assert _make_immutable(input_obj) == 42
