# file: lib/ansible/plugins/inventory/auto.py:30-62
# asked: {"lines": [30, 32, 34, 35, 36, 37, 39, 40, 42, 43, 44, 45, 47, 48, 50, 52, 53, 55, 56, 58, 59, 60, 61, 62], "branches": [[35, 36], [35, 37], [47, 48], [47, 50], [52, 53], [52, 55], [55, 56], [55, 58]]}
# gained: {"lines": [30, 32, 34, 35, 36, 37, 39, 40, 42, 43, 47, 48, 50, 52, 53, 55, 56, 58, 59, 60], "branches": [[35, 36], [35, 37], [47, 48], [47, 50], [52, 53], [52, 55], [55, 56], [55, 58]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleParserError
from ansible.plugins.inventory.auto import InventoryModule

@pytest.fixture
def inventory_module():
    return InventoryModule()

@patch('ansible.plugins.inventory.auto.BaseInventoryPlugin.verify_file')
def test_verify_file_yaml(mock_verify_file, inventory_module):
    mock_verify_file.return_value = True
    assert inventory_module.verify_file('test.yml') is True
    mock_verify_file.assert_called_once_with('test.yml')

def test_verify_file_non_yaml(inventory_module):
    assert inventory_module.verify_file('test.txt') is False

@patch('ansible.plugins.loader.inventory_loader.get')
@patch('ansible.plugins.inventory.auto.InventoryModule.verify_file')
@patch('ansible.plugins.inventory.auto.BaseInventoryPlugin.verify_file')
@patch('ansible.plugins.inventory.auto.BaseInventoryPlugin.parse')
def test_parse_valid_plugin(mock_base_parse, mock_base_verify, mock_verify, mock_get, inventory_module):
    mock_loader = MagicMock()
    mock_inventory = MagicMock()
    mock_plugin = MagicMock()
    mock_get.return_value = mock_plugin
    mock_loader.load_from_file.return_value = {'plugin': 'valid_plugin'}
    mock_plugin.verify_file.return_value = True

    inventory_module.parse(mock_inventory, mock_loader, 'test.yml')

    mock_get.assert_called_once_with('valid_plugin')
    mock_plugin.verify_file.assert_called_once_with('test.yml')
    mock_plugin.parse.assert_called_once_with(mock_inventory, mock_loader, 'test.yml', cache=True)

@patch('ansible.plugins.loader.inventory_loader.get')
def test_parse_no_plugin_key(mock_get, inventory_module):
    mock_loader = MagicMock()
    mock_inventory = MagicMock()
    mock_loader.load_from_file.return_value = {}

    with pytest.raises(AnsibleParserError, match="no root 'plugin' key found"):
        inventory_module.parse(mock_inventory, mock_loader, 'test.yml')

    mock_get.assert_not_called()

@patch('ansible.plugins.loader.inventory_loader.get')
def test_parse_unknown_plugin(mock_get, inventory_module):
    mock_loader = MagicMock()
    mock_inventory = MagicMock()
    mock_loader.load_from_file.return_value = {'plugin': 'unknown_plugin'}
    mock_get.return_value = None

    with pytest.raises(AnsibleParserError, match="specifies unknown plugin"):
        inventory_module.parse(mock_inventory, mock_loader, 'test.yml')

    mock_get.assert_called_once_with('unknown_plugin')

@patch('ansible.plugins.loader.inventory_loader.get')
@patch('ansible.plugins.inventory.auto.InventoryModule.verify_file')
def test_parse_plugin_verification_fail(mock_verify, mock_get, inventory_module):
    mock_loader = MagicMock()
    mock_inventory = MagicMock()
    mock_plugin = MagicMock()
    mock_loader.load_from_file.return_value = {'plugin': 'valid_plugin'}
    mock_get.return_value = mock_plugin
    mock_plugin.verify_file.return_value = False

    with pytest.raises(AnsibleParserError, match="could not be verified by plugin"):
        inventory_module.parse(mock_inventory, mock_loader, 'test.yml')

    mock_get.assert_called_once_with('valid_plugin')
    mock_plugin.verify_file.assert_called_once_with('test.yml')

@patch('ansible.plugins.loader.inventory_loader.get')
@patch('ansible.plugins.inventory.auto.InventoryModule.verify_file')
@patch('ansible.plugins.inventory.auto.BaseInventoryPlugin.verify_file')
@patch('ansible.plugins.inventory.auto.BaseInventoryPlugin.parse')
def test_parse_update_cache_if_changed(mock_base_parse, mock_base_verify, mock_verify, mock_get, inventory_module):
    mock_loader = MagicMock()
    mock_inventory = MagicMock()
    mock_plugin = MagicMock()
    mock_get.return_value = mock_plugin
    mock_loader.load_from_file.return_value = {'plugin': 'valid_plugin'}
    mock_plugin.verify_file.return_value = True

    inventory_module.parse(mock_inventory, mock_loader, 'test.yml')

    mock_plugin.update_cache_if_changed.assert_called_once()
