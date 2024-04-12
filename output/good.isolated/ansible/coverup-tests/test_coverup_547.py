# file lib/ansible/cli/playbook.py:213-217
# lines [213, 214, 215, 216, 217]
# branches ['215->exit', '215->216']

import pytest
from ansible.cli.playbook import PlaybookCLI
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager

# Mock classes to simulate the behavior of actual Inventory and VariableManager
class MockHost:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class MockInventory:
    def __init__(self, hosts):
        self.hosts = hosts

    def list_hosts(self):
        return self.hosts

@pytest.fixture
def mock_inventory(mocker):
    # Create a mock inventory with a list of mock hosts
    hosts = [MockHost('host1'), MockHost('host2')]
    inventory = MockInventory(hosts)
    return inventory

@pytest.fixture
def mock_variable_manager(mocker):
    # Create a mock VariableManager with a clear_facts method
    variable_manager = mocker.MagicMock(spec=VariableManager)
    return variable_manager

def test_flush_cache(mock_inventory, mock_variable_manager):
    # Call the static method _flush_cache with the mock objects
    PlaybookCLI._flush_cache(mock_inventory, mock_variable_manager)

    # Assert that clear_facts was called for each host in the inventory
    for host in mock_inventory.list_hosts():
        hostname = host.get_name()
        mock_variable_manager.clear_facts.assert_any_call(hostname)

    # Assert that clear_facts was called the correct number of times
    assert mock_variable_manager.clear_facts.call_count == len(mock_inventory.list_hosts())
