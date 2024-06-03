# file lib/ansible/plugins/inventory/yaml.py:87-94
# lines [87, 89, 90, 91, 92, 93, 94]
# branches ['90->91', '90->94', '92->93', '92->94']

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.inventory.yaml import InventoryModule

@pytest.fixture
def mock_base_file_inventory_plugin(mocker):
    mocker.patch('ansible.plugins.inventory.yaml.BaseFileInventoryPlugin.verify_file', return_value=True)

def test_verify_file_valid_yaml_extension(mock_base_file_inventory_plugin):
    inventory_module = InventoryModule()
    inventory_module.get_option = MagicMock(return_value=['.yaml', '.yml'])
    
    test_path = '/path/to/inventory.yaml'
    assert inventory_module.verify_file(test_path) == True

def test_verify_file_invalid_extension(mock_base_file_inventory_plugin):
    inventory_module = InventoryModule()
    inventory_module.get_option = MagicMock(return_value=['.yaml', '.yml'])
    
    test_path = '/path/to/inventory.txt'
    assert inventory_module.verify_file(test_path) == False

def test_verify_file_no_extension(mock_base_file_inventory_plugin):
    inventory_module = InventoryModule()
    inventory_module.get_option = MagicMock(return_value=['.yaml', '.yml'])
    
    test_path = '/path/to/inventory'
    assert inventory_module.verify_file(test_path) == True
