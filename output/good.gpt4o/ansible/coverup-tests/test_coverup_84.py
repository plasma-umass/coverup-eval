# file lib/ansible/plugins/inventory/auto.py:30-62
# lines [30, 32, 34, 35, 36, 37, 39, 40, 42, 43, 44, 45, 47, 48, 50, 52, 53, 55, 56, 58, 59, 60, 61, 62]
# branches ['35->36', '35->37', '47->48', '47->50', '52->53', '52->55', '55->56', '55->58']

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.inventory.auto import InventoryModule
from ansible.errors import AnsibleParserError
from ansible.plugins.inventory import BaseInventoryPlugin

@pytest.fixture
def mock_loader():
    return Mock()

@pytest.fixture
def mock_inventory():
    return Mock()

@pytest.fixture
def mock_inventory_loader():
    with patch('ansible.plugins.inventory.auto.inventory_loader') as mock:
        yield mock

class MockBaseInventoryPlugin(BaseInventoryPlugin):
    def verify_file(self, path):
        return True

def test_verify_file():
    inventory_module = InventoryModule()
    assert not inventory_module.verify_file('test.txt')
    with patch.object(BaseInventoryPlugin, 'verify_file', return_value=True):
        assert inventory_module.verify_file('test.yml')
        assert inventory_module.verify_file('test.yaml')

def test_parse_no_plugin_key(mock_loader, mock_inventory):
    inventory_module = InventoryModule()
    mock_loader.load_from_file.return_value = {}
    with pytest.raises(AnsibleParserError, match="no root 'plugin' key found"):
        inventory_module.parse(mock_inventory, mock_loader, 'test.yml')

def test_parse_unknown_plugin(mock_loader, mock_inventory, mock_inventory_loader):
    inventory_module = InventoryModule()
    mock_loader.load_from_file.return_value = {'plugin': 'unknown_plugin'}
    mock_inventory_loader.get.return_value = None
    with pytest.raises(AnsibleParserError, match="specifies unknown plugin"):
        inventory_module.parse(mock_inventory, mock_loader, 'test.yml')

def test_parse_plugin_verification_fail(mock_loader, mock_inventory, mock_inventory_loader):
    inventory_module = InventoryModule()
    mock_loader.load_from_file.return_value = {'plugin': 'known_plugin'}
    mock_plugin = Mock()
    mock_plugin.verify_file.return_value = False
    mock_inventory_loader.get.return_value = mock_plugin
    with pytest.raises(AnsibleParserError, match="could not be verified by plugin"):
        inventory_module.parse(mock_inventory, mock_loader, 'test.yml')

def test_parse_success(mock_loader, mock_inventory, mock_inventory_loader):
    inventory_module = InventoryModule()
    mock_loader.load_from_file.return_value = {'plugin': 'known_plugin'}
    mock_plugin = Mock()
    mock_plugin.verify_file.return_value = True
    mock_inventory_loader.get.return_value = mock_plugin
    inventory_module.parse(mock_inventory, mock_loader, 'test.yml')
    mock_plugin.parse.assert_called_once_with(mock_inventory, mock_loader, 'test.yml', cache=True)
    mock_plugin.update_cache_if_changed.assert_called_once()

def test_parse_success_no_update_cache(mock_loader, mock_inventory, mock_inventory_loader):
    inventory_module = InventoryModule()
    mock_loader.load_from_file.return_value = {'plugin': 'known_plugin'}
    mock_plugin = Mock()
    mock_plugin.verify_file.return_value = True
    mock_plugin.update_cache_if_changed.side_effect = AttributeError
    mock_inventory_loader.get.return_value = mock_plugin
    inventory_module.parse(mock_inventory, mock_loader, 'test.yml')
    mock_plugin.parse.assert_called_once_with(mock_inventory, mock_loader, 'test.yml', cache=True)
    mock_plugin.update_cache_if_changed.assert_called_once()
