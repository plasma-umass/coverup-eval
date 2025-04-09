# file: lib/ansible/vars/hostvars.py:79-90
# asked: {"lines": [79, 80, 86, 87, 89, 90], "branches": [[86, 87], [86, 89], [89, 0], [89, 90]]}
# gained: {"lines": [79, 80, 86, 87, 89], "branches": [[86, 87], [89, 0]]}

import pytest
from unittest.mock import Mock, MagicMock
from ansible.vars.hostvars import HostVars

@pytest.fixture
def mock_variable_manager():
    return Mock(_loader=None, _hostvars=None)

@pytest.fixture
def mock_loader():
    return Mock()

@pytest.fixture
def mock_inventory():
    inventory = Mock()
    inventory.hosts = []
    return inventory

@pytest.fixture
def hostvars(mock_variable_manager, mock_loader, mock_inventory):
    return HostVars(inventory=mock_inventory, variable_manager=mock_variable_manager, loader=mock_loader)

def test_setstate_updates_state(hostvars, mock_variable_manager, mock_loader):
    state = {'some_key': 'some_value', '_loader': mock_loader, '_variable_manager': mock_variable_manager}
    hostvars.__setstate__(state)
    
    assert hostvars.some_key == 'some_value'
    assert hostvars._loader == mock_loader
    assert hostvars._variable_manager == mock_variable_manager

def test_setstate_assigns_loader_if_none(hostvars, mock_variable_manager, mock_loader):
    state = {'_loader': mock_loader, '_variable_manager': mock_variable_manager}
    hostvars.__setstate__(state)
    
    assert mock_variable_manager._loader == mock_loader

def test_setstate_assigns_hostvars_if_none(hostvars, mock_variable_manager):
    state = {'_variable_manager': mock_variable_manager}
    hostvars.__setstate__(state)
    
    assert mock_variable_manager._hostvars == hostvars
