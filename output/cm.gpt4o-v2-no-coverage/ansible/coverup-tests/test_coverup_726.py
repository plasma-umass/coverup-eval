# file: lib/ansible/vars/hostvars.py:51-55
# asked: {"lines": [51, 52, 53, 54, 55], "branches": []}
# gained: {"lines": [51, 52, 53, 54, 55], "branches": []}

import pytest
from unittest.mock import Mock, PropertyMock
from ansible.vars.hostvars import HostVars

@pytest.fixture
def mock_inventory():
    inventory = Mock()
    type(inventory).hosts = PropertyMock(return_value=[])
    return inventory

@pytest.fixture
def mock_variable_manager():
    return Mock()

@pytest.fixture
def mock_loader():
    return Mock()

def test_hostvars_init(mock_inventory, mock_variable_manager, mock_loader):
    hostvars = HostVars(mock_inventory, mock_variable_manager, mock_loader)
    
    assert hostvars._inventory == mock_inventory
    assert hostvars._loader == mock_loader
    assert hostvars._variable_manager == mock_variable_manager
    assert mock_variable_manager._hostvars == hostvars
