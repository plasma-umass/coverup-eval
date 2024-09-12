# file: lib/ansible/vars/hostvars.py:79-90
# asked: {"lines": [90], "branches": [[86, 89], [89, 90]]}
# gained: {"lines": [], "branches": [[86, 89]]}

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

def test_setstate_assigns_loader_and_hostvars(hostvars, mock_variable_manager, mock_loader):
    state = {'_loader': mock_loader, '_variable_manager': mock_variable_manager}
    hostvars.__setstate__(state)
    
    assert mock_variable_manager._loader == mock_loader
    assert mock_variable_manager._hostvars == hostvars

def test_setstate_does_not_override_existing_loader_and_hostvars(hostvars, mock_variable_manager, mock_loader):
    existing_loader = Mock()
    existing_hostvars = Mock()
    mock_variable_manager._loader = existing_loader
    mock_variable_manager._hostvars = existing_hostvars
    
    state = {'_loader': mock_loader, '_variable_manager': mock_variable_manager}
    hostvars.__setstate__(state)
    
    assert mock_variable_manager._loader == existing_loader
    assert mock_variable_manager._hostvars == existing_hostvars
