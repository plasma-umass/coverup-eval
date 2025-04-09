# file lib/ansible/vars/hostvars.py:107-109
# lines [107, 109]
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
    # Create a HostVars instance with the provided inventory and variable_manager
    return HostVars(inventory=inventory, variable_manager=variable_manager, loader=DataLoader())

def test_hostvars_contains_existing_host(mocker, hostvars):
    # Mock the _find_host method to return a host object when called with 'existing_host'
    mocker.patch.object(hostvars, '_find_host', return_value='mocked_host')
    assert 'existing_host' in hostvars, "The host should be found in hostvars"

def test_hostvars_contains_non_existing_host(mocker, hostvars):
    # Mock the _find_host method to return None when called with 'non_existing_host'
    mocker.patch.object(hostvars, '_find_host', return_value=None)
    assert 'non_existing_host' not in hostvars, "The host should not be found in hostvars"
