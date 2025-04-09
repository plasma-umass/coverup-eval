# file lib/ansible/vars/hostvars.py:118-122
# lines [119, 120, 121, 122]
# branches ['120->121', '120->122']

import pytest
from ansible.vars.hostvars import HostVars
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager

@pytest.fixture
def inventory():
    # Setup inventory with DataLoader and InventoryManager
    loader = DataLoader()
    inventory = InventoryManager(loader=loader)
    # Add a host to the inventory to ensure the loop in __repr__ is executed
    inventory.add_host('testhost')
    return inventory

@pytest.fixture
def variable_manager(inventory):
    # Setup VariableManager
    loader = DataLoader()
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    return variable_manager

def test_hostvars_repr(mocker, inventory, variable_manager):
    # Mock the HostVars.get method to avoid side effects
    mocker.patch.object(HostVars, 'get', return_value='hostvars_value')
    
    # Create HostVars instance with the provided inventory and variable_manager fixtures
    loader = DataLoader()
    hostvars = HostVars(inventory, variable_manager, loader)
    
    # Call __repr__ and assert the output
    repr_output = repr(hostvars)
    expected_output = "{'testhost': 'hostvars_value'}"
    assert repr_output == expected_output
    
    # Cleanup is handled by pytest fixtures automatically
