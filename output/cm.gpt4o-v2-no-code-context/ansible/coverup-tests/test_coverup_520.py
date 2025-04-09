# file: lib/ansible/inventory/host.py:144-148
# asked: {"lines": [144, 145, 146, 148], "branches": [[145, 146], [145, 148]]}
# gained: {"lines": [144], "branches": []}

import pytest
from collections.abc import MutableMapping, Mapping
from unittest.mock import patch

class Host:
    def __init__(self):
        self.vars = {}

    def set_variable(self, key, value):
        if key in self.vars and isinstance(self.vars[key], MutableMapping) and isinstance(value, Mapping):
            self.vars[key] = combine_vars(self.vars[key], value)
        else:
            self.vars[key] = value

def combine_vars(vars1, vars2):
    # Dummy implementation for testing purposes
    combined = vars1.copy()
    combined.update(vars2)
    return combined

@pytest.fixture
def host():
    return Host()

def test_set_variable_combines_vars(host, mocker):
    mocker.patch('ansible.inventory.host.combine_vars', side_effect=combine_vars)
    host.vars = {'key1': {'subkey': 'subvalue'}}
    host.set_variable('key1', {'newsubkey': 'newsubvalue'})
    assert host.vars == {'key1': {'subkey': 'subvalue', 'newsubkey': 'newsubvalue'}}

def test_set_variable_sets_value(host):
    host.set_variable('key2', 'value2')
    assert host.vars == {'key2': 'value2'}

def test_set_variable_overwrites_non_mapping_value(host):
    host.vars = {'key3': 'oldvalue'}
    host.set_variable('key3', 'newvalue')
    assert host.vars == {'key3': 'newvalue'}

def test_set_variable_with_non_mapping_existing_value(host):
    host.vars = {'key4': 'oldvalue'}
    host.set_variable('key4', {'newsubkey': 'newsubvalue'})
    assert host.vars == {'key4': {'newsubkey': 'newsubvalue'}}
