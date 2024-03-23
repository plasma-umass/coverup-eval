# file lib/ansible/vars/hostvars.py:64-66
# lines [64, 66]
# branches []

import pytest
from ansible.vars.hostvars import HostVars
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager

@pytest.fixture
def inventory():
    # Create a DataLoader instance
    loader = DataLoader()
    # Create an Inventory instance with the DataLoader instance
    inventory = InventoryManager(loader=loader)
    return inventory

@pytest.fixture
def variable_manager(inventory):
    # Create a VariableManager instance
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    return variable_manager

@pytest.fixture
def hostvars(inventory, variable_manager):
    # Create a HostVars instance with the Inventory and VariableManager instances
    return HostVars(inventory=inventory, variable_manager=variable_manager, loader=DataLoader())

def test_find_host_existing_host(inventory, hostvars):
    # Add a host to the inventory
    inventory.add_host('testhost')
    # Find the host using the HostVars instance
    host = hostvars._find_host('testhost')
    # Assert that the host is found and is correct
    assert host is not None
    assert host.name == 'testhost'

def test_find_host_non_existing_host(hostvars):
    # Try to find a non-existing host using the HostVars instance
    host = hostvars._find_host('nonexistinghost')
    # Assert that the host is not found
    assert host is None

# Clean up after the test
def teardown_module(module):
    # Remove any added hosts
    inventory = getattr(module, 'inventory', None)
    if inventory and hasattr(inventory, 'clear_hosts'):
        inventory.clear_hosts()
