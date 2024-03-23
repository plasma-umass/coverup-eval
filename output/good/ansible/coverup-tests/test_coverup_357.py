# file lib/ansible/inventory/data.py:180-189
# lines [180, 182, 183, 184, 185, 187, 188, 189]
# branches ['182->183', '182->187', '187->exit', '187->188']

import pytest
from ansible.inventory.data import InventoryData
from ansible.utils.display import Display
from unittest.mock import MagicMock

# Mock the display object to prevent actual output during tests
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'debug')

@pytest.fixture
def inventory_data(mocker):
    # Setup inventory data with a group and a host
    inventory = InventoryData()
    inventory.groups = {'test_group': None}
    inventory.hosts = {'test_host': mocker.Mock()}
    return inventory

def test_remove_group(mock_display, inventory_data):
    # Precondition: Ensure 'test_group' is in the inventory
    assert 'test_group' in inventory_data.groups

    # Precondition: Ensure 'test_host' is in the inventory
    assert 'test_host' in inventory_data.hosts

    # Precondition: Ensure 'test_host' has a remove_group method
    assert hasattr(inventory_data.hosts['test_host'], 'remove_group')

    # Call remove_group
    inventory_data.remove_group('test_group')

    # Postcondition: 'test_group' should be removed from inventory groups
    assert 'test_group' not in inventory_data.groups

    # Postcondition: 'test_host's remove_group should have been called with 'test_group'
    inventory_data.hosts['test_host'].remove_group.assert_called_once_with('test_group')

    # Cleanup: No cleanup necessary as inventory_data is a fixture with function scope
