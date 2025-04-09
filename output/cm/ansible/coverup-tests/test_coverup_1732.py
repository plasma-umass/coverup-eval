# file lib/ansible/inventory/manager.py:181-182
# lines [182]
# branches []

import pytest
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def inventory_manager(mocker):
    # Mock the _inventory attribute directly to avoid side effects
    inventory = mocker.MagicMock()
    manager = InventoryManager(loader=None, sources='localhost,')
    manager._inventory = inventory
    return manager

def test_add_host_executes_line_182(inventory_manager):
    # Arrange
    host = 'testhost'
    group = 'testgroup'
    port = 2222

    # Act
    inventory_manager.add_host(host, group, port)

    # Assert
    # Verify that the add_host method of the _inventory attribute was called with the correct arguments
    assert inventory_manager._inventory.add_host.called
    inventory_manager._inventory.add_host.assert_called_with(host, group, port)
