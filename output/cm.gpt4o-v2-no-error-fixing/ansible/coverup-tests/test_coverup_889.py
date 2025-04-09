# file: lib/ansible/plugins/inventory/constructed.py:104-113
# asked: {"lines": [106, 107, 108, 110, 111, 113], "branches": [[107, 108], [107, 113], [110, 111], [110, 113]]}
# gained: {"lines": [106, 107, 108, 110, 111, 113], "branches": [[107, 108], [107, 113], [110, 111], [110, 113]]}

import pytest
import os
from ansible.plugins.inventory.constructed import InventoryModule
from ansible import constants as C
from unittest.mock import MagicMock

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_verify_file_with_valid_extension(inventory_module, mocker):
    mocker.patch('ansible.plugins.inventory.BaseInventoryPlugin.verify_file', return_value=True)
    mocker.patch('os.path.splitext', return_value=('filename', '.yml'))
    
    path = 'some_path.yml'
    assert inventory_module.verify_file(path) == True

def test_verify_file_with_invalid_extension(inventory_module, mocker):
    mocker.patch('ansible.plugins.inventory.BaseInventoryPlugin.verify_file', return_value=True)
    mocker.patch('os.path.splitext', return_value=('filename', '.txt'))
    
    path = 'some_path.txt'
    assert inventory_module.verify_file(path) == False

def test_verify_file_with_no_extension(inventory_module, mocker):
    mocker.patch('ansible.plugins.inventory.BaseInventoryPlugin.verify_file', return_value=True)
    mocker.patch('os.path.splitext', return_value=('filename', ''))
    
    path = 'some_path'
    assert inventory_module.verify_file(path) == True

def test_verify_file_super_returns_false(inventory_module, mocker):
    mocker.patch('ansible.plugins.inventory.BaseInventoryPlugin.verify_file', return_value=False)
    
    path = 'some_path.yml'
    assert inventory_module.verify_file(path) == False
