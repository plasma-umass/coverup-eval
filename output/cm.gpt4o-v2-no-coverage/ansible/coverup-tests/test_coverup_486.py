# file: lib/ansible/plugins/inventory/ini.py:249-254
# asked: {"lines": [249, 250, 251, 252, 253, 254], "branches": [[250, 251], [250, 254], [252, 250], [252, 253]]}
# gained: {"lines": [249, 250, 251, 252, 253, 254], "branches": [[250, 251], [250, 254], [252, 250], [252, 253]]}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.inventory.ini import InventoryModule

@pytest.fixture
def inventory_module():
    module = InventoryModule()
    module.inventory = MagicMock()
    return module

def test_add_pending_children(inventory_module):
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
            'parents': ['parent1'],
            'state': 'children'
        }
    }

    inventory_module._add_pending_children('group1', pending)

    inventory_module.inventory.add_child.assert_any_call('parent1', 'group1')
    inventory_module.inventory.add_child.assert_any_call('parent2', 'group1')
    inventory_module.inventory.add_child.assert_any_call('parent1', 'parent2')
    assert 'group1' not in pending
    assert 'parent2' not in pending
    assert 'parent1' not in pending
