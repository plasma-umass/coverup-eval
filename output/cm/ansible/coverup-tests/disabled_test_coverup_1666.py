# file lib/ansible/vars/hostvars.py:111-113
# lines [112, 113]
# branches ['112->exit', '112->113']

import pytest
from ansible.vars.hostvars import HostVars
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def inventory():
    # Setup DataLoader and InventoryManager for the test
    loader = DataLoader()
    inventory = InventoryManager(loader=loader)
    # Add a host to the inventory to ensure __iter__ is called
    inventory.add_host('testhost')
    return inventory, loader

def test_hostvars_iter(inventory):
    # Unpack the inventory and loader from the fixture
    inventory_manager, loader = inventory
    # Setup VariableManager for the test
    variable_manager = VariableManager(loader=loader, inventory=inventory_manager)
    
    # Create the HostVars object with the test inventory and variable manager
    hostvars = HostVars(inventory=inventory_manager, variable_manager=variable_manager, loader=loader)
    
    # Use the __iter__ method and collect the results
    hosts = list(iter(hostvars))
    
    # Assert that the host added to the inventory is in the result
    assert 'testhost' in hosts
    
    # Assert that the length of hosts is 1, as we only added one host
    assert len(hosts) == 1

    # Cleanup is handled by the fixture, no other state is modified
