# file lib/ansible/plugins/inventory/constructed.py:104-113
# lines [104, 106, 107, 108, 110, 111, 113]
# branches ['107->108', '107->113', '110->111', '110->113']

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.inventory.constructed import InventoryModule
from ansible.plugins.inventory import BaseInventoryPlugin, Constructable
import ansible.constants as C

@pytest.fixture
def inventory_module():
    return InventoryModule()

@pytest.fixture
def mock_super_verify_file(mocker):
    return mocker.patch('ansible.plugins.inventory.constructed.BaseInventoryPlugin.verify_file')

def test_verify_file_no_extension(inventory_module, mock_super_verify_file):
    mock_super_verify_file.return_value = True
    path = '/path/to/file'
    assert inventory_module.verify_file(path) == True

def test_verify_file_with_config_extension(inventory_module, mock_super_verify_file):
    mock_super_verify_file.return_value = True
    path = '/path/to/file.config'
    assert inventory_module.verify_file(path) == True

def test_verify_file_with_yaml_extension(inventory_module, mock_super_verify_file):
    mock_super_verify_file.return_value = True
    path = '/path/to/file.yaml'
    assert inventory_module.verify_file(path) == True

def test_verify_file_with_invalid_extension(inventory_module, mock_super_verify_file):
    mock_super_verify_file.return_value = True
    path = '/path/to/file.txt'
    assert inventory_module.verify_file(path) == False

def test_verify_file_super_returns_false(inventory_module, mock_super_verify_file):
    mock_super_verify_file.return_value = False
    path = '/path/to/file.yaml'
    assert inventory_module.verify_file(path) == False
