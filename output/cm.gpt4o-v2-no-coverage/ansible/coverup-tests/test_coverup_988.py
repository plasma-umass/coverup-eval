# file: lib/ansible/vars/hostvars.py:115-116
# asked: {"lines": [115, 116], "branches": []}
# gained: {"lines": [115, 116], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.hostvars import HostVars

@pytest.fixture
def mock_inventory():
    class MockInventory:
        def __init__(self, hosts):
            self.hosts = hosts
    return MockInventory

@pytest.fixture
def mock_variable_manager():
    class MockVariableManager:
        pass
    return MockVariableManager()

@pytest.fixture
def mock_loader():
    return MagicMock()

def test_hostvars_len(mock_inventory, mock_variable_manager, mock_loader):
    hosts = {'host1': {}, 'host2': {}}
    inventory = mock_inventory(hosts)
    variable_manager = mock_variable_manager
    loader = mock_loader

    hostvars = HostVars(inventory, variable_manager, loader)

    assert len(hostvars) == 2

    # Clean up
    del hostvars._inventory
