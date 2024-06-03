# file lib/ansible/inventory/manager.py:365-420
# lines [365, 372, 375, 376, 378, 380, 381, 382, 384, 385, 389, 391, 393, 394, 397, 399, 400, 402, 404, 406, 409, 410, 411, 412, 414, 415, 416, 417, 418, 420]
# branches ['375->376', '375->378', '380->381', '380->420', '381->382', '381->384', '384->385', '384->389', '391->393', '391->409', '397->399', '397->402', '402->404', '402->406', '409->410', '409->411', '411->412', '411->414', '415->416', '415->417', '417->418', '417->420']

import pytest
from unittest.mock import MagicMock, patch
from ansible.inventory.manager import InventoryManager
from ansible.errors import AnsibleOptionsError

@pytest.fixture
def inventory_manager():
    loader = MagicMock()
    sources = MagicMock()
    manager = InventoryManager(loader, sources)
    manager._subset = None
    manager._restriction = None
    manager._hosts_patterns_cache = {}
    return manager

def test_get_hosts_with_pattern_list(inventory_manager):
    inventory_manager._subset = ['subset1']
    inventory_manager._restriction = ['restriction1']
    inventory_manager._hosts_patterns_cache = {}
    
    mock_host = MagicMock()
    mock_host._uuid = 'uuid1'
    mock_host.name = 'host1'
    
    with patch('ansible.inventory.manager.split_host_pattern', return_value=['pattern1']) as mock_split, \
         patch.object(inventory_manager, '_evaluate_patterns', return_value=[mock_host]) as mock_eval, \
         patch('ansible.inventory.manager.deduplicate_list', return_value=[mock_host]) as mock_dedupe:
        
        hosts = inventory_manager.get_hosts(pattern=['pattern1'], ignore_limits=False, ignore_restrictions=False, order='sorted')
        
        mock_split.assert_called_once_with(['pattern1'])
        mock_eval.assert_called()
        mock_dedupe.assert_called()
        assert len(hosts) == 1
        assert hosts[0].name == 'host1'

def test_get_hosts_with_invalid_order(inventory_manager):
    with pytest.raises(AnsibleOptionsError, match="Invalid 'order' specified for inventory hosts: invalid_order"):
        inventory_manager.get_hosts(pattern="all", order='invalid_order')

def test_get_hosts_with_shuffle_order(inventory_manager):
    mock_host1 = MagicMock()
    mock_host1._uuid = 'uuid1'
    mock_host1.name = 'host1'
    
    mock_host2 = MagicMock()
    mock_host2._uuid = 'uuid2'
    mock_host2.name = 'host2'
    
    with patch('ansible.inventory.manager.split_host_pattern', return_value=['pattern1']) as mock_split, \
         patch.object(inventory_manager, '_evaluate_patterns', return_value=[mock_host1, mock_host2]) as mock_eval, \
         patch('ansible.inventory.manager.deduplicate_list', return_value=[mock_host1, mock_host2]) as mock_dedupe, \
         patch('ansible.inventory.manager.shuffle') as mock_shuffle:
        
        hosts = inventory_manager.get_hosts(pattern="all", order='shuffle')
        
        mock_split.assert_called_once_with("all")
        mock_eval.assert_called()
        mock_dedupe.assert_called()
        mock_shuffle.assert_called()
        assert len(hosts) == 2

def test_get_hosts_with_reverse_inventory_order(inventory_manager):
    mock_host1 = MagicMock()
    mock_host1._uuid = 'uuid1'
    mock_host1.name = 'host1'
    
    mock_host2 = MagicMock()
    mock_host2._uuid = 'uuid2'
    mock_host2.name = 'host2'
    
    with patch('ansible.inventory.manager.split_host_pattern', return_value=['pattern1']) as mock_split, \
         patch.object(inventory_manager, '_evaluate_patterns', return_value=[mock_host1, mock_host2]) as mock_eval, \
         patch('ansible.inventory.manager.deduplicate_list', return_value=[mock_host1, mock_host2]) as mock_dedupe:
        
        hosts = inventory_manager.get_hosts(pattern="all", order='reverse_inventory')
        
        mock_split.assert_called_once_with("all")
        mock_eval.assert_called()
        mock_dedupe.assert_called()
        assert len(hosts) == 2
        assert hosts[0].name == 'host2'
        assert hosts[1].name == 'host1'
