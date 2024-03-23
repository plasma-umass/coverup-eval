# file lib/ansible/vars/hostvars.py:61-62
# lines [61, 62]
# branches []

import pytest
from ansible.vars.hostvars import HostVars
from unittest.mock import MagicMock

# Assuming the existence of a minimal Inventory class for testing purposes
class MockInventory:
    def __init__(self):
        pass

@pytest.fixture
def host_vars():
    # Mocking the required arguments for HostVars initialization
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    # Create a HostVars instance with mocked dependencies
    hv = HostVars(inventory, variable_manager, loader)
    # Ensure _inventory attribute is not set before the test
    if hasattr(hv, '_inventory'):
        del hv._inventory
    return hv

@pytest.fixture
def mock_inventory():
    return MockInventory()

def test_set_inventory(host_vars, mock_inventory):
    # Precondition: _inventory attribute should not be set
    assert not hasattr(host_vars, '_inventory')
    
    # Action: Set the inventory
    host_vars.set_inventory(mock_inventory)
    
    # Postcondition: _inventory attribute should be set to mock_inventory
    assert hasattr(host_vars, '_inventory')
    assert host_vars._inventory is mock_inventory
