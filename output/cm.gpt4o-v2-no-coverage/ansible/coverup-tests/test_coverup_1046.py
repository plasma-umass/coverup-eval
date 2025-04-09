# file: lib/ansible/vars/hostvars.py:98-99
# asked: {"lines": [98, 99], "branches": []}
# gained: {"lines": [98, 99], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.hostvars import HostVars
from ansible.vars.hostvars import HostVarsVars
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

def test_set_host_variable(hostvars, mock_variable_manager):
    hostvars.set_host_variable('host1', 'varname', 'value1')
    mock_variable_manager.set_host_variable.assert_called_once_with('host1', 'varname', 'value1')

def test_len(hostvars):
    assert len(hostvars) == 2

def test_iter(hostvars):
    hosts = list(iter(hostvars))
    assert hosts == ['host1', 'host2']

def test_getitem_existing_host(hostvars, mock_loader):
    hostvars.raw_get = MagicMock(return_value={'var': 'value'})
    result = hostvars['host1']
    assert isinstance(result, HostVarsVars)
    assert result._loader == mock_loader

def test_getitem_undefined_host(hostvars):
    hostvars.raw_get = MagicMock(return_value=AnsibleUndefined())
    result = hostvars['undefined_host']
    assert isinstance(result, AnsibleUndefined)
