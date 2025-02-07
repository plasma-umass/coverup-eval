# file: lib/ansible/plugins/inventory/toml.py:249-254
# asked: {"lines": [249, 250, 251, 252, 253, 254], "branches": [[250, 251], [250, 254], [252, 253], [252, 254]]}
# gained: {"lines": [249, 250, 251, 252, 253, 254], "branches": [[250, 251], [250, 254], [252, 253], [252, 254]]}

import os
import pytest
from ansible.plugins.inventory.toml import InventoryModule
from ansible.plugins.inventory import BaseFileInventoryPlugin

class MockBaseFileInventoryPlugin(BaseFileInventoryPlugin):
    def verify_file(self, path):
        return path != 'invalid.txt'

@pytest.fixture
def inventory_module(monkeypatch):
    module = InventoryModule()
    monkeypatch.setattr(BaseFileInventoryPlugin, 'verify_file', MockBaseFileInventoryPlugin().verify_file)
    return module

def test_verify_file_with_toml_extension(inventory_module):
    assert inventory_module.verify_file('test.toml') == True

def test_verify_file_with_non_toml_extension(inventory_module):
    assert inventory_module.verify_file('test.txt') == False

def test_verify_file_with_no_extension(inventory_module):
    assert inventory_module.verify_file('test') == False

def test_verify_file_with_invalid_file(inventory_module):
    assert inventory_module.verify_file('invalid.txt') == False
