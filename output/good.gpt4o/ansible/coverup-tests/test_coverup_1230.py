# file lib/ansible/inventory/manager.py:348-363
# lines [354, 355, 356]
# branches ['351->354']

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.errors import AnsibleError
from ansible.parsing.dataloader import DataLoader

def test_match_list_invalid_pattern(mocker):
    # Create a DataLoader instance as required by InventoryManager
    loader = DataLoader()
    inventory_manager = InventoryManager(loader)
    
    # Mocking the items list
    items = ['host1', 'host2', 'host3']
    
    # Invalid pattern that should raise an exception
    invalid_pattern = '~[invalid'
    
    with pytest.raises(AnsibleError, match=r'Invalid host list pattern: ~\[invalid'):
        inventory_manager._match_list(items, invalid_pattern)
