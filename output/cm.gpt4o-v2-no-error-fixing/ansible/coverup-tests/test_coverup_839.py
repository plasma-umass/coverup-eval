# file: lib/ansible/inventory/manager.py:650-651
# asked: {"lines": [651], "branches": []}
# gained: {"lines": [651], "branches": []}

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader

def test_clear_pattern_cache():
    loader = DataLoader()
    manager = InventoryManager(loader)
    manager._pattern_cache = {'some': 'data'}
    manager.clear_pattern_cache()
    assert manager._pattern_cache == {}
