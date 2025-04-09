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

def test_verify_file_with_valid_extension(inventory_module, mocker):
    mocker.patch.object(BaseFileInventoryPlugin, 'verify_file', return_value=True)
    mocker.patch.object(inventory_module, 'get_option', return_value=['.yaml', '.yml'])
    
    valid_path = '/path/to/file.yaml'
    assert inventory_module.verify_file(valid_path) == True

def test_verify_file_with_invalid_extension(inventory_module, mocker):
    mocker.patch.object(BaseFileInventoryPlugin, 'verify_file', return_value=True)
    mocker.patch.object(inventory_module, 'get_option', return_value=['.yaml', '.yml'])
    
    invalid_path = '/path/to/file.txt'
    assert inventory_module.verify_file(invalid_path) == False

def test_verify_file_with_no_extension(inventory_module, mocker):
    mocker.patch.object(BaseFileInventoryPlugin, 'verify_file', return_value=True)
    mocker.patch.object(inventory_module, 'get_option', return_value=['.yaml', '.yml'])
    
    no_ext_path = '/path/to/file'
    assert inventory_module.verify_file(no_ext_path) == True

def test_verify_file_super_returns_false(inventory_module, mocker):
    mocker.patch.object(BaseFileInventoryPlugin, 'verify_file', return_value=False)
    
    any_path = '/path/to/file.yaml'
    assert inventory_module.verify_file(any_path) == False
