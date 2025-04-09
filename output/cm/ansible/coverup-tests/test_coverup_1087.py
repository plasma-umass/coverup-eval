# file lib/ansible/vars/hostvars.py:115-116
# lines [115, 116]
# branches []

import pytest
from ansible.vars.hostvars import HostVars
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader
from unittest.mock import MagicMock

@pytest.fixture
def inventory():
    # Create a DataLoader instance
    loader = DataLoader()
    # Create an InventoryManager instance with an empty source
    inventory = InventoryManager(loader=loader, sources='localhost,')
    return inventory

@pytest.fixture
def variable_manager(inventory):
    # Create a VariableManager instance
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    return variable_manager

@pytest.fixture
def hostvars(inventory, variable_manager):
    # Create a HostVars instance with the provided inventory and variable_manager
    hv = HostVars(inventory=inventory, variable_manager=variable_manager, loader=DataLoader())
    return hv

def test_hostvars_len(mocker, inventory, variable_manager):
    # Create a HostVars instance with the provided inventory and variable_manager
    hv = HostVars(inventory=inventory, variable_manager=variable_manager, loader=DataLoader())
    
    # Mock the __len__ method of the inventory.hosts to control the return value
    mocker.patch('ansible.inventory.manager.InventoryManager.hosts', new_callable=MagicMock(return_value={'host1': {}, 'host2': {}}))
    
    # Assert that the __len__ method of HostVars returns the mocked length
    assert len(hv) == 2
    # Cleanup is handled by the mocker fixture, no need for additional cleanup
