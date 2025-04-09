# file: lib/ansible/vars/hostvars.py:57-59
# asked: {"lines": [57, 58, 59], "branches": []}
# gained: {"lines": [57, 58, 59], "branches": []}

import pytest
from unittest.mock import Mock, MagicMock
from ansible.vars.hostvars import HostVars

@pytest.fixture
def mock_variable_manager():
    return Mock()

@pytest.fixture
def mock_inventory():
    inventory = Mock()
    inventory.hosts = []
    return inventory

@pytest.fixture
def hostvars(mock_inventory, mock_variable_manager):
    loader = Mock()
    return HostVars(mock_inventory, mock_variable_manager, loader)

def test_set_variable_manager(hostvars, mock_variable_manager):
    new_variable_manager = Mock()
    hostvars.set_variable_manager(new_variable_manager)
    
    assert hostvars._variable_manager == new_variable_manager
    assert new_variable_manager._hostvars == hostvars

    # Clean up
    del hostvars._variable_manager
    del new_variable_manager._hostvars
