# file: lib/ansible/inventory/manager.py:348-363
# asked: {"lines": [354, 355, 356], "branches": [[351, 354]]}
# gained: {"lines": [354, 355, 356], "branches": [[351, 354]]}

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def inventory_manager():
    loader = DataLoader()
    return InventoryManager(loader)

def test_match_list_valid_pattern(inventory_manager):
    manager = inventory_manager
    items = ['host1', 'host2', 'host3']
    pattern_str = 'host*'
    expected = ['host1', 'host2', 'host3']
    result = manager._match_list(items, pattern_str)
    assert result == expected

def test_match_list_invalid_pattern(inventory_manager):
    manager = inventory_manager
    items = ['host1', 'host2', 'host3']
    pattern_str = '~[invalid'
    with pytest.raises(AnsibleError, match='Invalid host list pattern: ~\[invalid'):
        manager._match_list(items, pattern_str)
