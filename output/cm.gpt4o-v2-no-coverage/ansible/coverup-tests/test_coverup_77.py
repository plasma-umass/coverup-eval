# file: lib/ansible/plugins/inventory/auto.py:30-62
# asked: {"lines": [30, 32, 34, 35, 36, 37, 39, 40, 42, 43, 44, 45, 47, 48, 50, 52, 53, 55, 56, 58, 59, 60, 61, 62], "branches": [[35, 36], [35, 37], [47, 48], [47, 50], [52, 53], [52, 55], [55, 56], [55, 58]]}
# gained: {"lines": [30, 32, 34, 35, 36, 37, 39, 40, 42, 43, 47, 48, 50, 52, 53, 55, 56, 58, 59, 60], "branches": [[35, 36], [35, 37], [47, 48], [47, 50], [52, 53], [52, 55], [55, 56], [55, 58]]}

import pytest
from unittest.mock import Mock, patch
from ansible.errors import AnsibleParserError
from ansible.plugins.inventory import BaseInventoryPlugin
from ansible.plugins.loader import inventory_loader
from ansible.plugins.inventory.auto import InventoryModule

@pytest.fixture
def mock_loader():
    return Mock()

@pytest.fixture
def mock_inventory():
    return Mock()

@pytest.fixture
def mock_inventory_loader(monkeypatch):
    mock_loader = Mock()
    monkeypatch.setattr(inventory_loader, 'get', mock_loader.get)
    return mock_loader

@pytest.fixture
def mock_os(monkeypatch):
    mock_os = Mock()
    monkeypatch.setattr('os.path.exists', mock_os.path.exists)
    monkeypatch.setattr('os.access', mock_os.access)
    return mock_os

def test_verify_file(mock_os):
    plugin = InventoryModule()
    mock_os.path.exists.return_value = True
    mock_os.access.return_value = True
    assert not plugin.verify_file('invalid.txt')
    assert plugin.verify_file('valid.yml')
    assert plugin.verify_file('valid.yaml')

def test_parse_no_plugin_key(mock_loader, mock_inventory):
    plugin = InventoryModule()
    mock_loader.load_from_file.return_value = {}
    with pytest.raises(AnsibleParserError, match="no root 'plugin' key found"):
        plugin.parse(mock_inventory, mock_loader, 'some_path')

def test_parse_unknown_plugin(mock_loader, mock_inventory, mock_inventory_loader):
    plugin = InventoryModule()
    mock_loader.load_from_file.return_value = {'plugin': 'unknown_plugin'}
    mock_inventory_loader.get.return_value = None
    with pytest.raises(AnsibleParserError, match="specifies unknown plugin"):
        plugin.parse(mock_inventory, mock_loader, 'some_path')

def test_parse_plugin_verification_fail(mock_loader, mock_inventory, mock_inventory_loader):
    plugin = InventoryModule()
    mock_loader.load_from_file.return_value = {'plugin': 'known_plugin'}
    mock_plugin = Mock()
    mock_plugin.verify_file.return_value = False
    mock_inventory_loader.get.return_value = mock_plugin
    with pytest.raises(AnsibleParserError, match="could not be verified by plugin"):
        plugin.parse(mock_inventory, mock_loader, 'some_path')

def test_parse_success(mock_loader, mock_inventory, mock_inventory_loader):
    plugin = InventoryModule()
    mock_loader.load_from_file.return_value = {'plugin': 'known_plugin'}
    mock_plugin = Mock()
    mock_plugin.verify_file.return_value = True
    mock_inventory_loader.get.return_value = mock_plugin
    plugin.parse(mock_inventory, mock_loader, 'some_path')
    mock_plugin.parse.assert_called_once_with(mock_inventory, mock_loader, 'some_path', cache=True)
    mock_plugin.update_cache_if_changed.assert_called_once()
