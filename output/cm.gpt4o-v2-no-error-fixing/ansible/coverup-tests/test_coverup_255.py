# file: lib/ansible/plugins/inventory/yaml.py:87-94
# asked: {"lines": [87, 89, 90, 91, 92, 93, 94], "branches": [[90, 91], [90, 94], [92, 93], [92, 94]]}
# gained: {"lines": [87, 89, 90, 91, 92, 93, 94], "branches": [[90, 91], [90, 94], [92, 93], [92, 94]]}

import os
import pytest
from unittest.mock import MagicMock
from ansible.plugins.inventory.yaml import InventoryModule

@pytest.fixture
def inventory_module():
    module = InventoryModule()
    module.get_option = MagicMock(return_value=['.yaml', '.yml'])
    return module

def test_verify_file_with_valid_yaml_extension(inventory_module, mocker):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.access', return_value=True)
    mocker.patch('ansible.plugins.inventory.BaseFileInventoryPlugin.verify_file', return_value=True)
    
    path = '/path/to/valid/file.yaml'
    assert inventory_module.verify_file(path) == True

def test_verify_file_with_invalid_extension(inventory_module, mocker):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.access', return_value=True)
    mocker.patch('ansible.plugins.inventory.BaseFileInventoryPlugin.verify_file', return_value=True)
    
    path = '/path/to/invalid/file.txt'
    assert inventory_module.verify_file(path) == False

def test_verify_file_with_no_extension(inventory_module, mocker):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.access', return_value=True)
    mocker.patch('ansible.plugins.inventory.BaseFileInventoryPlugin.verify_file', return_value=True)
    
    path = '/path/to/valid/file'
    assert inventory_module.verify_file(path) == True

def test_verify_file_base_class_returns_false(inventory_module, mocker):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.access', return_value=True)
    mocker.patch('ansible.plugins.inventory.BaseFileInventoryPlugin.verify_file', return_value=False)
    
    path = '/path/to/valid/file.yaml'
    assert inventory_module.verify_file(path) == False
