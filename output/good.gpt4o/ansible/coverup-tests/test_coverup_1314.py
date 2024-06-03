# file lib/ansible/plugins/inventory/yaml.py:87-94
# lines []
# branches ['90->94']

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.inventory.yaml import InventoryModule

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_verify_file_yaml_extension(inventory_module, mocker):
    mocker.patch('ansible.plugins.inventory.yaml.BaseFileInventoryPlugin.verify_file', return_value=True)
    mocker.patch('ansible.plugins.inventory.yaml.InventoryModule.get_option', return_value=['.yaml', '.yml'])

    path = '/path/to/inventory.yaml'
    assert inventory_module.verify_file(path) == True

def test_verify_file_no_extension(inventory_module, mocker):
    mocker.patch('ansible.plugins.inventory.yaml.BaseFileInventoryPlugin.verify_file', return_value=True)
    mocker.patch('ansible.plugins.inventory.yaml.InventoryModule.get_option', return_value=['.yaml', '.yml'])

    path = '/path/to/inventory'
    assert inventory_module.verify_file(path) == True

def test_verify_file_invalid_extension(inventory_module, mocker):
    mocker.patch('ansible.plugins.inventory.yaml.BaseFileInventoryPlugin.verify_file', return_value=True)
    mocker.patch('ansible.plugins.inventory.yaml.InventoryModule.get_option', return_value=['.yaml', '.yml'])

    path = '/path/to/inventory.txt'
    assert inventory_module.verify_file(path) == False

def test_verify_file_super_returns_false(inventory_module, mocker):
    mocker.patch('ansible.plugins.inventory.yaml.BaseFileInventoryPlugin.verify_file', return_value=False)
    mocker.patch('ansible.plugins.inventory.yaml.InventoryModule.get_option', return_value=['.yaml', '.yml'])

    path = '/path/to/inventory.yaml'
    assert inventory_module.verify_file(path) == False
