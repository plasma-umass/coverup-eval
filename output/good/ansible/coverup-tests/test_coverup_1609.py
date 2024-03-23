# file lib/ansible/plugins/inventory/ini.py:249-254
# lines [250, 251, 252, 253, 254]
# branches ['250->251', '250->254', '252->250', '252->253']

import pytest
from ansible.plugins.inventory.ini import InventoryModule
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def inventory_module(mocker):
    mocker.patch('ansible.inventory.manager.InventoryManager', autospec=True)
    mocker.patch('ansible.parsing.dataloader.DataLoader', autospec=True)
    return InventoryModule()

def test_add_pending_children(inventory_module, mocker):
    # Mock the necessary methods and attributes
    inventory_module.inventory = mocker.MagicMock()
    inventory_module.inventory.add_child = mocker.MagicMock()

    # Define a pending structure that will trigger the recursive call
    pending = {
        'child_group': {
            'parents': ['parent_group'],
            'state': 'children'
        },
        'parent_group': {
            'parents': ['grandparent_group'],
            'state': 'children'
        },
        'grandparent_group': {
            'parents': [],
            'state': 'children'
        }
    }

    # Call the method under test
    inventory_module._add_pending_children('child_group', pending)

    # Assert that add_child was called for both child-parent and parent-grandparent relationships
    inventory_module.inventory.add_child.assert_any_call('parent_group', 'child_group')
    inventory_module.inventory.add_child.assert_any_call('grandparent_group', 'parent_group')

    # Assert that the 'child_group' was deleted from pending
    assert 'child_group' not in pending

    # Clean up after the test
    mocker.stopall()
