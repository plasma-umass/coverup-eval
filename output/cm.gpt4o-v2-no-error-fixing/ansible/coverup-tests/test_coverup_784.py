# file: lib/ansible/plugins/inventory/toml.py:249-254
# asked: {"lines": [250, 251, 252, 253, 254], "branches": [[250, 251], [250, 254], [252, 253], [252, 254]]}
# gained: {"lines": [250, 251, 252, 253, 254], "branches": [[250, 251], [250, 254], [252, 253], [252, 254]]}

import os
import pytest
from unittest.mock import patch
from ansible.plugins.inventory.toml import InventoryModule

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_verify_file_toml_extension(inventory_module):
    with patch('ansible.plugins.inventory.BaseFileInventoryPlugin.verify_file', return_value=True):
        assert inventory_module.verify_file('test.toml') == True

def test_verify_file_non_toml_extension(inventory_module):
    with patch('ansible.plugins.inventory.BaseFileInventoryPlugin.verify_file', return_value=True):
        assert inventory_module.verify_file('test.txt') == False

def test_verify_file_invalid_path(inventory_module):
    with patch('ansible.plugins.inventory.BaseFileInventoryPlugin.verify_file', return_value=False):
        assert inventory_module.verify_file('test.toml') == False
