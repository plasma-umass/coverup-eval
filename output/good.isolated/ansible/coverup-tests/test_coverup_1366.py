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
    return inventory

@pytest.fixture
def variable_manager(inventory):
    # Setup VariableManager for the test
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    return variable_manager

def test_hostvars_iteration(inventory, variable_manager):
    # Mock the inventory to have some hosts
    inventory.add_host('host1')
    inventory.add_host('host2')

    # Create HostVars instance with the mocked inventory and variable manager
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=DataLoader())

    # Iterate over the hostvars to trigger __iter__
    hosts = [host for host in hostvars]

    # Assert that the hosts are correctly retrieved
    assert 'host1' in hosts
    assert 'host2' in hosts

    # Cleanup: No cleanup required as inventory and variable_manager are fixtures and will be discarded after the test
