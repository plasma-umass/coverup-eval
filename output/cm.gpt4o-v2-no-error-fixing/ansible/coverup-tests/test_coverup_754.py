# file: lib/ansible/utils/context_objects.py:20-50
# asked: {"lines": [31, 34, 35, 36, 37, 39, 40, 45, 50], "branches": [[28, 31], [33, 34], [35, 36], [35, 40], [36, 37], [36, 39], [41, 50], [44, 45]]}
# gained: {"lines": [34, 35, 36, 37, 40, 45, 50], "branches": [[33, 34], [35, 36], [35, 40], [36, 37], [41, 50], [44, 45]]}

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
    assert 'value1' in result
    assert 'value2' in result
    assert any(isinstance(item, tuple) and item == ('subvalue1', 'subvalue2') for item in result)

def test_make_immutable_with_sequence():
    data = ['value1', 'value2', ['subvalue1', 'subvalue2']]
    result = _make_immutable(data)
    assert isinstance(result, tuple)
    assert result[0] == 'value1'
    assert result[1] == 'value2'
    assert isinstance(result[2], tuple)
    assert result[2][0] == 'subvalue1'
    assert result[2][1] == 'subvalue2'

def test_make_immutable_with_other():
    data = 42
    result = _make_immutable(data)
    assert result == 42
