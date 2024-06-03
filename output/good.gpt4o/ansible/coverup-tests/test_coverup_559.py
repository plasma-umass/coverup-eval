# file lib/ansible/inventory/host.py:144-148
# lines [144, 145, 146, 148]
# branches ['145->146', '145->148']

import pytest
from unittest.mock import MagicMock
from collections.abc import MutableMapping, Mapping

class Host:
    def __init__(self):
        self.vars = {}

    def set_variable(self, key, value):
        if key in self.vars and isinstance(self.vars[key], MutableMapping) and isinstance(value, Mapping):
            self.vars = combine_vars(self.vars, {key: value})
        else:
            self.vars[key] = value

def combine_vars(vars1, vars2):
    combined = vars1.copy()
    for k, v in vars2.items():
        if k in combined and isinstance(combined[k], MutableMapping) and isinstance(v, Mapping):
            combined[k] = combine_vars(combined[k], v)
        else:
            combined[k] = v
    return combined

@pytest.fixture
def host():
    return Host()

def test_set_variable_combines_vars(host, mocker):
    mocker.patch('ansible.inventory.host.combine_vars', side_effect=combine_vars)
    host.vars = {'key1': {'subkey1': 'value1'}}
    host.set_variable('key1', {'subkey2': 'value2'})
    assert host.vars == {'key1': {'subkey1': 'value1', 'subkey2': 'value2'}}

def test_set_variable_overwrites_value(host):
    host.vars = {'key1': 'value1'}
    host.set_variable('key1', 'new_value')
    assert host.vars == {'key1': 'new_value'}

def test_set_variable_adds_new_key(host):
    host.set_variable('key2', 'value2')
    assert host.vars == {'key2': 'value2'}
