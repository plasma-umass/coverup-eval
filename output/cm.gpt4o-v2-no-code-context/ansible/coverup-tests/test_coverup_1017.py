# file: lib/ansible/utils/context_objects.py:20-50
# asked: {"lines": [31, 39, 47], "branches": [[28, 31], [36, 39], [44, 47]]}
# gained: {"lines": [31, 39, 47], "branches": [[28, 31], [36, 39], [44, 47]]}

import pytest
from collections.abc import Mapping, Set, Sequence, Container
from ansible.utils.context_objects import _make_immutable, ImmutableDict

def test_make_immutable_with_mapping(monkeypatch):
    class MockImmutableDict(dict):
        pass

    monkeypatch.setattr('ansible.utils.context_objects.ImmutableDict', MockImmutableDict)

    input_data = {'key1': 'value1', 'key2': 2, 'key3': [1, 2, 3]}
    result = _make_immutable(input_data)
    assert isinstance(result, MockImmutableDict)
    assert result['key1'] == 'value1'
    assert result['key2'] == 2
    assert result['key3'] == (1, 2, 3)

def test_make_immutable_with_set():
    input_data = {'value1', 2, (1, 2, 3)}
    result = _make_immutable(input_data)
    assert isinstance(result, frozenset)
    assert 'value1' in result
    assert 2 in result
    assert (1, 2, 3) in result

def test_make_immutable_with_sequence():
    input_data = ['value1', 2, {'key': 'value'}]
    result = _make_immutable(input_data)
    assert isinstance(result, tuple)
    assert result[0] == 'value1'
    assert result[1] == 2
    assert result[2] == ImmutableDict({'key': 'value'})
