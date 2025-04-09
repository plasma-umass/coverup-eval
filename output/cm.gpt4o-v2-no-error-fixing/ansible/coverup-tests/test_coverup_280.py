# file: lib/ansible/plugins/inventory/ini.py:249-254
# asked: {"lines": [249, 250, 251, 252, 253, 254], "branches": [[250, 251], [250, 254], [252, 250], [252, 253]]}
# gained: {"lines": [249, 250, 251, 252, 253, 254], "branches": [[250, 251], [250, 254], [252, 253]]}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.inventory.ini import InventoryModule

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_add_pending_children(inventory_module):
    # Mock the inventory and its add_child method
    inventory_module.inventory = MagicMock()
    inventory_module.inventory.add_child = MagicMock()

    # Define the pending dictionary
    pending = {
        'group1': {
            'parents': ['parent1', 'parent2'],
            'state': 'children'
        },
        'parent1': {
            'parents': [],
            'state': 'children'
        },
        'parent2': {
            'parents': [],
            'state': 'children'
        }
    }

    # Call the method
    inventory_module._add_pending_children('group1', pending)

    # Assertions to verify the expected behavior
    inventory_module.inventory.add_child.assert_any_call('parent1', 'group1')
    inventory_module.inventory.add_child.assert_any_call('parent2', 'group1')
    assert 'group1' not in pending
