# file: lib/ansible/vars/hostvars.py:64-66
# asked: {"lines": [64, 66], "branches": []}
# gained: {"lines": [64, 66], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.hostvars import HostVars

@pytest.fixture
def hostvars():
    inventory_mock = MagicMock()
    variable_manager_mock = MagicMock()
    loader_mock = MagicMock()
    hostvars_instance = HostVars(inventory_mock, variable_manager_mock, loader_mock)
    return hostvars_instance, inventory_mock

def test_find_host_existing_host(hostvars):
    hostvars_instance, inventory_mock = hostvars
    inventory_mock.get_host.return_value = 'host1'
    
    result = hostvars_instance._find_host('host1')
    
    inventory_mock.get_host.assert_called_once_with('host1')
    assert result == 'host1'

def test_find_host_non_existing_host(hostvars):
    hostvars_instance, inventory_mock = hostvars
    inventory_mock.get_host.return_value = None
    
    result = hostvars_instance._find_host('non_existing_host')
    
    inventory_mock.get_host.assert_called_once_with('non_existing_host')
    assert result is None
