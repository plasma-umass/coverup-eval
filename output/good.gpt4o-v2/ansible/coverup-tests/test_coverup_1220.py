# file: lib/ansible/utils/context_objects.py:20-50
# asked: {"lines": [31, 39, 47], "branches": [[28, 31], [36, 39], [44, 47]]}
# gained: {"lines": [31, 39, 47], "branches": [[28, 31], [36, 39], [44, 47]]}

import pytest
from ansible.module_utils.common._collections_compat import Container, Mapping, Sequence, Set
from ansible.module_utils.common.collections import ImmutableDict
from ansible.module_utils.six import binary_type, text_type
from ansible.utils.context_objects import _make_immutable

def test_make_immutable_with_mapping():
    data = {'key1': 'value1', 'key2': {'subkey': 'subvalue'}}
    result = _make_immutable(data)
    assert isinstance(result, ImmutableDict)
    assert result['key1'] == 'value1'
    assert isinstance(result['key2'], ImmutableDict)
    assert result['key2']['subkey'] == 'subvalue'

def test_make_immutable_with_set():
    data = {'value1', 'value2', ('subvalue1', 'subvalue2')}
    result = _make_immutable(data)
    assert isinstance(result, frozenset)
    assert ('subvalue1', 'subvalue2') in result

def test_make_immutable_with_sequence():
    data = ['value1', ['subvalue1', 'subvalue2'], 'value2']
    result = _make_immutable(data)
    assert isinstance(result, tuple)
    assert isinstance(result[1], tuple)
    assert result[1] == ('subvalue1', 'subvalue2')

def test_make_immutable_with_non_container_mapping():
    data = {'key1': 'value1', 'key2': 123}
    result = _make_immutable(data)
    assert isinstance(result, ImmutableDict)
    assert result['key1'] == 'value1'
    assert result['key2'] == 123

def test_make_immutable_with_non_container_set():
    data = {'value1', 'value2', 123}
    result = _make_immutable(data)
    assert isinstance(result, frozenset)
    assert 123 in result

def test_make_immutable_with_non_container_sequence():
    data = ['value1', 123, 'value2']
    result = _make_immutable(data)
    assert isinstance(result, tuple)
    assert result[1] == 123
