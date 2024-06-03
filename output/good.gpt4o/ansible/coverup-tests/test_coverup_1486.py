# file lib/ansible/plugins/inventory/generator.py:92-101
# lines []
# branches ['95->101']

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.inventory.generator import InventoryModule
from ansible.plugins.inventory import BaseInventoryPlugin
import ansible.constants as C

@pytest.fixture
def mock_base_inventory_plugin(mocker):
    mocker.patch('ansible.plugins.inventory.generator.BaseInventoryPlugin.verify_file', return_value=True)

@pytest.fixture
def mock_base_inventory_plugin_false(mocker):
    mocker.patch('ansible.plugins.inventory.generator.BaseInventoryPlugin.verify_file', return_value=False)

def test_verify_file_extension_config(mock_base_inventory_plugin):
    inventory_module = InventoryModule()
    path = '/path/to/file.config'
    
    assert inventory_module.verify_file(path) == True

def test_verify_file_extension_yaml(mock_base_inventory_plugin):
    inventory_module = InventoryModule()
    path = '/path/to/file.yaml'
    
    assert inventory_module.verify_file(path) == True

def test_verify_file_extension_invalid(mock_base_inventory_plugin):
    inventory_module = InventoryModule()
    path = '/path/to/file.txt'
    
    assert inventory_module.verify_file(path) == False

def test_verify_file_super_false(mock_base_inventory_plugin_false):
    inventory_module = InventoryModule()
    path = '/path/to/file.config'
    
    assert inventory_module.verify_file(path) == False
