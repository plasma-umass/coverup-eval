# file: lib/ansible/plugins/inventory/auto.py:30-62
# asked: {"lines": [30, 32, 34, 35, 36, 37, 39, 40, 42, 43, 44, 45, 47, 48, 50, 52, 53, 55, 56, 58, 59, 60, 61, 62], "branches": [[35, 36], [35, 37], [47, 48], [47, 50], [52, 53], [52, 55], [55, 56], [55, 58]]}
# gained: {"lines": [30, 32, 34, 35, 36, 37, 39, 40, 42, 43, 47, 48, 50, 52, 53, 55, 56, 58, 59, 60, 61, 62], "branches": [[35, 36], [35, 37], [47, 48], [47, 50], [52, 53], [52, 55], [55, 56], [55, 58]]}

import pytest
from ansible.plugins.inventory.auto import InventoryModule
from ansible.errors import AnsibleParserError
from unittest.mock import Mock, patch

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_verify_file_yaml(inventory_module, monkeypatch):
    # Mock the super call to return True
    monkeypatch.setattr('ansible.plugins.inventory.BaseInventoryPlugin.verify_file', lambda self, path: True)
    assert inventory_module.verify_file('test.yml') is True

def test_verify_file_non_yaml(inventory_module):
    assert inventory_module.verify_file('test.txt') is False

def test_parse_no_plugin_key(inventory_module, monkeypatch):
    mock_loader = Mock()
    mock_loader.load_from_file.return_value = {}
    mock_inventory = Mock()

    with pytest.raises(AnsibleParserError, match="no root 'plugin' key found"):
        inventory_module.parse(mock_inventory, mock_loader, 'test.yml')

def test_parse_unknown_plugin(inventory_module, monkeypatch):
    mock_loader = Mock()
    mock_loader.load_from_file.return_value = {'plugin': 'unknown_plugin'}
    mock_inventory = Mock()

    with patch('ansible.plugins.loader.inventory_loader.get', return_value=None):
        with pytest.raises(AnsibleParserError, match="specifies unknown plugin"):
            inventory_module.parse(mock_inventory, mock_loader, 'test.yml')

def test_parse_plugin_verification_fail(inventory_module, monkeypatch):
    mock_loader = Mock()
    mock_loader.load_from_file.return_value = {'plugin': 'known_plugin'}
    mock_inventory = Mock()
    mock_plugin = Mock()
    mock_plugin.verify_file.return_value = False

    with patch('ansible.plugins.loader.inventory_loader.get', return_value=mock_plugin):
        with pytest.raises(AnsibleParserError, match="could not be verified by plugin"):
            inventory_module.parse(mock_inventory, mock_loader, 'test.yml')

def test_parse_success(inventory_module, monkeypatch):
    mock_loader = Mock()
    mock_loader.load_from_file.return_value = {'plugin': 'known_plugin'}
    mock_inventory = Mock()
    mock_plugin = Mock()
    mock_plugin.verify_file.return_value = True

    with patch('ansible.plugins.loader.inventory_loader.get', return_value=mock_plugin):
        inventory_module.parse(mock_inventory, mock_loader, 'test.yml')
        mock_plugin.parse.assert_called_once_with(mock_inventory, mock_loader, 'test.yml', cache=True)

def test_parse_update_cache_if_changed(inventory_module, monkeypatch):
    mock_loader = Mock()
    mock_loader.load_from_file.return_value = {'plugin': 'known_plugin'}
    mock_inventory = Mock()
    mock_plugin = Mock()
    mock_plugin.verify_file.return_value = True

    with patch('ansible.plugins.loader.inventory_loader.get', return_value=mock_plugin):
        inventory_module.parse(mock_inventory, mock_loader, 'test.yml')
        mock_plugin.update_cache_if_changed.assert_called_once()

def test_parse_update_cache_if_changed_attribute_error(inventory_module, monkeypatch):
    mock_loader = Mock()
    mock_loader.load_from_file.return_value = {'plugin': 'known_plugin'}
    mock_inventory = Mock()
    mock_plugin = Mock()
    mock_plugin.verify_file.return_value = True
    del mock_plugin.update_cache_if_changed

    with patch('ansible.plugins.loader.inventory_loader.get', return_value=mock_plugin):
        inventory_module.parse(mock_inventory, mock_loader, 'test.yml')
        assert not hasattr(mock_plugin, 'update_cache_if_changed')
