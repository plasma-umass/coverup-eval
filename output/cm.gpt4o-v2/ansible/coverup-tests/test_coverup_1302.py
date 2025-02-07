# file: lib/ansible/plugins/inventory/ini.py:249-254
# asked: {"lines": [], "branches": [[252, 250]]}
# gained: {"lines": [], "branches": [[252, 250]]}

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
            'parents': ['parent1'],
            'state': 'children'
        },
        'parent1': {
            'parents': [],
            'state': 'children'
        }
    }

    inventory_module._add_pending_children('group1', pending)

    inventory_module.inventory.add_child.assert_any_call('parent1', 'group1')
    assert 'group1' not in pending
    assert 'parent1' not in pending

def test_add_pending_children_no_recursive(inventory_module):
    pending = {
        'group1': {
            'parents': ['parent1'],
            'state': 'children'
        },
        'parent1': {
            'parents': [],
            'state': 'complete'
        }
    }

    inventory_module._add_pending_children('group1', pending)

    inventory_module.inventory.add_child.assert_any_call('parent1', 'group1')
    assert 'group1' not in pending
    assert 'parent1' in pending
