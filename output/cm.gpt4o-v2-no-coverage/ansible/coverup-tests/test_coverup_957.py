# file: lib/ansible/vars/hostvars.py:61-62
# asked: {"lines": [61, 62], "branches": []}
# gained: {"lines": [61, 62], "branches": []}

import pytest
from ansible.vars.hostvars import HostVars
from unittest.mock import MagicMock

@pytest.fixture
def mock_variable_manager():
    return MagicMock()

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def hostvars(mock_variable_manager, mock_loader):
    inventory = MagicMock()
    return HostVars(inventory, mock_variable_manager, mock_loader)

def test_set_inventory(hostvars):
    new_inventory = MagicMock()
    hostvars.set_inventory(new_inventory)
    assert hostvars._inventory == new_inventory

def test_initialization(mock_variable_manager, mock_loader):
    inventory = MagicMock()
    hostvars = HostVars(inventory, mock_variable_manager, mock_loader)
    assert hostvars._inventory == inventory
    assert hostvars._loader == mock_loader
    assert hostvars._variable_manager == mock_variable_manager
    assert mock_variable_manager._hostvars == hostvars
