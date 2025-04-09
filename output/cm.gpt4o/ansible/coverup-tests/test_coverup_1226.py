# file lib/ansible/inventory/manager.py:448-498
# lines [487, 494, 495]
# branches ['486->487', '489->498']

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.errors import AnsibleError
from unittest.mock import MagicMock

@pytest.fixture
def inventory_manager():
    loader = MagicMock()
    sources = MagicMock()
    return InventoryManager(loader, sources)

def test_match_one_pattern_with_special_characters(inventory_manager, mocker):
    # Mocking the necessary methods to control their behavior
    mocker.patch.object(inventory_manager, '_split_subscript', return_value=('expr', slice(None)))
    mocker.patch.object(inventory_manager, '_enumerate_matches', return_value=['host1', 'host2'])
    mocker.patch.object(inventory_manager, '_apply_subscript', side_effect=IndexError)

    pattern = "!group1"
    
    with pytest.raises(AnsibleError, match="No hosts matched the subscripted pattern 'group1'"):
        inventory_manager._match_one_pattern(pattern)
    
    # Ensure the pattern cache is empty after the exception
    assert 'group1' not in inventory_manager._pattern_cache

def test_match_one_pattern_cache_hit(inventory_manager, mocker):
    # Mocking the necessary methods to control their behavior
    mocker.patch.object(inventory_manager, '_split_subscript', return_value=('expr', slice(None)))
    mocker.patch.object(inventory_manager, '_enumerate_matches', return_value=['host1', 'host2'])
    mocker.patch.object(inventory_manager, '_apply_subscript', return_value=['host1'])

    pattern = "group1"
    
    # First call to populate the cache
    result = inventory_manager._match_one_pattern(pattern)
    assert result == ['host1']
    
    # Modify the cache directly to ensure the cache hit
    inventory_manager._pattern_cache[pattern] = ['host1', 'host2']
    
    # Second call should hit the cache
    result = inventory_manager._match_one_pattern(pattern)
    assert result == ['host1', 'host2']
