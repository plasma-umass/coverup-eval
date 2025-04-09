# file: lib/ansible/module_utils/common/dict_transformations.py:112-124
# asked: {"lines": [112, 116, 117, 118, 119, 120, 121, 123, 124], "branches": [[116, 117], [116, 118], [119, 120], [119, 124], [120, 121], [120, 123]]}
# gained: {"lines": [112, 116, 117, 118, 119, 120, 121, 123, 124], "branches": [[116, 117], [116, 118], [119, 120], [119, 124], [120, 121], [120, 123]]}

import pytest
from copy import deepcopy
from ansible.module_utils.common.dict_transformations import dict_merge

def test_dict_merge_simple():
    a = {'key1': 'value1'}
    b = {'key2': 'value2'}
    result = dict_merge(a, b)
    assert result == {'key1': 'value1', 'key2': 'value2'}

def test_dict_merge_nested():
    a = {'key1': {'subkey1': 'subvalue1'}}
    b = {'key1': {'subkey2': 'subvalue2'}}
    result = dict_merge(a, b)
    assert result == {'key1': {'subkey1': 'subvalue1', 'subkey2': 'subvalue2'}}

def test_dict_merge_overwrite():
    a = {'key1': 'value1'}
    b = {'key1': 'value2'}
    result = dict_merge(a, b)
    assert result == {'key1': 'value2'}

def test_dict_merge_non_dict_b():
    a = {'key1': 'value1'}
    b = 'not a dict'
    result = dict_merge(a, b)
    assert result == 'not a dict'

def test_dict_merge_deepcopy():
    a = {'key1': {'subkey1': 'subvalue1'}}
    b = {'key1': {'subkey2': 'subvalue2'}}
    result = dict_merge(a, b)
    b['key1']['subkey2'] = 'changed'
    assert result == {'key1': {'subkey1': 'subvalue1', 'subkey2': 'subvalue2'}}

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    # Ensure no state pollution between tests
    yield
    monkeypatch.undo()
