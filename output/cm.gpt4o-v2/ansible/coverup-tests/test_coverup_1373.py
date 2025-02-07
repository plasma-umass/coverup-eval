# file: lib/ansible/plugins/inventory/yaml.py:87-94
# asked: {"lines": [89, 90, 91, 92, 93, 94], "branches": [[90, 91], [90, 94], [92, 93], [92, 94]]}
# gained: {"lines": [89, 90, 91, 92, 93, 94], "branches": [[90, 91], [90, 94], [92, 93], [92, 94]]}

import os
import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.inventory import BaseFileInventoryPlugin
from ansible.plugins.inventory.yaml import InventoryModule

@pytest.fixture
def inventory_module():
    return InventoryModule()

@pytest.fixture
def mock_super_verify_file(monkeypatch):
    def mock_verify_file(self, path):
        return True
    monkeypatch.setattr(BaseFileInventoryPlugin, 'verify_file', mock_verify_file)

def test_verify_file_with_valid_extension(inventory_module, mock_super_verify_file):
    with patch.object(inventory_module, 'get_option', return_value=['.yaml', '.yml']):
        valid = inventory_module.verify_file('/path/to/inventory.yaml')
        assert valid is True

def test_verify_file_with_invalid_extension(inventory_module, mock_super_verify_file):
    with patch.object(inventory_module, 'get_option', return_value=['.yaml', '.yml']):
        valid = inventory_module.verify_file('/path/to/inventory.txt')
        assert valid is False

def test_verify_file_with_no_extension(inventory_module, mock_super_verify_file):
    with patch.object(inventory_module, 'get_option', return_value=['.yaml', '.yml']):
        valid = inventory_module.verify_file('/path/to/inventory')
        assert valid is True

def test_verify_file_super_fails(inventory_module, monkeypatch):
    def mock_verify_file(self, path):
        return False
    monkeypatch.setattr(BaseFileInventoryPlugin, 'verify_file', mock_verify_file)
    valid = inventory_module.verify_file('/path/to/inventory.yaml')
    assert valid is False
