# file lib/ansible/plugins/inventory/constructed.py:115-117
# lines [115, 117]
# branches []

import pytest
from ansible.plugins.inventory.constructed import InventoryModule
from ansible.inventory.host import Host
from ansible.inventory.group import Group
from ansible.inventory.data import InventoryData
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager

# Mock classes to avoid side effects
class MockLoader(DataLoader):
    def __init__(self):
        pass

class MockSources:
    pass

# Test function
def test_get_all_host_vars(mocker):
    # Setup mocks
    mocker.patch.object(InventoryModule, 'host_groupvars', return_value={'group_var': 'value1'})
    mocker.patch.object(InventoryModule, 'host_vars', return_value={'host_var': 'value2'})

    # Create instances
    inventory_module = InventoryModule()
    host = Host(name='testhost')
    loader = MockLoader()
    sources = MockSources()

    # Call the method
    all_vars = inventory_module.get_all_host_vars(host, loader, sources)

    # Assertions to verify postconditions
    assert all_vars == {'group_var': 'value1', 'host_var': 'value2'}, "The returned vars should be a combination of group and host vars"

    # Cleanup is handled by the mocker fixture, which undoes all patches after the test
