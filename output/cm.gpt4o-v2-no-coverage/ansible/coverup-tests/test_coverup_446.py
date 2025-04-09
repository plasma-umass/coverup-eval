# file: lib/ansible/plugins/inventory/constructed.py:104-113
# asked: {"lines": [104, 106, 107, 108, 110, 111, 113], "branches": [[107, 108], [107, 113], [110, 111], [110, 113]]}
# gained: {"lines": [104, 106, 107, 108, 110, 111, 113], "branches": [[107, 108], [107, 113], [110, 111], [110, 113]]}

import os
import pytest
from unittest.mock import MagicMock
from ansible.plugins.inventory.constructed import InventoryModule
from ansible import constants as C

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_verify_file_no_extension(inventory_module, mocker):
    mocker.patch('ansible.plugins.inventory.BaseInventoryPlugin.verify_file', return_value=True)
    path = "/path/to/file"
    assert inventory_module.verify_file(path) == True

def test_verify_file_with_config_extension(inventory_module, mocker):
    mocker.patch('ansible.plugins.inventory.BaseInventoryPlugin.verify_file', return_value=True)
    path = "/path/to/file.config"
    assert inventory_module.verify_file(path) == True

def test_verify_file_with_yaml_extension(inventory_module, mocker):
    mocker.patch('ansible.plugins.inventory.BaseInventoryPlugin.verify_file', return_value=True)
    for ext in C.YAML_FILENAME_EXTENSIONS:
        path = f"/path/to/file{ext}"
        assert inventory_module.verify_file(path) == True

def test_verify_file_with_invalid_extension(inventory_module, mocker):
    mocker.patch('ansible.plugins.inventory.BaseInventoryPlugin.verify_file', return_value=True)
    path = "/path/to/file.txt"
    assert inventory_module.verify_file(path) == False

def test_verify_file_super_returns_false(inventory_module, mocker):
    mocker.patch('ansible.plugins.inventory.BaseInventoryPlugin.verify_file', return_value=False)
    path = "/path/to/file"
    assert inventory_module.verify_file(path) == False
