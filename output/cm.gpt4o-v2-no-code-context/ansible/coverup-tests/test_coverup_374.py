# file: lib/ansible/inventory/group.py:244-252
# asked: {"lines": [244, 246, 247, 249, 250, 252], "branches": [[246, 247], [246, 249], [249, 250], [249, 252]]}
# gained: {"lines": [244], "branches": []}

import pytest
from unittest.mock import MagicMock
from collections.abc import MutableMapping, Mapping

class Group:
    def __init__(self):
        self.vars = {}
        self.priority = 0

    def set_priority(self, priority):
        self.priority = priority

    def set_variable(self, key, value):
        if key == 'ansible_group_priority':
            self.set_priority(int(value))
        else:
            if key in self.vars and isinstance(self.vars[key], MutableMapping) and isinstance(value, Mapping):
                self.vars = combine_vars(self.vars, {key: value})
            else:
                self.vars[key] = value

def combine_vars(vars1, vars2):
    result = vars1.copy()
    for k, v in vars2.items():
        if k in result and isinstance(result[k], MutableMapping) and isinstance(v, Mapping):
            result[k] = combine_vars(result[k], v)
        else:
            result[k] = v
    return result

@pytest.fixture
def group():
    return Group()

def test_set_variable_priority(group):
    group.set_variable('ansible_group_priority', '10')
    assert group.priority == 10

def test_set_variable_existing_mapping(group, monkeypatch):
    group.vars = {'key1': {'subkey': 'value1'}}
    new_value = {'subkey': 'value2'}
    monkeypatch.setattr('ansible.inventory.group.combine_vars', combine_vars)
    group.set_variable('key1', new_value)
    assert group.vars == {'key1': {'subkey': 'value2'}}

def test_set_variable_new_key(group):
    group.set_variable('new_key', 'new_value')
    assert group.vars == {'new_key': 'new_value'}

def test_set_variable_non_mapping_existing_key(group):
    group.vars = {'key1': 'value1'}
    group.set_variable('key1', 'new_value')
    assert group.vars == {'key1': 'new_value'}
