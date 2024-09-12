# file: lib/ansible/plugins/inventory/auto.py:30-62
# asked: {"lines": [44, 45, 61, 62], "branches": []}
# gained: {"lines": [44, 45, 61, 62], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.errors import AnsibleParserError
from ansible.plugins.inventory.auto import InventoryModule
from ansible.plugins.loader import inventory_loader

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_parse_attribute_error_handling(inventory_module):
    inventory = Mock()
    loader = Mock()
    path = 'dummy_path.yml'
    
    # Mock the loader to return an object that raises AttributeError on get
    loader.load_from_file.return_value = Mock(get=Mock(side_effect=AttributeError))
    
    with pytest.raises(AnsibleParserError, match="no root 'plugin' key found"):
        inventory_module.parse(inventory, loader, path)

def test_parse_update_cache_if_changed_handling(inventory_module):
    inventory = Mock()
    loader = Mock()
    path = 'dummy_path.yml'
    
    # Mock the loader to return a valid config
    loader.load_from_file.return_value = {'plugin': 'valid_plugin'}
    
    # Mock the inventory_loader to return a plugin that raises AttributeError on update_cache_if_changed
    plugin = Mock()
    plugin.verify_file.return_value = True
    plugin.update_cache_if_changed.side_effect = AttributeError
    with patch.object(inventory_loader, 'get', return_value=plugin):
        inventory_module.parse(inventory, loader, path)
    
    # Ensure update_cache_if_changed was called and handled
    plugin.update_cache_if_changed.assert_called_once()

@patch('os.path.exists', return_value=True)
@patch('os.access', return_value=True)
def test_verify_file(mock_exists, mock_access, inventory_module):
    # Test with .yml file
    assert inventory_module.verify_file('test.yml') == True
    
    # Test with .yaml file
    assert inventory_module.verify_file('test.yaml') == True
    
    # Test with invalid file extension
    assert inventory_module.verify_file('test.txt') == False
