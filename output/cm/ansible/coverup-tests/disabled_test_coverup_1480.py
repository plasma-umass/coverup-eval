# file lib/ansible/vars/hostvars.py:64-66
# lines [66]
# branches []

import pytest
from ansible.vars.hostvars import HostVars
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def inventory():
    # Create a DataLoader instance
    loader = DataLoader()
    # Create an InventoryManager instance with the created DataLoader
    inventory = InventoryManager(loader=loader)
    return inventory

@pytest.fixture
def variable_manager(inventory):
    # Create a VariableManager instance
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    return variable_manager

@pytest.fixture
def hostvars(inventory, variable_manager):
    # Create a HostVars instance with the created InventoryManager and VariableManager
    return HostVars(inventory=inventory, variable_manager=variable_manager, loader=DataLoader())

def test_find_host_existing_host(inventory, hostvars, mocker):
    # Add a host to the inventory
    inventory.add_host('testhost')
    # Ensure that the _find_host method returns the correct host
    host = hostvars._find_host('testhost')
    assert host is not None
    assert host.name == 'testhost'

def test_find_host_non_existing_host(hostvars, mocker):
    # Mock the get_host method to return None for a non-existing host
    mocker.patch.object(hostvars._inventory, 'get_host', return_value=None)
    # Ensure that the _find_host method returns None for a non-existing host
    host = hostvars._find_host('nonexistinghost')
    assert host is None
