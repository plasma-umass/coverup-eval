# file lib/ansible/vars/hostvars.py:64-66
# lines [66]
# branches []

import pytest
from ansible.vars.hostvars import HostVars
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def inventory_manager():
    loader = DataLoader()
    return InventoryManager(loader=loader)

@pytest.fixture
def variable_manager(inventory_manager):
    return VariableManager(loader=DataLoader(), inventory=inventory_manager)

@pytest.fixture
def hostvars(inventory_manager, variable_manager):
    loader = DataLoader()
    return HostVars(inventory_manager, variable_manager, loader)

def test_find_host_method_executes_line_66(mocker, hostvars):
    # Mock the _inventory.get_host method to ensure it is called
    mocker.patch.object(hostvars._inventory, 'get_host', return_value='mocked_host')

    # Call the _find_host method which should execute line 66
    result = hostvars._find_host('localhost')

    # Assert that the mocked get_host method was called with 'localhost'
    hostvars._inventory.get_host.assert_called_once_with('localhost')

    # Assert that the result of _find_host is the mocked return value
    assert result == 'mocked_host'
