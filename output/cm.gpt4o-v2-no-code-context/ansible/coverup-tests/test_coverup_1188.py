# file: lib/ansible/plugins/inventory/auto.py:30-62
# asked: {"lines": [44, 45], "branches": []}
# gained: {"lines": [44, 45], "branches": []}

import pytest
from ansible.plugins.inventory.auto import InventoryModule
from ansible.errors import AnsibleParserError
from unittest.mock import Mock, patch

@pytest.fixture
def mock_loader():
    return Mock()

@pytest.fixture
def mock_inventory():
    return Mock()

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_parse_with_invalid_config_data(mock_loader, mock_inventory, inventory_module):
    # Mock the loader to return a non-dict object to trigger AttributeError
    mock_loader.load_from_file.return_value = None

    with pytest.raises(AnsibleParserError) as excinfo:
        inventory_module.parse(mock_inventory, mock_loader, 'dummy_path.yml')

    assert "no root 'plugin' key found" in str(excinfo.value)

def test_parse_with_missing_plugin_key(mock_loader, mock_inventory, inventory_module):
    # Mock the loader to return a dict without 'plugin' key
    mock_loader.load_from_file.return_value = {}

    with pytest.raises(AnsibleParserError) as excinfo:
        inventory_module.parse(mock_inventory, mock_loader, 'dummy_path.yml')

    assert "no root 'plugin' key found" in str(excinfo.value)

def test_parse_with_unknown_plugin(mock_loader, mock_inventory, inventory_module):
    # Mock the loader to return a dict with an unknown 'plugin' key
    mock_loader.load_from_file.return_value = {'plugin': 'unknown_plugin'}

    with patch('ansible.plugins.inventory.auto.inventory_loader.get', return_value=None):
        with pytest.raises(AnsibleParserError) as excinfo:
            inventory_module.parse(mock_inventory, mock_loader, 'dummy_path.yml')

    assert "specifies unknown plugin" in str(excinfo.value)

def test_parse_with_unverified_plugin(mock_loader, mock_inventory, inventory_module):
    # Mock the loader to return a dict with a valid 'plugin' key
    mock_loader.load_from_file.return_value = {'plugin': 'known_plugin'}

    mock_plugin = Mock()
    mock_plugin.verify_file.return_value = False

    with patch('ansible.plugins.inventory.auto.inventory_loader.get', return_value=mock_plugin):
        with pytest.raises(AnsibleParserError) as excinfo:
            inventory_module.parse(mock_inventory, mock_loader, 'dummy_path.yml')

    assert "could not be verified by plugin" in str(excinfo.value)

def test_parse_with_valid_plugin(mock_loader, mock_inventory, inventory_module):
    # Mock the loader to return a dict with a valid 'plugin' key
    mock_loader.load_from_file.return_value = {'plugin': 'known_plugin'}

    mock_plugin = Mock()
    mock_plugin.verify_file.return_value = True

    with patch('ansible.plugins.inventory.auto.inventory_loader.get', return_value=mock_plugin):
        inventory_module.parse(mock_inventory, mock_loader, 'dummy_path.yml')

    mock_plugin.parse.assert_called_once_with(mock_inventory, mock_loader, 'dummy_path.yml', cache=True)
    mock_plugin.update_cache_if_changed.assert_called_once()
