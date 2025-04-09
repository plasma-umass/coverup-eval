# file: lib/ansible/utils/context_objects.py:20-50
# asked: {"lines": [31, 39], "branches": [[28, 31], [36, 39]]}
# gained: {"lines": [31, 39], "branches": [[28, 31], [36, 39]]}

import pytest
from ansible.module_utils.common._collections_compat import Container, Mapping, Sequence, Set
from ansible.module_utils.common.collections import ImmutableDict
from ansible.module_utils.six import binary_type, text_type
from ansible.utils.context_objects import _make_immutable

def test_make_immutable_with_mapping():
    data = {'key1': 'value1', 'key2': 2, 'key3': [1, 2, 3]}
    result = _make_immutable(data)
    assert isinstance(result, ImmutableDict)
    assert result['key1'] == 'value1'
    assert result['key2'] == 2
    assert result['key3'] == (1, 2, 3)

def test_make_immutable_with_set():
    data = {'value1', 'value2', 3}
    result = _make_immutable(data)
    assert isinstance(result, frozenset)
    assert 'value1' in result
    assert 'value2' in result
    assert 3 in result

def test_make_immutable_with_sequence():
    data = ['value1', 'value2', 3]
    result = _make_immutable(data)
    assert isinstance(result, tuple)
    assert result == ('value1', 'value2', 3)
