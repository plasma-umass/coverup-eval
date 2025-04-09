# file: lib/ansible/vars/hostvars.py:104-105
# asked: {"lines": [104, 105], "branches": []}
# gained: {"lines": [104, 105], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.vars.hostvars import HostVars, HostVarsVars
from ansible.template import AnsibleUndefined

@pytest.fixture
def mock_inventory():
    inventory = MagicMock()
    inventory.hosts = ['host1', 'host2']
    return inventory

@pytest.fixture
def mock_variable_manager():
    return MagicMock()

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def hostvars(mock_inventory, mock_variable_manager, mock_loader):
    return HostVars(mock_inventory, mock_variable_manager, mock_loader)

def test_set_host_facts(hostvars, mock_variable_manager):
    host = 'host1'
    facts = {'fact1': 'value1'}
    hostvars.set_host_facts(host, facts)
    mock_variable_manager.set_host_facts.assert_called_once_with(host, facts)

def test_iter(hostvars):
    hosts = list(iter(hostvars))
    assert hosts == ['host1', 'host2']

def test_len(hostvars):
    assert len(hostvars) == 2

@patch('ansible.vars.hostvars.HostVars.raw_get')
def test_getitem(mock_raw_get, hostvars, mock_loader):
    host_name = 'host1'
    data = {'var1': 'value1'}
    mock_raw_get.return_value = data
    result = hostvars[host_name]
    assert isinstance(result, HostVarsVars)
    assert result._vars == data
    assert result._loader == mock_loader

@patch('ansible.vars.hostvars.HostVars.raw_get')
def test_getitem_undefined(mock_raw_get, hostvars):
    host_name = 'host1'
    data = AnsibleUndefined()
    mock_raw_get.return_value = data
    result = hostvars[host_name]
    assert result is data
