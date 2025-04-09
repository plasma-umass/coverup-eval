# file: lib/ansible/inventory/host.py:144-148
# asked: {"lines": [146], "branches": [[145, 146]]}
# gained: {"lines": [146], "branches": [[145, 146]]}

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.common._collections_compat import Mapping, MutableMapping
from ansible.utils.vars import combine_vars
from ansible.inventory.host import Host

@pytest.fixture
def host():
    return Host()

def test_set_variable_with_mutable_mapping(monkeypatch, host):
    mock_combine_vars = MagicMock(return_value={'key': {'nested_key': 'nested_value'}})
    monkeypatch.setattr('ansible.inventory.host.combine_vars', mock_combine_vars)
    
    host.vars = {'key': {'existing_key': 'existing_value'}}
    host.set_variable('key', {'nested_key': 'nested_value'})
    
    assert host.vars == {'key': {'nested_key': 'nested_value'}}
    mock_combine_vars.assert_called_once_with({'key': {'existing_key': 'existing_value'}}, {'key': {'nested_key': 'nested_value'}})

def test_set_variable_without_mutable_mapping(host):
    host.vars = {'key': 'existing_value'}
    host.set_variable('key', 'new_value')
    
    assert host.vars == {'key': 'new_value'}

def test_set_variable_new_key(host):
    host.vars = {}
    host.set_variable('new_key', 'new_value')
    
    assert host.vars == {'new_key': 'new_value'}
