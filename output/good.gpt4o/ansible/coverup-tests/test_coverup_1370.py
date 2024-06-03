# file lib/ansible/inventory/manager.py:243-333
# lines [246, 247, 248, 251, 254, 255, 256, 258, 260, 261, 264, 265, 266, 267, 268, 273, 276, 278, 279, 282, 283, 284, 285, 287, 288, 290, 291, 292, 293, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 308, 310, 311, 315, 317, 319, 320, 321, 322, 325, 326, 328, 331, 333]
# branches ['254->255', '254->273', '256->258', '256->310', '260->261', '260->264', '267->256', '267->268', '276->278', '276->310', '287->288', '287->308', '310->311', '310->315', '315->317', '315->331', '317->319', '317->325', '319->320', '319->325', '321->319', '321->322', '325->326', '325->328']

import os
import pytest
from unittest.mock import MagicMock, patch
from ansible.inventory.manager import InventoryManager
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.utils.display import Display

@pytest.fixture
def inventory_manager():
    loader = MagicMock()
    manager = InventoryManager(loader)
    manager._inventory = MagicMock()
    manager._inventory.current_source = None
    manager._inventory.processed_sources = []
    return manager

@pytest.fixture
def mock_display():
    with patch('ansible.utils.display.Display') as mock_display:
        yield mock_display

@pytest.fixture
def mock_fetch_inventory_plugins():
    with patch.object(InventoryManager, '_fetch_inventory_plugins') as mock_plugins:
        yield mock_plugins

def test_parse_source_directory(inventory_manager, mock_display, mock_fetch_inventory_plugins, tmp_path):
    # Create a temporary directory with files
    temp_dir = tmp_path / "inventory_dir"
    temp_dir.mkdir()
    (temp_dir / "file1").write_text("content1")
    (temp_dir / "file2").write_text("content2")

    # Mock the plugins
    mock_plugin = MagicMock()
    mock_plugin.verify_file.return_value = True
    mock_plugin.parse.side_effect = AnsibleParserError("Parsing error")
    mock_fetch_inventory_plugins.return_value = [mock_plugin]

    # Call the method
    result = inventory_manager.parse_source(str(temp_dir))

    # Assertions
    assert not result
    assert inventory_manager._inventory.current_source is None
    assert len(inventory_manager._inventory.processed_sources) == 0
    assert mock_plugin.verify_file.call_count == 2
    assert mock_plugin.parse.call_count == 2

def test_parse_source_file(inventory_manager, mock_display, mock_fetch_inventory_plugins, tmp_path):
    # Create a temporary file
    temp_file = tmp_path / "inventory_file"
    temp_file.write_text("content")

    # Mock the plugins
    mock_plugin = MagicMock()
    mock_plugin.verify_file.return_value = True
    mock_plugin.parse.side_effect = AnsibleParserError("Parsing error")
    mock_fetch_inventory_plugins.return_value = [mock_plugin]

    # Call the method
    result = inventory_manager.parse_source(str(temp_file))

    # Assertions
    assert not result
    assert inventory_manager._inventory.current_source is None
    assert len(inventory_manager._inventory.processed_sources) == 0
    assert mock_plugin.verify_file.call_count == 1
    assert mock_plugin.parse.call_count == 1

def test_parse_source_plugin_success(inventory_manager, mock_display, mock_fetch_inventory_plugins, tmp_path):
    # Create a temporary file
    temp_file = tmp_path / "inventory_file"
    temp_file.write_text("content")

    # Mock the plugins
    mock_plugin = MagicMock()
    mock_plugin.verify_file.return_value = True
    mock_plugin.parse.return_value = True
    mock_fetch_inventory_plugins.return_value = [mock_plugin]

    # Call the method
    result = inventory_manager.parse_source(str(temp_file))

    # Assertions
    assert result
    assert inventory_manager._inventory.current_source is None
    assert len(inventory_manager._inventory.processed_sources) == 1
    assert mock_plugin.verify_file.call_count == 1
    assert mock_plugin.parse.call_count == 1

def test_parse_source_plugin_failure(inventory_manager, mock_display, mock_fetch_inventory_plugins, tmp_path):
    # Create a temporary file
    temp_file = tmp_path / "inventory_file"
    temp_file.write_text("content")

    # Mock the plugins
    mock_plugin = MagicMock()
    mock_plugin.verify_file.return_value = False
    mock_fetch_inventory_plugins.return_value = [mock_plugin]

    # Call the method
    result = inventory_manager.parse_source(str(temp_file))

    # Assertions
    assert not result
    assert inventory_manager._inventory.current_source is None
    assert len(inventory_manager._inventory.processed_sources) == 0
    assert mock_plugin.verify_file.call_count == 1
    assert mock_plugin.parse.call_count == 0
