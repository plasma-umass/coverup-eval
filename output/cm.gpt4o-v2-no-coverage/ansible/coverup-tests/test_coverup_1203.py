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
def hostvars(mock_inventory, mock_variable_manager, mock_loader):
    return HostVars(inventory=mock_inventory, variable_manager=mock_variable_manager, loader=mock_loader)

def test_setstate_updates_state(hostvars, mock_variable_manager, mock_loader):
    state = {'some_key': 'some_value'}
    hostvars.__setstate__(state)
    
    assert hostvars.some_key == 'some_value'
    assert mock_variable_manager._loader == mock_loader
    assert mock_variable_manager._hostvars == hostvars

def test_setstate_preserves_existing_loader_and_hostvars(hostvars, mock_variable_manager, mock_loader):
    mock_variable_manager._loader = 'existing_loader'
    mock_variable_manager._hostvars = 'existing_hostvars'
    
    state = {'another_key': 'another_value'}
    hostvars.__setstate__(state)
    
    assert hostvars.another_key == 'another_value'
    assert mock_variable_manager._loader == 'existing_loader'
    assert mock_variable_manager._hostvars == 'existing_hostvars'
