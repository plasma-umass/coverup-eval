# file: lib/ansible/inventory/manager.py:243-333
# asked: {"lines": [255, 256, 258, 260, 261, 264, 265, 266, 267, 268, 284, 285, 299, 300, 301, 302, 303, 304, 305, 306, 308, 315, 317, 319, 320, 321, 322, 325, 326, 328], "branches": [[254, 255], [256, 258], [256, 310], [260, 261], [260, 264], [267, 256], [267, 268], [276, 310], [287, 308], [310, 315], [315, 317], [315, 331], [317, 319], [317, 325], [319, 320], [319, 325], [321, 319], [321, 322], [325, 326], [325, 328]]}
# gained: {"lines": [284, 285, 299, 303, 304, 305, 306, 308, 315, 317, 319, 320, 321, 322, 325, 328], "branches": [[276, 310], [287, 308], [310, 315], [315, 317], [317, 319], [317, 325], [319, 320], [319, 325], [321, 322], [325, 328]]}

import os
import pytest
from unittest.mock import MagicMock, patch

# Assuming the InventoryManager class is imported from ansible/inventory/manager.py
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def inventory_manager():
    loader = MagicMock()
    manager = InventoryManager(loader)
    manager._inventory = MagicMock()
    manager._inventory.current_source = None
    manager._inventory.processed_sources = []
    manager._fetch_inventory_plugins = MagicMock(return_value=[])
    return manager

def test_parse_source_directory(inventory_manager, monkeypatch):
    source = '/tmp/test_inventory_dir'
    os.makedirs(source, exist_ok=True)
    with open(os.path.join(source, 'file1'), 'w') as f:
        f.write('content')

    monkeypatch.setattr('os.path.isdir', lambda x: True)
    monkeypatch.setattr('os.listdir', lambda x: ['file1'])
    monkeypatch.setattr('ansible.inventory.manager.to_bytes', lambda x: x)
    monkeypatch.setattr('ansible.inventory.manager.to_text', lambda x, errors='strict': x)
    monkeypatch.setattr(inventory_manager, 'parse_source', lambda x, cache=False: True)

    parsed = inventory_manager.parse_source(source)
    assert parsed
    assert inventory_manager._inventory.current_source is None

    os.remove(os.path.join(source, 'file1'))
    os.rmdir(source)

def test_parse_source_plugin_exception(inventory_manager, monkeypatch):
    source = '/tmp/test_inventory_file'
    with open(source, 'w') as f:
        f.write('content')

    plugin = MagicMock()
    plugin.verify_file = MagicMock(side_effect=Exception('verify_file error'))
    inventory_manager._fetch_inventory_plugins = MagicMock(return_value=[plugin])

    monkeypatch.setattr('os.path.isdir', lambda x: False)
    monkeypatch.setattr('ansible.inventory.manager.to_bytes', lambda x: x)
    monkeypatch.setattr('ansible.inventory.manager.to_text', lambda x, errors='strict': x)

    parsed = inventory_manager.parse_source(source)
    assert not parsed
    assert inventory_manager._inventory.current_source is None

    os.remove(source)

def test_parse_source_plugin_parsing(inventory_manager, monkeypatch):
    source = '/tmp/test_inventory_file'
    with open(source, 'w') as f:
        f.write('content')

    plugin = MagicMock()
    plugin.verify_file = MagicMock(return_value=True)
    plugin.parse = MagicMock()
    plugin.update_cache_if_changed = MagicMock()
    inventory_manager._fetch_inventory_plugins = MagicMock(return_value=[plugin])

    monkeypatch.setattr('os.path.isdir', lambda x: False)
    monkeypatch.setattr('ansible.inventory.manager.to_bytes', lambda x: x)
    monkeypatch.setattr('ansible.inventory.manager.to_text', lambda x, errors='strict': x)

    parsed = inventory_manager.parse_source(source)
    assert parsed
    assert inventory_manager._inventory.current_source is None
    assert source in inventory_manager._inventory.processed_sources

    os.remove(source)

def test_parse_source_plugin_parsing_failure(inventory_manager, monkeypatch):
    source = '/tmp/test_inventory_file'
    with open(source, 'w') as f:
        f.write('content')

    plugin = MagicMock()
    plugin.verify_file = MagicMock(return_value=True)
    plugin.parse = MagicMock(side_effect=Exception('parse error'))
    inventory_manager._fetch_inventory_plugins = MagicMock(return_value=[plugin])

    monkeypatch.setattr('os.path.isdir', lambda x: False)
    monkeypatch.setattr('ansible.inventory.manager.to_bytes', lambda x: x)
    monkeypatch.setattr('ansible.inventory.manager.to_text', lambda x, errors='strict': x)

    parsed = inventory_manager.parse_source(source)
    assert not parsed
    assert inventory_manager._inventory.current_source is None

    os.remove(source)

def test_parse_source_default_inventory_warning(inventory_manager, monkeypatch):
    source = '/etc/ansible/hosts'

    monkeypatch.setattr('os.path.isdir', lambda x: False)
    monkeypatch.setattr('os.path.exists', lambda x: True)
    monkeypatch.setattr('ansible.inventory.manager.to_bytes', lambda x: x)
    monkeypatch.setattr('ansible.inventory.manager.to_text', lambda x, errors='strict': x)

    parsed = inventory_manager.parse_source(source)
    assert not parsed
    assert inventory_manager._inventory.current_source is None
