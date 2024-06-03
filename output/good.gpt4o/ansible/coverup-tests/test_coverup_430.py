# file lib/ansible/plugins/inventory/toml.py:249-254
# lines [249, 250, 251, 252, 253, 254]
# branches ['250->251', '250->254', '252->253', '252->254']

import os
import pytest
from ansible.plugins.inventory.toml import InventoryModule
from unittest.mock import patch

@pytest.fixture
def mock_base_file_inventory_plugin(mocker):
    mocker.patch('ansible.plugins.inventory.toml.BaseFileInventoryPlugin.verify_file', return_value=True)

def test_verify_file_toml_extension(mock_base_file_inventory_plugin):
    inventory = InventoryModule()
    test_path = '/path/to/inventory.toml'
    
    assert inventory.verify_file(test_path) is True

def test_verify_file_non_toml_extension(mock_base_file_inventory_plugin):
    inventory = InventoryModule()
    test_path = '/path/to/inventory.txt'
    
    assert inventory.verify_file(test_path) is False

def test_verify_file_base_class_returns_false(mocker):
    mocker.patch('ansible.plugins.inventory.toml.BaseFileInventoryPlugin.verify_file', return_value=False)
    inventory = InventoryModule()
    test_path = '/path/to/inventory.toml'
    
    assert inventory.verify_file(test_path) is False
