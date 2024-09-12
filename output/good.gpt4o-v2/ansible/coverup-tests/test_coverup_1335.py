# file: lib/ansible/inventory/manager.py:243-333
# asked: {"lines": [255, 256, 258, 260, 261, 264, 265, 266, 267, 268, 284, 285, 299, 300, 301, 302, 303, 304, 305, 306, 319, 320, 321, 322, 326], "branches": [[254, 255], [256, 258], [256, 310], [260, 261], [260, 264], [267, 256], [267, 268], [315, 331], [317, 319], [319, 320], [319, 325], [321, 319], [321, 322], [325, 326]]}
# gained: {"lines": [284, 285, 299, 300, 301, 302, 303, 304, 305, 306, 319, 320, 321, 322, 326], "branches": [[315, 331], [317, 319], [319, 320], [319, 325], [321, 322], [325, 326]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def inventory_manager():
    loader = MagicMock()
    return InventoryManager(loader)

def test_parse_source_directory(inventory_manager, monkeypatch):
    source = '/some/directory'
    b_source = source.encode('utf-8')
    
    def mock_isdir(path):
        return path == b_source

    def mock_listdir(path):
        return ['file1', 'file2']

    def mock_parse_source(path, cache=False):
        return True

    monkeypatch.setattr(os.path, 'isdir', mock_isdir)
    monkeypatch.setattr(os, 'listdir', mock_listdir)
    monkeypatch.setattr(inventory_manager, 'parse_source', mock_parse_source)

    parsed = inventory_manager.parse_source(source)
    assert parsed

def test_parse_source_plugin_verification_failure(inventory_manager, monkeypatch):
    source = '/some/file'
    b_source = source.encode('utf-8')
    
    def mock_isdir(path):
        return False

    def mock_fetch_inventory_plugins():
        plugin = MagicMock()
        plugin.verify_file.side_effect = Exception("Verification failed")
        return [plugin]

    monkeypatch.setattr(os.path, 'isdir', mock_isdir)
    monkeypatch.setattr(inventory_manager, '_fetch_inventory_plugins', mock_fetch_inventory_plugins)

    parsed = inventory_manager.parse_source(source)
    assert not parsed

def test_parse_source_plugin_parsing_failure(inventory_manager, monkeypatch):
    source = '/some/file'
    b_source = source.encode('utf-8')
    
    def mock_isdir(path):
        return False

    def mock_fetch_inventory_plugins():
        plugin = MagicMock()
        plugin.verify_file.return_value = True
        plugin.parse.side_effect = AnsibleParserError("Parsing failed")
        return [plugin]

    monkeypatch.setattr(os.path, 'isdir', mock_isdir)
    monkeypatch.setattr(inventory_manager, '_fetch_inventory_plugins', mock_fetch_inventory_plugins)

    parsed = inventory_manager.parse_source(source)
    assert not parsed

def test_parse_source_plugin_general_failure(inventory_manager, monkeypatch):
    source = '/some/file'
    b_source = source.encode('utf-8')
    
    def mock_isdir(path):
        return False

    def mock_fetch_inventory_plugins():
        plugin = MagicMock()
        plugin.verify_file.return_value = True
        plugin.parse.side_effect = Exception("General failure")
        return [plugin]

    monkeypatch.setattr(os.path, 'isdir', mock_isdir)
    monkeypatch.setattr(inventory_manager, '_fetch_inventory_plugins', mock_fetch_inventory_plugins)

    parsed = inventory_manager.parse_source(source)
    assert not parsed

def test_parse_source_no_plugins(inventory_manager, monkeypatch):
    source = '/some/file'
    b_source = source.encode('utf-8')
    
    def mock_isdir(path):
        return False

    def mock_fetch_inventory_plugins():
        return []

    monkeypatch.setattr(os.path, 'isdir', mock_isdir)
    monkeypatch.setattr(inventory_manager, '_fetch_inventory_plugins', mock_fetch_inventory_plugins)

    parsed = inventory_manager.parse_source(source)
    assert not parsed

def test_parse_source_default_inventory(inventory_manager, monkeypatch):
    source = '/etc/ansible/hosts'
    b_source = source.encode('utf-8')
    
    def mock_isdir(path):
        return False

    def mock_exists(path):
        return False

    def mock_fetch_inventory_plugins():
        return []

    monkeypatch.setattr(os.path, 'isdir', mock_isdir)
    monkeypatch.setattr(os.path, 'exists', mock_exists)
    monkeypatch.setattr(inventory_manager, '_fetch_inventory_plugins', mock_fetch_inventory_plugins)

    parsed = inventory_manager.parse_source(source)
    assert not parsed

def test_parse_source_failures(inventory_manager, monkeypatch):
    source = '/some/file'
    b_source = source.encode('utf-8')
    
    def mock_isdir(path):
        return False

    def mock_fetch_inventory_plugins():
        plugin = MagicMock()
        plugin.verify_file.return_value = True
        plugin.parse.side_effect = AnsibleParserError("Parsing failed")
        return [plugin]

    monkeypatch.setattr(os.path, 'isdir', mock_isdir)
    monkeypatch.setattr(inventory_manager, '_fetch_inventory_plugins', mock_fetch_inventory_plugins)

    with patch('ansible.inventory.manager.C.INVENTORY_ANY_UNPARSED_IS_FAILED', True):
        with pytest.raises(AnsibleError):
            inventory_manager.parse_source(source)
